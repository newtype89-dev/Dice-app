#moduals
import random

#roll funtion
def die_roll(i):
    roll= random.randint(1,i)
    return roll
 

#result list
roll_results=[]

#choice logic
for roll in roll_results:
    i=int(input("roll a D"))
    roll_results.append(roll)

print(roll_results)
