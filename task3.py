from typing import List
class Agent:
    def __init__(self, val):
        self.value = val
    def value(option:int)->float:
        return value[int]

# question 1
def isParetoImprovement(agents:List[Agent],option1:int,option2:int)->bool:
    isImprove = True
    for a in agents :
        if a.value[option1] < a.value[option2] :
            isImprove = False
    return isImprove

# question 2
def isParetoOptimal(agents:List[Agent],option:int,allOptions:List[int])->bool:
    isPare = True
    for x in allOptions:
        if x != option and isParetoImprovement(agents,x,option) :
            isPare = False
    return isPare

# check the algorithms
listAmi: List[int] = [1,2,3,4,5]
listTami: List[int] = [3,1,2,5,4]
listRami: List[int] = [3,5,5,1,1]

Ami = Agent(listAmi)
Tami = Agent(listTami)
Rami = Agent(listRami)

listAgents: List[Agent] = [Ami,Tami,Rami]
option = 1
options: List[int] = [0,1,2,3,4]

print(isParetoOptimal(listAgents,option,options))
