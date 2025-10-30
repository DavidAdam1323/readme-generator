from question_manager import QuestionManager

def main():
  question_manager = QuestionManager()
  question_manager.display_welcome()
  
  try:
    answers = question_manager.ask_questions()
    
    print("\n" + "="*50)
    print(" "*20 + "THANK YOU!" + " "*20)
    print("="*50 + "\n")
    print("Here's what you entered:\n")
    
    for key, value in answers.items():
      print(f"{key}: {value}")
      
  except Exception as error:
    print(f"Sorry, there was an error: {error}")

if __name__ == "__main__":
  main()