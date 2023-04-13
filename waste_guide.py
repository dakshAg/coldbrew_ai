# This script will take a data input of product ingredients and output a waste guide

# The score is based on the criteria described in the notion document "Waste Disposal Guide"

# We will start by importing relevant packages and sample dataset
import pandas as pd
import numpy as np
import openai
import requests as r
from bs4 import BeautifulSoup
import scraper

# The data we will be looking for contains product and manufacturer information and country of origin.
data = pd.read_csv("data.csv")
# Using the data, we will create a function that will take in a product name and output a sustainability score
def waste_disposal(data, location):
    #Pull the ingredients from the data as well as the user's location
    ingredients = data["ingredients"]
    lga = location["lga"]
    return ingredients, lga

# Given the ingredients and location, we need to use a web scraper to find the relevant waste disposal information
def web_scraper(ingredients, lga):
    # We need openai to classift the ingredients into categories that match the waste disposal guide
    # We will use the openai api to do this
    
    
    
# Now we just need a main function that will run the sustainability score function and save the score to a json file.
def main(data):
    carbon = carbon_calc(data)
    water = water_calc(data)
    recyclability = recyclability_calc(data)
    energy = energy_calc(data)
    sourcing = sourcing_calc(data)
    # Then we need to run the sustainability score function
    score = sustainability_score(carbon, water, recyclability, energy, sourcing)
    return score    