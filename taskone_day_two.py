import time #importing time for delay

get_username = False
print("Welcome to Serendipity Booksellers book club 📚😊")
while True:
    # print("Welcome to Serendipity Booksellers book club 📚😊")
    if get_username == False:
        username = input("Please enter your username.(type X or E to exit)\n")
        get_username = True
    input_text = input("Enter the number of books you have purchased this month (type X or E to exit and use N to change username)\n")
    try:
        #check if text is an integer
        number_of_books = int(input_text)
        #check if integer is a positive number
        assert number_of_books >= 0
    except:
        #check for E or X strings for exiting the program
        if input_text.upper() == "E" or input_text.upper() == "X":
            print("exiting program")
            print("bye 👋")
            break
        elif input_text.upper() == "N":
            get_username = False
            time.sleep(1.5)
            continue
        else:
            #set -1 value for elif print statement
            number_of_books = -1
        print()
    #if elif statements for printing points earned
    if number_of_books == 0:
        print("Sorry "+username+" ☹️ ,you have earned no points this month.")
    elif number_of_books == 1:
        print("Congratulations "+username+"👏 ,you have earned 6 points this month.")
    elif number_of_books == 2:
        print("Congratulations "+username+"👏 ,you have earned 12 points this month.")
    elif number_of_books == 3:
        print("Congratulations "+username+"👏 ,you have earned 32 points this month.")
    elif number_of_books >= 4:
        print("Congratulations "+username+"👏 ,you have earned 60 points this month.")
    elif number_of_books == -1:
        print("Oops "+username+"😵 !you did not enter a valid number")
    print()
    time.sleep(2) # Sleep for 2 seconds before restarting program