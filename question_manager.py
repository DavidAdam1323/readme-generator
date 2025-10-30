class QuestionManager:
  def __init__(self):
    self.questions = []
  
  def get_basic_questions(self):
    basic_questions = [
      {
        "type": "input",
        "name": "title",
        "message": "What is your project title?"
      },
      {
        "type": "input",
        "name": "description",
        "message": "Write a short description of your project:"
      }
    ]
    
    return basic_questions
  
  def display_welcome(self):
    print("\n" + "="*50)
    print(" "*17 + "README GENERATOR" + " "*17)
    print("="*50 + "\n")
    print("Please, answer the following questions to create a README file.\n")
