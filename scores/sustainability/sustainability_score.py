# This script will take a data input of product ingredients and output a sustainability score

# The score is based on the criteria described in the notion document "Sustainability Score"

# We will start by importing relevant packages and sample dataset
import pandas as pd
import numpy as np
from . import gpt
import re


def extract_numbers(string):
    # Remove all non-numeric characters from the string using a regular expression
    string = re.sub(r'\D', '', string)

    # Convert the resulting string of numbers to a list of integers
    numbers = [int(digit) for digit in string]

    return numbers


# Using the data, we will create a function that will take in a product name and output a sustainability score
def ai_sustainability_score(prod_name):
    # We need openai to classify the ingredients into categories that match the waste disposal guide
    # We will use the openai api to do this
    x = gpt.get_response(
        "Please rate the sustainability of " + prod_name + " on a scale of 1 to 10, with 1 being not sustainable at all and 10 being extremely sustainable. Please take into consideration factors such as the materials used, the manufacturing process, the products lifespan, and its impact on the environment.")
    # Extract the numbers from the response and return the average
    # First we will delete everything that is not a number
    scores = extract_numbers(x)
    result = sum(scores) * 2
    return x, scores, result

# print(ai_sustainability_score("Coca Cola Bottle"))
