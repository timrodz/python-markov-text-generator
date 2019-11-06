import os
import json
import markovify


def create_text_body(input_filename) -> list:
    print(f"Creating body from file {input_filename}")
    text_body = []
    with open(input_filename, "r") as input_file:
        for text_object in input_file:
            text_json = json.loads(text_object)
            body = text_json.get("full_text", "")
            if "\n" in text:
                body.replace("\n", " ")
            text_body.append(body)
    print("Body creation complete")
    return text_body


def create_markov_chain(text_body: list, state_size: int = 2) -> markovify.Text:
    print("Creating markov chain")
    text_model = markovify.Text(text_body, state_size=state_size)
    print("Markov chain creation complete")
    return text_model


def generate_text(output_filename: str, text_model: markovify.Text, length: int = 280) -> None:
    print("Creating text from model")

    def make_sentence(model) -> str:
        text = text_model.make_short_sentence(length)
        print(f"Text: {text}")
        return text

    # Important: encoding=utf-8, otherwise it will break with emoji characters
    with open(output_filename, "w", encoding="utf-8") as output_file:
        for i in range(100):
            sentence = make_sentence(text_model)
            if sentence is not None:
                try:
                    output_file.write(f"{sentence}\n")
                except Exception as e:
                    print(f"Exception {e}:{sentence}")
    print("Text creation complete")
