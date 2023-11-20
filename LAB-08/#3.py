#3
class Dates:
    def __init__(self,dates):
        self.dates=dates
    @classmethod
    def toDashDate(cls,dates):
        dates=dates.replace('/','-')
        return cls(dates)
    def getDate(self):
        return self.dates
date1 = Dates("05-09-2020")
dateFromDB = "05/09/2020"
date2= Dates.toDashDate(dateFromDB)
if(date1.getDate() == date2.getDate() ):
    print("Equal")
else:
    print("Unequal")


