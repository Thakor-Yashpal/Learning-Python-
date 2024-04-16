def funny():
    current_year = 2024  
    birth_year = int(input("Type Your Birth Year: "))
    your_age = current_year - birth_year
    if your_age < 18:
        print("You are so young")
    else:
        print("You are an adult")
    print("Your age is:", your_age)
funny()
