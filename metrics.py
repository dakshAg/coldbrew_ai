# This script will take a data input of product ingredients and output a waste guide
# The score is based on the criteria described in the notion document "Waste Disposal Guide"
# We will start by importing relevant packages and sample dataset
import gpt
import re

def extract_numbers(string):
    # Remove all non-numeric characters from the string using a regular expression
    string = re.sub(r'\D', '', string)
    # Convert the resulting string of numbers to a list of integers
    numbers = [int(digit) for digit in string]
    return numbers

# Given the ingredients and location, we need to get gpt to give us a waste disposal guide
def ai_disposal(prod_name, lga_url):
    # We need openai to classift the ingredients into categories that match the waste disposal guide
    # We will use the openai api to do this
    response = gpt.get_response(0.5,
        "First classify this" + prod_name + "into a general category on the following website then use information from this site to tell me what I should do with it:" + lga_url)
    return response

# Using the data, we will create a function that will take in a product name and output a sustainability score
def ai_cf_wf(prod_name):
    # We need openai to classify the ingredients into categories that match the waste disposal guide
    # We will use the openai api to do this
    response_carbon = gpt.get_response(0.2,
        "Please rate the sustainability of " + prod_name + " on a scale of 1 to 10, with 1 being not sustainable at all and 10 being extremely sustainable. Please take into consideration factors such as the materials used, the manufacturing process, the products lifespan, and its impact on the environment.")
    response_water = gpt.get_response(0.2,
        "Please rate the sustainability of " + prod_name + " on a scale of 1 to 10, with 1 being not sustainable at all and 10 being extremely sustainable. Please take into consideration factors such as the materials used, the manufacturing process, the products lifespan, and its impact on the environment.")
    # Extract the numbers from the response
    score_carbon = extract_numbers(response_carbon)
    score_water = extract_numbers(response_water)
    return score_carbon, score_water