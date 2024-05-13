import pytest
from cv_generator.cv_generator import read_template, parse_template, merge


def test_read_template_returns_stripped_string():
    actual = read_template(
        "/home/abdalrhman/mid-advanced-projects/CV-generator/assets/personal_summary.txt"
    )
    expected = "I'm {Name} and I have Bachelor's degree in {major} and Currently working as a {job_title}  -  at {company_name}."
    assert actual == expected


# @pytest.mark.skip("pending")
def test_parse_template():
    template = "I'm {Name} and I have Bachelor's degree in {major} and Currently working as a {job_title}  -  at {company_name}."
    user_info = {
        "name": "John Doe",
        "major": "Computer Science",
        "job_title": "Software Engineer",
        "company_name": "Tech Corp",
    }
    actual = parse_template(template, user_info)
    expected = "I'm John Doe and I have Bachelor's degree in Computer Science and Currently working as a Software Engineer  -  at Tech Corp."
    assert actual == expected


# Corrected test_merge
def test_merge():
    content = "I'm {} and I have Bachelor's degree in {} and Currently working as a {}  -  at {}."
    formatted_content = content.format("john", "CS", "developer", "ABCIT")
    file_path = (
        "assets/personal_summary.txt"  # Make sure this is a valid path where you have write permissions
    )
    merge(file_path, formatted_content)
    with open(file_path, "r") as f:
        actual = f.read()
    expected = "I'm john and I have Bachelor's degree in CS and Currently working as a developer  -  at ABCIT."
    assert actual == expected


# Corrected test_read_template_raises_exception_with_bad_path
def test_read_template_raises_exception_with_bad_path():
    with pytest.raises(FileNotFoundError):
        read_template("non_existent_file.txt")
