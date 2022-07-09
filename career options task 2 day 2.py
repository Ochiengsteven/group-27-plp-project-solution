career_list = ["Data science",
                           "Web development",
                           "Data analysis",
                           "Cyber security",
                           "Ethical hacking"]

career_questions = ["What do i need to become a data scientist?",
                                        "How can i become a fullstack webdeveloper?",
                                        "How can i start data analysis?",
                                        "What is Cyber security?",
                                        "Hacking! isn't that dangerous?"]

career_advice = ["Data science is not a bad idea, it's one of the best paying jobs in this centuary.",
                                "Web development is also a hotcake in the programming field.",
                                "Data analysis goes hand in hand with data science.",
                                "Cyber security is a crucial aspect in the softaware engineering world.",
                                "Hacking isn't that dangerouse if done with the right intentions."]

print("Available careers are: ", career_list)
while True:
    prompt = input("Please enter your preferred career: ")

    if prompt in career_list and prompt == career_list[0]:
        print("Your requested career is", prompt)
        print("\n" , career_questions[0])
        print("\n ", career_advice[0])

    elif prompt in career_list and prompt == career_list[1]:
        print("Your requested career is", prompt)
        print("\n" , career_questions[1])
        print("\n ", career_advice[1])

    elif prompt in career_list and prompt == career_list[2]:
        print("Your requested career is", prompt)
        print("\n" , career_questions[2])
        print("\n ", career_advice[2])

    elif prompt in career_list and prompt == career_list[3]:
        print("Your requested career is", prompt)
        print("\n" , career_questions[3])
        print("\n ", career_advice[3])

    elif prompt in career_list and prompt == career_list[4]:
        print("Your requested career is", prompt)
        print("\n" , career_questions[4])
        print("\n ", career_advice[4])

    else:
        print("Invalid input, kindly try again")


    done_already = input("Enter (y/n) to continue or quit: ")
    if done_already == "yes" or done_already == "y".lower():
        continue
    else:
        print("Your inputed career is", prompt)
        break