#need to import stuff

def main():
    user_list = []

    while True:
        user_info = {}
        name = get_valid_input("Enter your name (4-30 characters): ", 4, 30)
        weight = get_valid_weight_input()
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

            file_name = "bmi.txt"
            if os.path.exists(file_name):
                create_new_file = input(f"A file named '{file_name}' already exists. Do you want to create a new file? (yes/no): ")
                if create_new_file.lower() != 'yes':
                    with open(file_name, "a") as file:
                        for person in user_list:
                            file.write(f"{person['Name']} :{person['Weight']} :{person['Height']} :{person['BMI']:.2f}\n")
            else:
                save_to_file(user_list, file_name)

            break