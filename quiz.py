from question import Question

class Quiz:
    def __init__(self, title):
        self.title = title
        self.questions = []

    def add_question(self, question):
        if not isinstance(question, Question):
            raise TypeError("Only Question objects can be added to a Quiz.")
        self.questions.append(question)

    def attempt_quiz(self):
        score = 0
        total_questions = len(self.questions)
        
        print(f"\n--- Starting Quiz: {self.title} ({total_questions} Questions) ---")
        
        for question in self.questions:
            question.display()
            
            while True:
                try:
                    user_input = input("Your answer (enter the number, e.g., 1, 2...): ")
                    if not user_input.strip():
                        raise ValueError("Answer cannot be empty.")
                        
                    answer_index = int(user_input)
                    
                    if answer_index < 1 or answer_index > len(question.options):
                        raise ValueError("Invalid option number selected.")
                        
                    break 
                    
                except ValueError as e:
                    print(f"Invalid input. Please try again. ({e})")

            if question.is_correct(answer_index):
                score += 1
            
        print("--- Quiz Finished ---")
        return score, total_questions

    def to_dict(self):
        """Persistence: Returns a dictionary for JSON serialization."""
        return {
            "title": self.title,
            "questions": [q.to_dict() for q in self.questions]
        }

    @classmethod
    def from_dict(cls, data):
        """Persistence: Creates a Quiz object from saved data (Deserialization)."""
        quiz = cls(data['title'])
        for q_data in data['questions']:
            question = Question(
                q_data['text'],
                q_data['options'],
                q_data['correct_answer']
            )
            quiz.add_question(question)
        return quiz
