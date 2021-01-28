computedStats = {
  "avg": 0.0,
  "max": 0.0,
  "min": 0.0
}
  
G_Obj_list=[]

def Delet_list():
    del G_Obj_list[:]
    
def Append_list(list=[]):
    for x in list:
        G_Obj_list.append(x)
        
def calculateStats(numbers):
  if len(numbers) == 0:
    computedStats["avg"] =float("nan")
    computedStats["max"] =float("nan")
    computedStats["min"] =float("nan")
  else: 
    computedStats["avg"] =sum(numbers) / len(numbers)
    computedStats["max"] =max(numbers)
    computedStats["min"] =min(numbers)
  return computedStats

class EmailAlert:
    def __init__(self):
        self.emailSent = False

class LEDAlert:
    def __init__(self):
        self.ledGlows = False


class StatsAlerter:
    def __init__(self,maxThreshold,Obj_list=[]):
        Delet_list()
        Append_list(Obj_list)
        self.maxThreshold = maxThreshold

    def checkAndAlert(self, lst):
        if len(lst) == 0:
            print("Empty/Invalid Object List")
        else:
            if max(lst) > self.maxThreshold:
                print("maxThreshold has been reached\nSend Email alert\nGlow Led Alert")
                G_Obj_list[0].emailSent = True
                G_Obj_list[1].ledGlows = True
            else:
                print("maxThreshold has not reached\nEmail alert not sent\nDont Glow Led Alert")
                G_Obj_list[0].emailSent = False
                G_Obj_list[1].ledGlows = False
                
