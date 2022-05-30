
class Importer:
    def __init__(self,name):
        if name == "Amazon":
            from scripts.Amazon.Amazon_28_05 import checker
            object = checker
        if name == "BK":
            from scripts.BK.BK_28_05 import checker
            object = checker
        if name == "Hulu":
            from scripts.Hulu.Hulu_28_05 import checker
            object = checker
        if name == "Indeed":
            from scripts.Indeed.Indeed_28_05 import checker
            object = checker
        if name == "LinkedIn":
            from scripts.LinkedIn.LinkedIn_28_05 import checker
            object = checker
        if name == "Netflix":
            from scripts.Netflix.Netflix_28_05 import checker
            object = checker
        if name == "Snagajob":
            from scripts.Snagajob.Snagajob_28_05 import checker
            object = checker
        if name == "Uber":
            from scripts.Uber.Uber_28_05 import checker
            object = checker
        if name == "WW":
            from scripts.WW.WW_28_05 import checker
            object = checker
        self.checker = object
