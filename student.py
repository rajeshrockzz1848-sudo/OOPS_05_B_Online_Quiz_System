class Student:
    next_id = 1001 
    
    def __init__(self, name, student_id=None):
        if student_id is None:
            self.student_id = Student.next_id
            Student.next_id += 1
        else:
            self.student_id = student_id
            
        self.name = name
        self.scores = {} 

    def record_score(self, quiz_title, score, total_questions):
        self.scores[quiz_title] = (score, total_questions)

    def get_summary(self):
        report = {
            "ID": self.student_id,
            "Name": self.name,
            "Total_Quizzes_Attempted": len(self.scores),
            "Quiz_Details": self.scores
        }
        return report

    def to_dict(self):        
        serializable_scores = {title: list(data) for title, data in self.scores.items()}
        return {
            "id": self.student_id,
            "name": self.name,
            "scores": serializable_scores
        }

    @classmethod
    def from_dict(cls, data):
        student = cls(data['name'], student_id=data['id'])
        student.scores = {title: tuple(data) for title, data in data['scores'].items()}
        return student
