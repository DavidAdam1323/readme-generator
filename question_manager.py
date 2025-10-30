from InquirerPy import prompt

class QuestionManager:
  def __init__(self):
    self.questions = []

  def get_all_questions(self):
    basic_questions = [
      {
        "type": "input",
        "name": "title",
        "message": "What is your project title?",
        "validate": lambda answer: len(answer.strip()) > 0,
        "invalid_message": "Please, enter your project title."
      },
      {
        "type": "input",
        "name": "description",
        "message": "Write a short description of your project:",
        "validate": lambda answer: len(answer.strip()) > 0,
        "invalid_message": "Please, enter a description."
      },
      {
        "type": "input",
        "name": "installation",
        "message": "What are the installation instructions?"
      },
      {
        "type": "input",
        "name": "usage",
        "message": "How do you use this project?"
      },
      {
        "type": "list",
        "name": "license",
        "message": "Choose a license for your project:",
        "choices": ["MIT License", "Unlicense", "No license", "None"]
      },
      {
        "type": "input",
        "name": "author",
        "message": "What is your name (Author)?"
      },
      {
        "type": "input",
        "name": "email",
        "message": "What is your email address?"
      },
      {
        "type": "input",
        "name": "linkedin",
        "message": "What is your LinkedIn profile URL?"
      },
    ]
    
    return basic_questions
  
  def ask_questions(self):
    questions = self.get_all_questions()
    answers = prompt(questions)
    return answers
   
  def display_welcome(self):
    print("\n" + "="*50)
    print(" "*17 + "README GENERATOR" + " "*17)
    print("="*50 + "\n")
    print("Please, answer the following questions to create a README file.\n")
