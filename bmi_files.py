import os

def save_to_file(people, filename):
    with open(filename, "w") as file:
        file.write("Name ;Weight (kg) ;Height (cm) ;BMI\n")
        for person in people:
            file.write(f"{person['Name']} :{person['Weight']} :{person['Height']} :{person['BMI']:.2f}\n")


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
user_list = []
            
while True:
    user_info = {}
    name = get_valid_input("Enter your name (4-30 characters): ", 4, 30)
    weight =get_valid_weight_input()
    height = get_valid_height_input()
    bmi = get_bmi_score(weight, height)

    user_info["Name"] = name
    user_info["Weight"] = weight
    user_info["Height"] = height
    user_info["BMI"] = bmi

    user_list.append(user_info)

    program_continue = input("Do you want to enter information for another user? (yes/no): ")
    if program_continue.lower() != 'yes':
        print("\nUser Information:")
        for user in user_list:
            output = f"Name: {user['Name']}\nWeight: {user['Weight']} KG\nHeight: {user['Height']} Cm\nBMI: {user['BMI']:.2f}"
            print(output) 
        if os.path.exists("bmi.txt"):
            create_new_file = input("A file named 'bmi.txt' already exists. Do you want to create a new file? (yes/no): ")
            if create_new_file.lower() == 'yes':
                file_counter = 1
                while os.path.exists(f"bmi{file_counter}.txt"):
                    file_counter += 1
                save_to_file(user_list, f"bmi{file_counter}.txt")
            else:
                print("Data was not saved to a file.")
        else:
            save_to_file(user_list, "bmi.txt")

        break

