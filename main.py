from question_manager import QuestionManager
from readme_generator import ReadmeGenerator

def main():
  question_manager = QuestionManager()
  question_manager.display_welcome()
  
  try:
    answers = question_manager.ask_questions()
    
    generator = ReadmeGenerator(answers)
    generator.generate_content()
    
    if generator.save_file():
      print("\n" + "="*50)
      print(" "*4 + "Success: README.md file has been created." + " "*4)
      print("="*50 + "\n")
    else:
      print("\n" + "="*50)
      print(" "*8 + "Error: README.md file not created." + " "*8)
      print("="*50 + "\n")
      
  except Exception as error:
    print(f"Sorry, there was an error: {error}")

if __name__ == "__main__":
  main()