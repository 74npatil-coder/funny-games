import random
random_nu=random.randint(1,50)
chance=5
count=0
while count<chance:
    guess=int(input("Enter number from range(1,50): "))
    count+=1
    if random_nu==guess:
        print("Number is found!!!")
        break
    elif random_nu<guess:
        print("Please enter smaller number..")
    elif random_nu>guess:
        print("Please enter greater number..")
    
else:
    print(f"Opps, you fail cooreact number is {random_nu} ")
    



