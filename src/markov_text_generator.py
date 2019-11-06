import json
import markovify


def create_text_body(input_filename: str, text_key: str = "full_text") -> list:
    """
    Takes data from a .JSONL file
    :param input_filename: file path + extension
    :param text_key: key to look for in json data
    :return: list of sentences
    """
    print(f"Creating body from file {input_filename}")
    text_body = []
    with open(input_filename, "r") as input_file:
        for text_object in input_file:
            text_json = json.loads(text_object)
            body = text_json.get(text_key, "")
            if "\n" in body:
                body.replace("\n", " ")
            text_body.append(body)
    print("Body creation complete")
    return text_body


def create_markov_chain(text_body: list, state_size: int = 2) -> markovify.Text:
    """
    Creates the markov chain based on a text body (corpus)
    :param text_body: list of sentences
    :param state_size: Number of words in the state
    :return: Markov Chain object
    """
    print("Creating markov chain")
    markov_chain = markovify.Text(text_body, state_size=state_size)
    print("Markov chain creation complete")
    return markov_chain


def generate_text(
        output_filename: str,
        markov_chain: markovify.Text,
        sentence_amount: int = 100,
        sentence_length_max: int = 280,
        sentence_length_min: int = 20,
) -> None:
    """
    Generates text using a Markov Chain Model and writes it to a file
    :param output_filename: file path + extension
    :param markov_chain: Markov Chain Model
    :param sentence_amount: Amount of sentences to generate
    :param sentence_length_max: Max sentence character length
    :param sentence_length_min: Min sentence character length
    :return: None
    """
    print("Creating text from model")
    
    def create_sentence() -> str:
        text = markov_chain.make_short_sentence(
            sentence_length_max,
            sentence_length_min
        )
        print(f"Text: {text}")
        return text
    
    # Important: encoding=utf-8, otherwise it will break with emoji characters
    with open(output_filename, "w", encoding="utf-8") as output_file:
        for i in range(sentence_amount):
            sentence = create_sentence()
            if sentence is not None:
                try:
                    output_file.write(f"{sentence}\n")
                except Exception as e:
                    print(f"Exception {e}:{sentence}")
    print("Text creation complete")
