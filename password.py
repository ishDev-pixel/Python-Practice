password="ishrat"
attempts=0
max_attempts=3

while attempts <= max_attempts:
    passwd=input("enter password")
    attempts+=1
    if passwd==password:
        print("unlocked!")
        break
    else:
        remains=max_attempts-attempts
        if remains >0:
            print("you have attempst")
        
else:
    print("account locked")            