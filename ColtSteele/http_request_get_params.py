import requests
from random import randint
from colors_art import print_art

url = 'https://icanhazdadjoke.com/search'


def get_joke(topic):
    response = requests.get(
        url,
        headers={'Accept': 'application/json'},
        params={'term': topic}
    )
    return response.json()  # this returns a dictionary


def choose_joke(data):
    joke_message = f"Sorry, I don't have any jokes about {data['search_term']}"
    joke_message += "\nPlease try again."

    total = len(data['results'])
    if total > 0:
        results = data['results']
        joke = randint(0, total - 1)

        if total == 1:
            joke_message = f"I've got one joke about {data['search_term']}"
            joke_message += ". Here it is:"
        else:
            joke_message = f"I've got {total} jokes about {data['search_term']}"
            joke_message += ". Here's one:"
        joke_message += f"\n{results[joke]['joke']}"
    return joke_message


if __name__ == "__main__":
    print_art('Dad Joke 2020', 'green')
    topic = input('Let me tell you a joke! Give me a topic: ')
    data = get_joke(topic)
    print(choose_joke(data))
