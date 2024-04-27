import re

if __name__ == '__main__':

    initial_text = """
homEwork:
  tHis iz your homeWork, copy these Text to variable.

  You NEED TO normalize it fROM letter CASEs point oF View. also, create one MORE senTENCE witH 
LAST WoRDS of each existING SENtence and add it to the END OF this Paragraph. 

  it iZ misspeLLing here. fix“iZ” with correct “is”, but ONLY when it Iz a mistAKE.

  last iz TO calculate nuMber OF Whitespace characteRS in this Tex. caREFULL, not only Spaces, 
but ALL whitespaces. I got 87.
"""

lowercase_text = initial_text.lower()  # Normalize letter cases to lower case
paragraphs: list = lowercase_text.split("\n\n")   # Split the text into paragraphs
capitalized_paragraphs = []
joined_text = []
last_words = []

for paragraph in paragraphs:  # Process paragraphs
    capitalized_paragraph = paragraph.lstrip().capitalize().strip('\n')  # Capitalize the first letters in paragraphs
    # print(capitalized_paragraph)
    sentences = capitalized_paragraph.split(".")  # Split the paragraphs into sentences
    sentences.pop()
    # print(sentences)
    capitalized_sentences = []

    for sentence in sentences:  # Process sentences
        capitalized_sentence = sentence.strip().capitalize() + ". "  # Capitalize sentences
        words = sentence.split(" ")  # Get the last words
        last_words.append(words[-1])
        capitalized_sentences.append(capitalized_sentence)

    joined_paragraph = "  " + "".join(f"{row}" for row in capitalized_sentences).rstrip()   # Join the sentences in paragraphs
    capitalized_paragraphs.append(joined_paragraph)


last_sentence = " ".join(last_words).capitalize() + "."  # Join last words to create the  sentence and add it the text
capitalized_paragraphs[1] += " " + last_sentence

joined_text = "".join(f"{parag}\n\n" for parag in capitalized_paragraphs)   # Join the paragraphs in text


corrected_text = joined_text.replace(" iz ", " is ")   # Correct error iz -> is
print(corrected_text)

whitespace_pattern = re.compile(r'\s+')  # Calculate number of whitespaces
whitespaces_count_corrected = len(whitespace_pattern.findall(corrected_text))
print(whitespaces_count_corrected)
