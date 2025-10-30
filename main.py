from question_manager import QuestionManager

def main():
  question_manager = QuestionManager()
  question_manager.display_welcome()
  
  questions = question_manager.get_basic_questions()
  print(f"Ready to ask {len(questions)} questions:\n")
  
  for i, question in enumerate(questions, 1):
    print(f"{i}. {question["message"]}")
    
  print(f"\nNotice: The license question has {len(questions[4]["choices"])} options to choose from!")
  
  # print("First Question:", questions[0]["message"])
  # print("Second Question:", questions[1]["message"])
  
  # print("Welcome to README generator!")
  # print("Testing...")

if __name__ == "__main__":
  main()