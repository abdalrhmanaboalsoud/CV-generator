def read_template(file_path):
    """Reads the CV template file and returns its content."""
    try:
        with open(file_path, 'r') as template_file:
            return template_file.read()
    except FileNotFoundError:
        print("Template file not found. Please check the file path.")
        return None

def parse_template(template_content, user_info):
    """Replaces placeholders in the template with user information."""
    try:
        # Split the skills and languages input into separate lists
        skills_list = user_info['skills'].split(',')
        language_levels = user_info['languages'].split(',')
        arabic_level = language_levels[0].strip() if len(language_levels) > 0 else ""
        english_level = language_levels[1].strip() if len(language_levels) > 1 else ""

        # Replace placeholders with user information
        return template_content.format(
            Name=user_info['name'],
            phone_number=user_info['phone_number'],
            email=user_info['email'],
            city=user_info['city'],
            university_name=user_info['university_name'],
            major=user_info['major'],
            graduation_date=user_info['graduation_date'],
            company_name=user_info['company_name'],
            job_title=user_info['job_title'],
            your_responsibilities=user_info['responsibilities'],
            skill_01=skills_list[0].strip() if len(skills_list) > 0 else "",
            skill_02=skills_list[1].strip() if len(skills_list) > 1 else "",
            skill_03=skills_list[2].strip() if len(skills_list) > 2 else "",
            skill_04=skills_list[3].strip() if len(skills_list) > 3 else "",
            Arabic_language_level=arabic_level,
            English_language_level=english_level
        )
    except KeyError as e:
        print(f"Error: Placeholder {e} not found in the template.")
        return None

def merge(file_path, modified_content):
    """Writes the modified content to a file and prints it."""
    if modified_content:
        try:
            with open(file_path, 'w') as cv_file:
                cv_file.write(modified_content)
            print("CV has been generated with your information.")
            with open(file_path, 'r') as cv:
                print(cv.read())
        except IOError:
            print("Could not write to file. Please check the file path and permissions.")

# Main program execution
print("Welcome to the CV Generator!")
print("This tool helps you create a CV from the command line.")
print("Please provide the following information to generate your CV:")

# Collect user information
user_info = {
    'name': input("Enter your name: "),
    'phone_number': input("Enter your phone number: "),
    'email': input("Enter your email: "),
    'city': input("Enter your city: "),
    'university_name': input("Enter your university name: "),
    'major': input("Enter your major: "),
    'graduation_date': input("Enter your graduation date: "),
    'company_name': input("Enter your company name: "),
    'job_title': input("Enter your job title: "),
    'responsibilities': input("Enter your responsibilities: "),
    'skills': input("Enter your top 4 skills (comma-separated): "),
    'languages': input("Enter your Arabic and English language levels (comma-separated): ")
}


template_content = read_template('assets/cv_template.txt')
if template_content:
    modified_content = parse_template(template_content, user_info)
    merge('assets/my_cv.txt', modified_content)
