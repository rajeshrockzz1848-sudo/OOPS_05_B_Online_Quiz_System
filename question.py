class Question:
    def __init__(self, text, options, correct_answer):
        self.text = text
        self.options = options  
        if not isinstance(correct_answer, int) or correct_answer < 0 or correct_answer >= len(options):
            raise ValueError("Correct answer index is invalid.")
        self.correct_answer = correct_answer

    def display(self):
        print(f"\nQ: {self.text}")
        for i, option in enumerate(self.options):
            print(f"   {i+1}. {option}")

    def is_correct(self, answer_index):
        return (answer_index - 1) == self.correct_answer

    def to_dict(self):
        """Persistence: Returns a dictionary for JSON serialization."""
        return {
            "text": self.text,
            "options": self.options,
            "correct_answer": self.correct_answer
        }
