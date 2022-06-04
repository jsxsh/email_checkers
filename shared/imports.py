

class Importer:
    def __init__(self,name):
        if name == "Amazon":
            from scripts.Amazon.Amazon import Checker
            object = Checker
        if name == "BK":
            from scripts.BK.BK import Checker
            object = Checker
        if name == "Hulu":
            from scripts.Hulu.Hulu import Checker
            object = Checker
        if name == "Indeed":
            from scripts.Indeed.Indeed import Checker
            object = Checker
        if name == "LinkedIn":
            from scripts.LinkedIn.LinkedIn import Checker
            object = Checker
        if name == "Netflix":
            from scripts.Netflix.Netflix import Checker
            object = Checker
        if name == "Snagajob":
            from scripts.Snagajob.Snagajob import Checker
            object = Checker
        if name == "Uber":
            from scripts.Uber.Uber import Checker
            object = Checker
        if name == "WW":
            from scripts.WW.WW import Checker
            object = Checker
        self.checker = object

