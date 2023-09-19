while True:
    user_input = input("Enter a number or 'q' to quit: ")

    if user_input.lower() == 'q':
        print("Exiting the program.")
        break

    try:
        number = float(user_input)
        power = number ** 2
        print(f"The power of {number} is {power}")
    except ValueError:
        print("Invalid input. Please enter a number or 'q' to quit.")
