# This script will take a data input of product ingredients and output a waste guide
# The score is based on the criteria described in the notion document "Waste Disposal Guide"
# We will start by importing relevant packages and sample dataset
import pandas as pd
import numpy as np
from . import gpt
import requests as r
from bs4 import BeautifulSoup


# Given the ingredients and location, we need to get gpt to give us a waste disposal guide
def ai_disposal(prod_name, lga_url):
    # We need openai to classift the ingredients into categories that match the waste disposal guide
    # We will use the openai api to do this
    x = gpt.get_response(
        "First classify this" + prod_name + "into a general category on the following website then use information from this site to tell me what I should do with it:" + lga_url)
    return x


# Now we just need a main function that will run save the disposal guide
def main():
    name = input("Please enter the product name: ")
    url = input("Please enter the url of the LGA website: ")
    return print(ai_disposal(name, url))


# Run the main function
if __name__ == '__main__':
    main()
