class ClassManagement:
    def __init__(self):
        self.school_classes = {}

    def create_classes(self):
        num_classes = int(input("Enter the number of classes in the school: "))
        for class_number in range(1, num_classes + 1):
            while True:
                num_students = int(input(f"Enter the number of students in Class {class_number}: "))
                if num_students > 33:
                    print("Error: Maximum of 33 students allowed per class. Please try again.")
                else:
                    self.school_classes[class_number] = num_students
                    break
        print("Classes created successfully.")

    def view_classes(self):
        print("\nClass Management:")
        for class_number, num_students in self.school_classes.items():
            print(f"Class {class_number}: {num_students} students")

    def delete_class(self):
        class_number = int(input("Enter the class number to delete: "))
        if class_number in self.school_classes:
            del self.school_classes[class_number]
            print(f"Class {class_number} deleted successfully.")
        else:
            print("Class not found.")

def main():
    school = ClassManagement()

    while True:
        print("\nMenu:")
        print("1. Create Classes")
        print("2. View Classes")
        print("3. Delete Class")
        print("4. Exit")

        choice = int(input("Enter your choice (1-4): "))

        if choice == 1:
            school.create_classes()
        elif choice == 2:
            school.view_classes()
        elif choice == 3:
            school.delete_class()
        elif choice == 4:
            print("Exiting...")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
