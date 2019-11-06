import os

from src import markov_text_generator

if __name__ == "__main__":
    curr_path = os.path.abspath(os.path.dirname(__file__))
    input_filename = os.path.join(curr_path, 'data/input.jsonl')
    output_filename = os.path.join(curr_path, 'data/output1.txt')
    text_body = markov_text_generator.create_text_body(input_filename)
    text_model = markov_text_generator.create_markov_chain(text_body, 1)
    markov_text_generator.generate_text(output_filename, text_model, 140)
