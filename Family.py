import datetime

class Patient:
    def __init__(self, name, age, gender, medical_history, current_symptoms):
        self.name = name
        self.age = age
        self.gender = gender
        self.medical_history = medical_history
        self.current_symptoms = current_symptoms
        self.record = []

    def add_record(self, date, symptoms, medication, doctor_notes):
        record = {
            "date": date,
            "symptoms": symptoms,
            "medication": medication,
            "doctor_notes": doctor_notes
        }
        self.record.append(record)

    def get_record(self, date=None):
        if date:
            for record in self.record:
                if record["date"] == date:
                    return record
            return None
        else:
            return self.record

    def print_record(self):
        for record in self.record:
            print(f"Date: {record['date']}")
            print(f"Symptoms: {record['symptoms']}")
            print(f"Medication: {record['medication']}")
            print(f"Doctor Notes: {record['doctor_notes']}\n")

class Family:
    def __init__(self):
        self.members = []

    def add_member(self, patient):
        self.members.append(patient)

    def get_member(self, name):
        for member in self.members:
            if member.name == name:
                return member
        return None

    def print_family_records(self):
        for member in self.members:
            print(f"Patient: {member.name}\n")
            member.print_record()

def main():
    family = Family()

    while True:
        print("\nFamily Health Monitoring System")
        print("1. Add a new family member")
        print("2. Add a health record for a family member")
        print("3. View health records for a family member")
        print("4. View health records for the entire family")
        print("5. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            name = input("Enter patient name: ")
            age = int(input("Enter patient age: "))
            gender = input("Enter patient gender: ")
            medical_history = input("Enter patient medical history: ")
            current_symptoms = input("Enter patient current symptoms: ")
            patient = Patient(name, age, gender, medical_history, current_symptoms)
            family.add_member(patient)
            print("Family member added successfully!")

        elif choice == "2":
            member_name = input("Enter the name of the family member: ")
            member = family.get_member(member_name)
            if member:
                date = datetime.date.today().strftime("%Y-%m-%d")
                symptoms = input("Enter symptoms: ")
                medication = input("Enter medication: ")
                doctor_notes = input("Enter doctor notes: ")
                member.add_record(date, symptoms, medication, doctor_notes)
                print("Health record added successfully!")
            else:
                print("Family member not found!")

        elif choice == "3":
            member_name = input("Enter the name of the family member: ")
            member = family.get_member(member_name)
            if member:
                date = input("Enter date (YYYY-MM-DD) to view specific record (leave blank to view all records): ")
                if date:
                    record = member.get_record(date)
                    if record:
                        print(f"Date: {record['date']}")
                        print(f"Symptoms: {record['symptoms']}")
                        print(f"Medication: {record['medication']}")
                        print(f"Doctor Notes: {record['doctor_notes']}")
                    else:
                        print("No record found for the given date!")
                else:
                    member.print_record()
            else:
                print("Family member not found!")

        elif choice == "4":
            family.print_family_records()

        elif choice == "5":
            print("Exiting the system...")
            break

        else:
            print("Invalid choice!")

if __name__ == "__main__":
    main()