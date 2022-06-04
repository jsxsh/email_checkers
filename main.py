import logging
import concurrent.futures
import time
import gc
import os

from shared.csv_editor import CSVEditor
from shared.imports import Importer

class Main:

    def __init__(self,name,chunk_size,max_workers,input_file,start_from,count_checkpoint=100,testing=False):
        self.name = name
        self.testing = testing
        self.chunk_size = chunk_size
        self.max_workers = max_workers
        self.input_file = input_file
        self.start_from = start_from
        self.count_checkpoint = count_checkpoint
        try: os.mkdir("logs")
        except: pass
        logging.basicConfig(filename=f'logs/main.log', level=logging.INFO, filemode='w', format='%(asctime)s - %(levelname)s - %(message)s', datefmt='%d-%m-%y %H:%M:%S')
        logging.info(f"{self.name} script started.")
        self.checker = Importer(self.name).checker
        self.run_chunk()
        
    def run_chunk(self):
        editor = CSVEditor(input_file=self.input_file,name=self.name)
        self.all_records = editor.input_records
        logging.info(f"{len(self.all_records)} emails to check.")
        
        for number in range(self.start_from,len(self.all_records),self.chunk_size):
            self.skipped_emails = []
            self.chunk_results = []
            self.chunk = []
            self.count = 0

            self.create_chunk(number)
            self.process_chunk()

            editor.save(results=self.chunk_results,skipped=self.skipped_emails)

            gc.collect()

            logging.info(f"Chunk completed. {len(self.chunk_results)} emails saved. {len(self.skipped_emails)} email skipped.")
            print(f"Chunk completed. {len(self.chunk_results)} emails saved. {len(self.skipped_emails)} email skipped.")
        
            if self.testing:
                break

    def create_chunk(self,index):
        for x in range(index,index+self.chunk_size):
            try:
                self.chunk.append(self.all_records[x])
            except Exception as exc:
                print(exc)
                break
        print(f"Scraping {index}-{index+self.chunk_size}.")
        logging.info(f"Scraping {index}-{index+self.chunk_size}.")

    def process_chunk(self):
        start = time.time()
        with concurrent.futures.ThreadPoolExecutor(max_workers=self.max_workers) as executor:
            futures = []
            for pair in self.chunk:
                futures.append(executor.submit(self.checker,pair))
            for future in concurrent.futures.as_completed(futures):
                r = future.result().response
                if "@" in str(r[0]):
                    self.chunk_results.append(r[0])
                if "@" in str(r[1]):
                   self.skipped_emails.append(r[1])
                self.count+=1
                if self.count%self.count_checkpoint==0:
                    print(f"{self.count} emails checked.")
                    logging.info(f"{self.count} emails checked.")
        end = time.time()

        logging.info(f"{self.count} emails checked.")
        logging.info(f"Total: {end-start}")




Main(start_from=0,chunk_size=200,max_workers=10,input_file="2324mayVSfeed",name="Amazon",testing=True)




