# Import the random module
import random

# Define the alphabet of characters to choose from
characters = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789#$%@!'


def generate_random_str(length):
    # Initialize an empty string
    string = ''
    while len(string.encode('utf-8')) < length:
        string += random.choice(characters)
    return string
