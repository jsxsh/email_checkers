import pandas as pd
from datetime import datetime,date
import csv
import os


class CSVEditor:

    def __init__(self,input_file,name,email_name="Email",save_skipped=True):
        self.input_file = input_file
        self.name = name
        self.email_name = email_name
        self.save_skipped = save_skipped
        self.input_records = self.read()
        self.create()


    def read(self):
        emails = []
        try: frame = pd.read_csv(f"{self.input_file}.csv",dtype=str) 
        except: frame = pd.read_csv(f"{self.input_file}.csv",dtype=str,encoding='latin-1') 
        self.columns = list((frame).columns); self.columns.remove(self.email_name)
        try: self.columns.remove("email_exception")
        except: pass

        self.dict_originals = {}
        for x in range(len(frame[self.email_name])):
            try:
                email = str(frame[self.email_name][x])
                if "@" not in email: raise Exception("Not an email")
                self.dict_originals[email] = {}
                emails.append(email)
                for item in self.columns:
                    try:
                        self.dict_originals[email][item] = str(frame[item][x])
                    except:
                        self.dict_originals[email][item] = ""

            except Exception("Not an email") as exc:
                pass
        print(f"{len(emails)} records found.")
        emails = list(set(emails))
        print(f"{len(emails)} records left after removing duplicates.")
        return emails


    def create(self):
        now = datetime.now(); today = date.today()
        time_stamp = now.strftime("%H-%M"); date_stamp = today.strftime("%d-%m-%Y")
        folder_name = f"{self.name}_{date_stamp}-{time_stamp}"

        try: os.mkdir("results")
        except: pass
        try: os.mkdir(f"results/{folder_name}")
        except: pass

        self.file_name = f"results/{folder_name}/{self.name}_{date_stamp}-{time_stamp}.csv"
        self.file_name_skipped = f"results/{folder_name}/{self.name}_skipped_{date_stamp}-{time_stamp}.csv"
        

        self.columns.insert(0,"Status"); self.columns.insert(0,"Email")
        with open(self.file_name,"w",newline="",encoding="utf-8") as f:
            writer = csv.writer(f)
            writer.writerow(self.columns)

        self.columns.pop(1);self.columns.insert(1,"email_exception")
        if self.save_skipped == True:
            with open(self.file_name_skipped,"w",newline="",encoding="utf-8") as f:
                writer = csv.writer(f)
                writer.writerow(self.columns)

        self.columns.pop(0);self.columns.pop(0)


    def save(self,results,skipped=[]):
        records = []
        for result in results:
            try:
                record = []
                email = result[0]
                status = result[1]
                for item in self.columns:
                    record.append(self.dict_originals[email][item])
                record.insert(0,status);record.insert(0,email)
                record = tuple(record)
                records.append(record)
            except Exception as exc:
                pass

        with open(self.file_name,"a",newline="",encoding="utf-8") as f:
            writer = csv.writer(f)
            writer.writerows([x for x in records])


        if self.save_skipped == True:
            skipped_emails = []
            for result in skipped:
                try:
                    record = []
                    email = result[0]
                    exception = result[1]
                    for item in self.columns:
                        record.append(self.dict_originals[email][item])
                    record.insert(0,exception);record.insert(0,email)
                    record = tuple(record)
                    skipped_emails.append(record)
                except Exception as exc:
                    pass
            with open(self.file_name_skipped,"a",newline="",encoding="utf-8") as f:
                writer = csv.writer(f)
                writer.writerows([x for x in skipped_emails])

