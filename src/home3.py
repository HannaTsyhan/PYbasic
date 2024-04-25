import re

def camel_to_snake(text):
    # Use regular expression to find all capital letters
    s1 = re.sub('(.)([A-Z][a-z]+)', r'\1_\2', text)

    # Convert the remaining capital letters to lowercase
    return re.sub('([a-z0-9])([A-Z])', r'\1_\2', s1).lower()

# Example
camel_case_text = "CamelCaseExample"
snake_case_text = camel_to_snake(camel_case_text)
print(snake_case_text)  # Output: camel_case_example
