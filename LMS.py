import pandas as pd

StudentAccountDictionary = {
    "StudentId": [10001, 10002, 10003],
    "StudentName": ["Ahmad", "Ali", "yth"],
    "StudentClass": ["1", "2", "3"],
    "Subjects": [["Math", "English", "Science"], ["Math", "Chemistry", "Science"],
                 ["islamicStudies", "English", "Physics"]]
}

studentDF = pd.DataFrame(StudentAccountDictionary)
studentDF.to_csv("StudentData.csv", index=False)

while True:
    print("\n" + "=" * 30)
    choice = input(
        "1. Student Registration\n2. Student Information Fetch\n3. Student Information Update\n4. Exit\nSelection: ")

    if choice == "1":
        print("====== Student Registration =======")
        studentDF = pd.read_csv("StudentData.csv")

        new_id = int(input("Enter Student Id: "))
        new_name = input("Enter Student Name: ")
        new_class = input("Enter Student Class: ")

        sub_list = []
        num_subs = int(input("How many subjects? "))
        for i in range(num_subs):
            sub = input(f"Enter Subject {i + 1}: ")
            sub_list.append(sub)

        new_row = {"StudentId": new_id, "StudentName": new_name, "StudentClass": new_class, "Subjects": sub_list}
        studentDF = pd.concat([studentDF, pd.DataFrame([new_row])], ignore_index=True)

        studentDF.to_csv("StudentData.csv", index=False)
        print("Student Registered Successfully!")

    elif choice == "2":
        print("====== Student Information Fetch ========")
        studentDF = pd.read_csv("StudentData.csv")
        studentId = int(input("Enter Student Id: "))

        if studentId not in list(studentDF["StudentId"]):
            print("Student Id Not Found")
            continue

        for i in range(len(studentDF)):
            if studentDF["StudentId"][i] == studentId:
                print(f"Student Name : {studentDF['StudentName'][i]}")
                print(f"Student Class : {studentDF['StudentClass'][i]}")
                print(f"Student Subjects : {studentDF['Subjects'][i]}")


    elif choice == "3":

        print("====== Student Information Update =======")

        studentDF = pd.read_csv("StudentData.csv")

        studentId = int(input("Enter Student Id: "))


        if studentId not in studentDF["StudentId"].values:
            print("Student Id Not Found")

            continue

        for i in range(len(studentDF)):

            if studentDF["StudentId"][i] == studentId:

                print("What do you want to update?")

                updateChoice = input("1. Name\n2. Class\n3. Subjects\nSelection: ")

                if updateChoice == "1":

                    new_val = input("Enter New Student Name: ")

                    studentDF.at[i, 'StudentName'] = new_val

                    print(f"Updated Name to {new_val}")


                elif updateChoice == "2":

                    new_val = input("Enter New Student Class: ")

                    studentDF.at[i, 'StudentClass'] = new_val

                    print(f"Updated Class to {new_val}")


                elif updateChoice == "3":

                    new_sub_list = []

                    num_subs = int(input("How many subjects? "))

                    for j in range(num_subs):
                        sub = input(f"Enter Subject {j + 1}: ")

                        new_sub_list.append(sub)

                    studentDF.at[i, 'Subjects'] = new_sub_list

                    print("Updated Subjects.")


        studentDF.to_csv("StudentData.csv", index=False)

        print("Changes saved to CSV successfully.")

    elif choice == "4":
        print("Exiting...")
        break