
students_details = []
students = {}

def add_entry():
    name = input ( "Enter Name" )
    student_id = input ( "Enter Id" )
    students["Name"] = name
    students["student_id"] = student_id
    students_details.append(students)

def show_entry():
    print ( f"{students}" )
    print(f"{students_details}")

while True:
    take = input ( " Do you want to add student Y or N" )
    if take == "y" or take == "Y":
        add_entry ()
        show_entry ()
    else:
        print ( "Thanks" )
        #print(f"{students_details}")
        for one in students_details:
            for two in one :
                print(f"{two}")
        break
