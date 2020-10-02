import random
n=random.randint(1,9)
i=1
while(i<6):
    v=int(input("enter your choice from 1 to 9 "))
    if(v==n):
        print("your number",i,"guess is right")
        break
    else:
        print("your guess is wrong")
    i=i+1    

