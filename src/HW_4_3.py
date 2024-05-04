
import re


def get_initail_text() -> str:
    return """
homEwork:
  tHis iz your homeWork, copy these Text to variable.

  You NEED TO normalize it fROM letter CASEs point oF View. also, create one MORE senTENCE witH 
LAST WoRDS of each existING SENtence and add it to the END OF this Paragraph. 

  it iZ misspeLLing here. fix“iZ” with correct “is”, but ONLY when it Iz a mistAKE.

  last iz TO calculate nuMber OF Whitespace characteRS in this Tex. caREFULL, not only Spaces, 
but ALL whitespaces. I got 87.
"""


def to_lower_case(initial_text: str) -> str:
    """
    takes in text
    returns text in lower case
    """
    lowercase_text = initial_text.lower()
    return (lowercase_text)


def split_text(text: str, delimiter: str) -> list:
    """
        takes in text
        returns text split with delimiter
        """
    return text.split(delimiter)


def normalize_text(raw_text: str) -> str:
    """
        takes in text, splits it into paragraphs and sentences, capitalizes them and add additional sentence
        returns normalized text
        """
    capitalized_paragraphs = []
    last_words = []
    paragraphs = split_text(raw_text, "\n\n")
    for paragraph in paragraphs:  # Process paragraphs
        sentences = split_text(paragraph, ".")
        sentences.pop()
        # print(sentences)
        capitalized_sentences = []
        for sentence in sentences:  # Process sentences
            capitalized_sentence = sentence.strip().capitalize() + ". "
            words = split_text(sentence, " ")
            last_words.append(words[-1])
            capitalized_sentences.append(capitalized_sentence)
        joined_paragraph = "  " + "".join(
            f"{row}" for row in capitalized_sentences).rstrip()
        capitalized_paragraphs.append(joined_paragraph)

    last_sentence = " ".join(
        last_words).capitalize() + "."
    capitalized_paragraphs[1] += " " + last_sentence

    return "".join(f"{parag}\n\n" for parag in capitalized_paragraphs)


def correct_text (text: str) -> str:
    """
        takes in text,
        returns text with corrected spelling mistakes
        """
    return text.replace(" iz ", " is ")

def count_whitespaces (text: str) -> int:
    """
        takes in text, counts whitespaces
        returns number of whitespaces
        """
    whitespace_pattern = re.compile(r'\s+')
    return len(whitespace_pattern.findall(text))


if __name__ == '__main__':
    initial_text = get_initail_text()
    lower_init_text = to_lower_case(initial_text)
    normalized_text = normalize_text(lower_init_text)
    corrected_text = correct_text(normalized_text)
    print(corrected_text)
    whitespaces_counted = count_whitespaces(corrected_text)
    print(whitespaces_counted)
