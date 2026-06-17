# Kimberly Smith
# CIS261
# WK10 VIBE Coding

"""
Student Grade Calculator
This program was created, reviewed, tested, and improved with the help of VIBE/AI.
It manages student records including test scores and calculates grades.
"""

def load_students():
    """Load student records from student_grades.txt file."""
    students = []
    try:
        with open('student_grades.txt', 'r') as file:
            for line in file:
                line = line.strip()
                if line:
                    parts = line.split('|')
                    if len(parts) == 7:
                        student = {
                            'name': parts[0],
                            'id': parts[1],
                            'test1': float(parts[2]),
                            'test2': float(parts[3]),
                            'test3': float(parts[4]),
                            'average': float(parts[5]),
                            'grade': parts[6]
                        }
                        students.append(student)
        print(f"Loaded {len(students)} student(s) from file.")
    except FileNotFoundError:
        print("No existing student records file found. Starting fresh.")
    except Exception as e:
        print(f"Error loading students: {e}")
    
    return students


def save_students(students):
    """Save student records to student_grades.txt file in pipe-delimited format."""
    try:
        with open('student_grades.txt', 'w') as file:
            for student in students:
                line = f"{student['name']}|{student['id']}|{student['test1']:.2f}|{student['test2']:.2f}|{student['test3']:.2f}|{student['average']:.2f}|{student['grade']}\n"
                file.write(line)
        print(f"Successfully saved {len(students)} student record(s) to file.")
    except Exception as e:
        print(f"Error saving students: {e}")


def calculate_average(test1, test2, test3):
    """Calculate the average of three test scores."""
    return (test1 + test2 + test3) / 3


def get_letter_grade(average):
    """Calculate letter grade based on average score."""
    if average >= 90:
        return 'A'
    elif average >= 80:
        return 'B'
    elif average >= 70:
        return 'C'
    elif average >= 60:
        return 'D'
    else:
        return 'F'


def add_student(students):
    """Add a new student record to the list."""
    print("\n--- Add New Student ---")
    
    try:
        name = input("Enter student name: ").strip()
        if not name:
            print("Student name cannot be empty.")
            return
        
        student_id = input("Enter student ID: ").strip()
        if not student_id:
            print("Student ID cannot be empty.")
            return
        
        test1 = float(input("Enter Test 1 score (0-100): "))
        if test1 < 0 or test1 > 100:
            print("Test score must be between 0 and 100.")
            return
        
        test2 = float(input("Enter Test 2 score (0-100): "))
        if test2 < 0 or test2 > 100:
            print("Test score must be between 0 and 100.")
            return
        
        test3 = float(input("Enter Test 3 score (0-100): "))
        if test3 < 0 or test3 > 100:
            print("Test score must be between 0 and 100.")
            return
        
        average = calculate_average(test1, test2, test3)
        grade = get_letter_grade(average)
        
        student = {
            'name': name,
            'id': student_id,
            'test1': test1,
            'test2': test2,
            'test3': test3,
            'average': average,
            'grade': grade
        }
        
        students.append(student)
        print(f"Student '{name}' added successfully with grade {grade}!")
    
    except ValueError:
        print("Invalid input. Please enter valid numbers for test scores.")
    except Exception as e:
        print(f"Error adding student: {e}")


def display_students(students):
    """Display all students in a formatted table."""
    if not students:
        print("\nNo students in the database yet.")
        return
    
    print("\n" + "="*110)
    print(f"{'Name':<20} {'ID':<12} {'Test 1':<10} {'Test 2':<10} {'Test 3':<10} {'Average':<10} {'Grade':<8}")
    print("="*110)
    
    for student in students:
        print(f"{student['name']:<20} {student['id']:<12} {student['test1']:<10.2f} {student['test2']:<10.2f} {student['test3']:<10.2f} {student['average']:<10.2f} {student['grade']:<8}")
    
    print("="*110)


def calculate_class_statistics(students):
    """Calculate and display class statistics."""
    if not students:
        print("\nNo students in the database yet.")
        return
    
    averages = [student['average'] for student in students]
    
    highest_average = max(averages)
    lowest_average = min(averages)
    class_average = sum(averages) / len(averages)
    
    print("\n--- Class Statistics ---")
    print(f"Highest average: {highest_average:.2f}")
    print(f"Lowest average: {lowest_average:.2f}")
    print(f"Class average: {class_average:.2f}")


def search_student(students):
    """Search for a student by name (case-insensitive)."""
    if not students:
        print("\nNo students in the database yet.")
        return
    
    search_name = input("\nEnter student name to search (case-insensitive): ").strip().lower()
    
    found = False
    for student in students:
        if student['name'].lower() == search_name:
            print(f"\nFound student:")
            print(f"Name: {student['name']}")
            print(f"ID: {student['id']}")
            print(f"Test 1: {student['test1']:.2f}")
            print(f"Test 2: {student['test2']:.2f}")
            print(f"Test 3: {student['test3']:.2f}")
            print(f"Average: {student['average']:.2f}")
            print(f"Grade: {student['grade']}")
            found = True
            break
    
    if not found:
        print(f"No student named '{search_name}' found.")


def display_menu():
    """Display the main menu and get user choice."""
    print("\n" + "="*50)
    print("STUDENT GRADE CALCULATOR")
    print("="*50)
    print("1. Add new student")
    print("2. Display all students")
    print("3. Search for student")
    print("4. View class statistics")
    print("5. Save and exit (or press ESC)")
    print("="*50)
    
    choice = input("Enter your choice (1-5 or ESC): ").strip()
    return choice


def main():
    """Main program loop."""
    students = load_students()

    while True:
        choice = display_menu()

        if choice == '1':
            add_student(students)
        elif choice == '2':
            display_students(students)
        elif choice == '3':
            search_student(students)
        elif choice == '4':
            calculate_class_statistics(students)
        elif choice == '5':
            save_students(students)
            print("Goodbye!")
            break
        elif choice.upper() == 'ESC':
            save_students(students)
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please enter a number between 1 and 5, or ESC to exit.")


if __name__ == "__main__":
    main()
