class ReadmeGenerator:
  def __init__(self, answers):
    self.answers = answers
    self.readme_content = ""
    
  def generate_content(self):
    # title and description
    content = f"# {self.answers["title"]}\n\n"
    content += f"**Description:** {self.answers["description"]}\n\n"
    
    # install section
    content += "## Installation\n\n"
    content += f"{self.answers["installation"]}\n\n"
    
    # usage section
    content += "## Usage\n\n"
    content += f"{self.answers["usage"]}\n\n"
    
    # license info
    content += "## License\n\n"
    content += f"This project is licensed under the: {self.answers["license"]}\n\n"
    
    # author and contact details
    content += "## Contact\n\n"
    content += f"- **Author:** {self.answers['author']}\n"
    content += f"- **Email:** {self.answers['email']}\n"
    content += f"- **LinkedIn:** [→ Click here to connect with me!]({self.answers['linkedin']})\n\n"
    
    content += "<br />"
    content += '<hr style="height:3px; background-color:#b2b2b2; border:none;">'
    content += "<br />\n\n"
    
    # my note message
    content += f">_“This project was developed as part of the Step8Up Full Stack Web Development Bootcamp's Week 6 coding challenge.”_\n\n"
    
    self.readme_content = content
    return content
  
  def save_file(self, file_name="README.md"):
    try:
      with open(file_name, "w", encoding="utf-8") as file:
        file.write(self.readme_content)
      return True
    except Exception as error:
      print(f"Error saving file: {error}.")
      return False