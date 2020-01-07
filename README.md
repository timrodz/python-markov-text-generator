# Markov Text Generator

Python based text generator that uses the [markovify](https://github.com/jsvine/markovify) python library.

Example data can be found in `/data/input.jsonl`. In this case, the data has been obtained from Twitter by using either [Tweepy](https://www.tweepy.org/) or [twarc](https://github.com/DocNow/twarc) - All we care about is how the text corpus (body) is formatted. You're more than welcome to have a look at my [Python Twitter Scraper using Tweepy](https://github.com/timrodz/python-twitter-scraper-tweepy) for a basic implementation

## How-to

1. Load an _input_ file (`.jsonl`) file with (ideally) more than 1000 sentences. More sentences help build stronger texts.
2. Run `create_text_body` and specify the `text_key` to look for in your input file.
3. Run `create_markov_chain` with your resulting text_body and pass in the state_size.
4. `generate_text` will create a specific amount of  sentences by a specified minimum and maximum length of characters. An output file is required, which is where we'll save our newly created sentences.

### Quick links

- What are [.jsonl](http://jsonlines.org/) files?
- Markov chains [visually explained](http://setosa.io/ev/markov-chains/).
