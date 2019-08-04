Employee = []
company = True


class Employeess:

    def __init__(self, Name, Department, Position, Rate):
        self.Name = Name
        self.Department = Department
        self.Position = Position
        self.Rate = Rate

    def compute(self, Hourly):
        return Hourly * self.Rate


while company:
    print("""
------------------------------------------------------------------
                "CHOOSE YOUR OPTION BELOW: "
                (1.) Add An Employee: 
                (2.) Enter The Hourly Of Employee: 
                (3.) Show The Employees Informations: 
                (4.) EXIT:
------------------------------------------------------------------    
          """)

    print("Enter The Option:", end="")
    user = int(input())

    if user == 1:
         
            print("Type The Name: ", end="")     
            Name = (input())

            print("Type The Department: ", end="") 
            Department = input()

            print("Type The Position: ", end="") 
            Position = input()

            print("Type The Rate: ", end="") 
            Rate = int(input())

            Employee.append(Employeess(Name, Department, Position, Rate))

            continue

    elif user == 2:
        e1m = Employeess(Name, Department, Position, Rate)
        print("Type The Index Of The Employee: ", end="")

        e = int(input())
        print(Employee[e].Name, "HAS BEEN SELECTED")
        print("Enter The Hourly Of Employee: ", end="")
        l = int(input())
        print(Employee[e].Rate * l)
        continue

    elif user == 3:

        for ex in Employee:
            print("\nName:", ex.Name, "\nDepartment:", ex.Department, "\nPosition:", ex.Position, "\nRate:", ex.Rate,"\n")

        continue

    elif user == 4:
        running = False

    else:
        print("WRONG!!! PLEASE TRY AGAIN LATER:")
        
        continue
     
    break
