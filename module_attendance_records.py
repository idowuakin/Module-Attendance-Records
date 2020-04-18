from datetime import date


def create_account():
    # Creates user account as well as takes necessary input from user for creating account.
    print("Please fill the details to create account.")
    username = input("Please input the name for your account : ")
    password = input("Please input the password for your account : ")
    print(f"Account created with username {username}, password {password}")
    file = open('Login_data.txt', 'a')
    file.write(username+','+password+'\n')
    file.close()
    login()


def check_credentials(username, password):
    # Check if login credentials provided by the user are valid or not.
    credentials_file = open('Login_data.txt', 'r')
    for credentials in credentials_file:
        credentials = credentials.rstrip()
        username_ = credentials.split(',')[0]
        password_ = credentials.split(',')[1]
        if username_ == username and password_ == password:
            print(f"\n\nWelcome {username}")
            return "success"
    print("\n\nLogin failed.")
    exit()


def login():
    # Takes login credentials from the user and executes next function if credentials are valid
    print("\n\nPlease enter your login details.")
    name = input("Name: ")
    password = input("Password: ")
    validate = check_credentials(name, password)
    if validate == "success":
        menu()


def select_module():
    # Ask the lecturer to select the module on which they want to work
    module_file = open('Modules.txt', 'r')
    print("Choose a Module")
    modules = []
    for module_data in module_file:
        modules.append(module_data.split(', ')[0])
    for i, module_name in enumerate(modules):
        num = str(i+1)
        print(f"{num}. {module_name}")
    answer = input('>  ')
    module = modules[int(answer)-1]
    return module


def load_data(filename):
    # Load students data from the attendance file and returns seperate list for each field
    file = open(filename, 'r')
    data = []
    for students_data in file:
        data.append(students_data.rstrip())
    file.close()
    student_list = []
    present_list = []
    absent_list = []
    excuse_list = []
    for student_data in data:
        student_list.append(student_data.split(',')[0])
        present_list.append(int(student_data.split(',')[1]))
        absent_list.append(int(student_data.split(',')[2]))
        excuse_list.append(int(student_data.split(',')[3]))
    return student_list, present_list, absent_list, excuse_list


def record_attendance():
    # records attendance of the student on the selected module by lecturer
    module = select_module()
    student_list, present_list, absent_list, excuse_list = load_data(module+'.txt')
    print(f"There are {str(len(student_list))} students enrolled.")
    for i, student in enumerate(student_list):
        print(f"Student #{str(i+1)}: {student}")
        print("1. Present")
        print("2. Absent")
        print("3. Excused")
        answer = input(">  ")
        if answer == "1":
            present_list[i] = present_list[i]+1
        elif answer == "2":
            absent_list[i] = absent_list[i]+1
        elif answer == "3":
            excuse_list[i] = excuse_list[i]+1
    file = open(module+'.txt', 'w')
    for i, student in enumerate(student_list):
        file.write(student+','+str(present_list[i])+','+str(absent_list[i])+','+str(excuse_list[i])+'\n')
    file.close()


def generate_statistics():
    # generate statistics of students attendance for the selected module and save the statistics in a file
    module = select_module()
    student_list, present_list, absent_list, excuse_list = load_data(module+'.txt')
    num_of_students = len(student_list)
    num_of_classes = present_list[0]+absent_list[0]+excuse_list[0]
    average_attendance = sum(present_list)/num_of_students
    max_attendance = max(present_list)
    low_attenders = []
    non_attenders = []
    max_attenders = []
    for i, present in enumerate(present_list):
        if present*100/num_of_classes < 70:
            low_attenders.append(student_list[i])
        if present == 0:
            non_attenders.append(student_list[i])
        if present == max_attendance:
            max_attenders.append(student_list[i])
            
    print(f"Module: {module}")
    print(f"Number of students: {str(num_of_students)}")
    print(f"Number of Classes: {str(num_of_classes)}")
    print(f"Average Attendance: {str(average_attendance)}days")
    print(f"Low Attender(s): under 70.0%")
    print(f"        {', '.join(low_attenders)}")
    print(f"Non Attender(s):")
    print(f"        {', '.join(non_attenders)}")
    print(f"Best Attender(s):")
    print(f"        Attended {max_attendance}/{num_of_classes} days")
    print(f"        {', '.join(max_attenders)}")

    today = date.today()
    filename = module+'_'+today.strftime('%d_%m_%y')+'.txt'
    file = open(filename, 'w')
    file.write(f"Module: {module}\n")
    file.write(f"Number of students: {str(num_of_students)}\n")
    file.write(f"Number of Classes: {str(num_of_classes)}\n")
    file.write(f"Average Attendance: {str(average_attendance)}days\n")
    file.write(f"Low Attender(s): under 70.0%\n")
    file.write(f"        {', '.join(low_attenders)}\n")
    file.write(f"Non Attender(s):\n")
    file.write(f"        {', '.join(non_attenders)}\n")
    file.write(f"Best Attender(s):\n")
    file.write(f"        Attended {max_attendance}/{num_of_classes} days\n")
    file.write(f"        {', '.join(max_attenders)}\n")
    file.close()


def menu():
    # ask the lecturer to select the task they want to perform
    print("1. Record Attendance")
    print("2. Generate Statistics")
    print("3. Exit")
    answer = input(">  ")
    if answer == '1':
        record_attendance()
    elif answer == '2':
        generate_statistics()
    elif answer == '3':
        exit()
        

def main():
    # Initial function which verifies if the user has a account or not and then will run other fuctions according it.
    print("Do you have a account?")
    print("1. Yes, I want to login.")
    print("2. No, I want to create one.")
    print("3. Exit")
    answer = input(">  ")
    if answer == '1':
        login()
    elif answer == '2':
        create_account()
    elif answer == '3':
        exit()


main()
