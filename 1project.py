student = {}

while True:
    print("\n------STUDENT MANAGER APP------")
    print("1. Add Student")
    print("2. View Student")
    print("3. Cheak Result")
    print("4. exit")

    choice = input("Enter your choice")

    #Add Student
    if choice == "1":
        name = input("enter student name:")
        mark = int(input("Enter Marks:"))
        student[name]= marks
        print(f"{name} Succesful added!")

    #view student
    elif choice ==  "2":
        if not student:
            print("No student found!") 
        else:
            for name, marks in student.items():
                print(name,":", marks)  



    #cheak result
    elif choice =="3":
        name = input("Enter student Name:")

        if name in student:
            mark = student[name]

            if marks >=40:
                print("Pass")
            else:
                print("FAIL")    

        else:
            print("Student Not found!")        

    #exit
    elif choice == "4":  
        print("Execting.....") 
        break   
    else:
        print("in - valid input")