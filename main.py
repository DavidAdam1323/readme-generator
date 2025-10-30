from question_manager import QuestionManager

def main():
  question_manager = QuestionManager()
  question_manager.display_welcome()
  
  questions = question_manager.get_basic_questions()
  print("Questions to be used:", len(questions))
  print("First Question:", questions[0]["message"])
  print("Second Question:", questions[1]["message"])
  
  # print("Welcome to README generator!")
  # print("Testing...")

if __name__ == "__main__":
  main()