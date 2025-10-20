from quiz_system import QuizSystem
from quiz import Quiz
from question import Question
def initialize_system(system):
    if not system.quizzes:
        print("\n*** Initializing Default Quizzes ***")
        q1 = Question("What is Python primarily known for?", ["Web Browsing", "Data Analysis", "Game Console Design"], 1)
        q2 = Question("Which keyword is used for a function in Python?", ["def", "func", "function"], 0)
        q3 = Question("Which data structure is ordered and mutable?", ["tuple", "list", "set"], 1)
        
        quiz_oop = Quiz("OOP Fundamentals")
        quiz_oop.add_question(Question("What does OOP stand for?", ["Object Oriented Protocols", "Object Oriented Programming", "Optimal Operating Plan"], 1))
        quiz_oop.add_question(Question("A blueprint for creating objects is called a:", ["Instance", "Method", "Class"], 2))
        
        quiz_python = Quiz("Basic Python")
        quiz_python.add_question(q1)
        quiz_python.add_question(q2)
        quiz_python.add_question(q3)
        
        system.add_quiz(quiz_oop)
        system.add_quiz(quiz_python)
        
    if not system.students:
        print("\n*** Initializing Default Students ***")
        system.create_student("Alice")
        system.create_student("Bob")
    
    print("\n--- System Ready. Data persistence enabled. ---")

def generate_student_report(system):
    """Reports: Prints a detailed report for all students."""
    print("\n" + "="*40)
    print("           STUDENT PERFORMANCE REPORT")
    print("="*40)
    
    if not system.students:
        print("No students registered yet.")
        return

    for student_id, student in system.students.items():
        report = student.get_summary() 
        
        print(f"\n--- Student ID: {report['ID']} | Name: {report['Name']} ---")
        
        if report['Total_Quizzes_Attempted'] == 0:
            print("   -> No quizzes attempted yet.")
            continue

        print(f"   Quizzes Attempted: {report['Total_Quizzes_Attempted']}")
        print("   Details:")
        
        for quiz_title, (score, total) in report['Quiz_Details'].items():
            percent = (score/total) * 100
            print(f"     - {quiz_title}: {score}/{total} ({percent:.2f}%)")
    print("\n" + "="*40 + "\n")

def main():
    quiz_system = QuizSystem()
    initialize_system(quiz_system) 
    
    while True:
        print("\n" + "-"*30)
        print("ONLINE QUIZ SYSTEM MENU")
        print("-"*30)
        print("1. Attempt Quiz")
        print("2. Generate Student Report")
        print("3. View Available Quizzes")
        print("4. Register New Student")
        print("5. Exit")
        
        choice = input("Enter your choice (1-5): ")
        
        if choice == '1':
            try:
                student_id = int(input("Enter your Student ID: "))
                print("\nAvailable Quizzes: " + ", ".join(quiz_system.quizzes.keys()))
                quiz_title = input("Enter the title of the quiz to attempt: ")
                
                quiz_system.attempt_quiz(student_id, quiz_title)
                
            except ValueError as e:
                print(f"Invalid Input: {e}. Please enter a valid number for the ID.")
            except Exception as e:
                print(f"Error during quiz selection: {e}")
                
        elif choice == '2':
            generate_student_report(quiz_system)

        elif choice == '5':
            print("Saving all data...")
            quiz_system.save_data() 
            print("Thank you for using the Online Quiz System. Goodbye!")
            break
     
        elif choice == '3':
            print("\nAvailable Quizzes:")
            if not quiz_system.quizzes:
                print("No quizzes available.")
            for title in quiz_system.quizzes:
                print(f"- {title}")
                
        elif choice == '4':
            name = input("Enter new student's name: ")
            if name.strip():
                quiz_system.create_student(name)
            else:
                print("Student name cannot be empty.")
                
        else:
            print("Invalid choice. Please enter a number between 1 and 5.")

if __name__ == "__main__":
    main()
