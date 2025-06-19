#moduals
import random

#roll options
print("""Pick die
      1. d4
      2. d6
      3.d8
      4.d10
      5.d12
      6.d20
      7.d100""")
#print("how many dice?")

#random dice seeds
d4= random.randrange(1,4)
d6= random.randrange(1,6)
d8= random.randrange(1,8)
d10= random.randrange(1,10)
d12= random.randrange(1,12)
d20= random.randrange(1,20)
d100= random.randrange(1,100)

#result list
roll_results=[]

#choice logic

while(True):
    choice= int(input("pick a Die"))
    if(choice==1):
        roll_results.append(d4)
    elif(choice==2):
        roll_results.append(d6)
    elif(choice==3):
        roll_results.append(d8)
    elif(choice==4):
        roll_results.append(d10)
    elif(choice==5):
        roll_results.append(d12)
    elif(choice==6):
        roll_results.append(d20)
    elif(choice==7):
        roll_results.append(d100)
        
    print(roll_results)

