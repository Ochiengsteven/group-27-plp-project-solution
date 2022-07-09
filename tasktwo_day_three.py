# Calories from Fat and Carbohydrates A nutritionist who works for a fitness club helps members by evaluating their diets. As part of her evaluation,
# she asks members for the number of fat grams and carbohydrate grams that they consumed in a day. Then,
# she calculates the number of calories that result from the fat, using the following formula:
# Calories from fats fat grams * 9
# Next, she calculates the number of calories that result from the carbohydrates, using the following formula:
# Calories from carbs carb grams * 4
# The nutritionist asks you to write a program that will make these calculations.

import os #import os module for clearing command line
print("Hello and Welcome to AfyaDiet diet evaluation 🍴🍓😋")
username = input("Please enter member username\n")  # enter members username
os.system("cls")
calculatable = False #boolean to indicate whether the calcutation can be performed(initialised as false)
while True:
    print(username,"'s data")
    try:
        # check if inputs are a number(float)
        fat_grams = float(input("enter fat intake in grams\n"))
        carbohydrate_grams = float(input("enter carbohydrate intake in gramms)\n"))
        os.system("cls")
        # check if inputs are positive value
        assert fat_grams >= 0 and carbohydrate_grams >= 0
        calculatable = True #if the inputs are valid set calculatable to true 
    except:
        # If inputs are not valid show message and leave calculatable as false
        os.system("cls")
        print("invalid input please use a valid numerical value")
    if calculatable:#if calculatable is true perform the calculations
        fat_calories = fat_grams * 9
        carb_calories = carbohydrate_grams * 4
        total_calories = fat_calories + carb_calories
        print(username,"'s results are")
        print("      fat calories are: ", fat_calories)
        print("     carb calories are: ", carb_calories)
        print("     Total calories are: ", total_calories)
        calculatable = False #set to false for next loop
    else:#if calculatable is false pass
        pass
    choice=input("use R to run again, U to change user or X to  exit program\n") #prompt user to choose what to do next
    if choice.upper() == "R":
        print("running again")
    elif choice.upper() == "U":
        username = input("Please enter member username\n")  # enter members username
    elif choice.upper() == "X":
         print("exiting")
         break#break and hence exit program
    os.system("cls")