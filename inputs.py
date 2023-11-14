def get_bmi_score(weight, height):
    height_meters = height / 100
    bmi_score = weight / (height_meters ** 2)
    return bmi_score

def get_valid_input(prompt, min_length, max_length):
    while True:
        user_input = input(prompt)
        if min_length <= len(user_input) <= max_length and user_input.isalpha():
            return user_input
        else:
            print(f"Please retype, Min length is {min_length} and maximum is {max_length} LETTERS ONLY")

def get_valid_height_input():
    while True:
        try:
            height = int(input("Enter your height in centimeters (between 50 and 300): "))
            if 50 <= height <= 300:
                return height
            else:
                print("Please enter a valid height between 50 and 300 centimeters.")
        except ValueError:
            print("Please enter a valid number for age.")

def get_valid_weight_input():
    while True:
        try:
            weight = int(input("Enter your weight in kilograms (between 20 and 400 kilograms): "))
            if 20 <= weight <= 400:
                return weight
            else:
                print("Please enter a valid weight between 20 and 400 kilograms.")
        except ValueError:
            print("Please enter a valid number for your weight.")