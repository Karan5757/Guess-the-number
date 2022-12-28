# ***** Guess the number *****
hd={7}
print("Guess the hidden number")
print("Rules: \n 1) You'll have 7 attempts. \n 2) The number is between 1-50.")
while(True):
    a=int(input())
    if a==7:
        print("Congratulations")
        break
    elif a>0 and a<=12:
        print("You're really close")
    elif a>12 and a<=15:
        print("You're close")
    elif a>15 and a<=25:
        print("You are far")
    elif a>=25 and a<=50:
        print("Very far")
    else:
        print("Try again")
        continue
