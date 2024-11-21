


Weight = 48
Height = 162

BMI = Weight / (Height/100)**2
print("Your BMI is", BMI)

if BMI <= 18.4:
    print("You are underweight")

elif BMI <= 24.9:
    print("You are healthy")

elif BMI <= 29.9:
    print("You are overweight")

elif BMI <= 34.9:
    print("You are severely overweight")

elif BMI <= 39.9:
    print("You are obese")

else:
 print("You are severely obese")



Num3 = 26

if Num3 < 50:
    print("NUmber is less than 50")
     
    if Num3%2 == 0:
       print("Your number is even")

    else:
        print("Your number is odd")

else:
    print("Your number is greater than 50")





import datetime

current_time = datetime.datetime.now()
print("The time now is ", current_time)

import calendar

print("\n", calendar.calendar(2022))


Num = int(input("enter a number"))
print("Number to be checked:", Num)

if Num%2 == 0:
  print("Your number is even")

else:
   print("Your number is odd")



