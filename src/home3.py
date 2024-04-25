def main():
    print('Hello, World!')


if __name__ == '__main__':
    main()

import re

def camel_to_snake(text):
    # Use regular expression to find all capital letters
    s1 = re.sub('(.)([A-Z][a-z]+)', r'\1_\2', text)

    # Convert the remaining capital letters to lowercase
    return re.sub('([a-z0-9])([A-Z])', r'\1_\2', s1).lower()

# Example
camel_case_text = "  tHis iz your homeWork, copy these Text to variable. You NEED TO normalize it fROM letter CASEs point oF View. also, create one MORE senTENCE witH LAST WoRDS of each existING SENtence and add it to the END OF this Paragraph."
snake_case_text = camel_to_snake(camel_case_text)
print(snake_case_text)  # Output: camel_case_example
