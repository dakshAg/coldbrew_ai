# This script will get all of the metrics for a given product
import gpt
import re

def extract_numbers(string):
    """This takes a string and extracts the numbers from it

    Args:
        string (str): The string that will be searched for numbers

    Returns:
        list: The list of numbers that were extracted from the string
    """
    # Remove all non-numeric characters from the string using a regular expression
    string = re.sub(r'\D', '', string)
    # Convert the resulting string of numbers to a list of integers
    numbers = [int(digit) for digit in string]
    return numbers


# Given the ingredients and location, we need to get gpt to give us a waste disposal guide
def ai_disposal(prod_name, lga_url):
    """Takes a product name and lga url and returns the waste disposal guide

    Args:
        prod_name (str): The product name you are interested in
        lga_url (str): String of the url to the waste disposal guide for the lga

    Returns:
        str: Response from gpt3
    """
    return gpt.get_response(0.5,
                                "First classify this" + prod_name + "into a general category on the following website then use information from this site to tell me what I should do with it:" + lga_url)


# Now we need a function for the carbon and water footprint
def ai_cf_wf(prod_name):
    """This takes a product name and uses gpt3 to approximate carbon and water footprint

    Args:
        prod_name (str): The name of the product you are interested in

    Returns:
        str: The response for carbon footprint and water footprint
    """
    response_carbon = gpt.get_response(0.2,
                                       "Please rate the sustainability of " + prod_name + " on a scale of 1 to 10, with 1 being not sustainable at all and 10 being extremely sustainable. Please take into consideration factors such as the materials used, the manufacturing process, the products lifespan, and its impact on the environment.")
    response_water = gpt.get_response(0.2,
                                      "Please rate the sustainability of " + prod_name + " on a scale of 1 to 10, with 1 being not sustainable at all and 10 being extremely sustainable. Please take into consideration factors such as the materials used, the manufacturing process, the products lifespan, and its impact on the environment.")
    # Extract the numbers from the response
    score_carbon = extract_numbers(response_carbon)
    score_water = extract_numbers(response_water)
    return score_carbon, score_water


def final_report(prod_name, url):
    """The combination of ai_disposal and ai_cf_wf

    Args:
        prod_name (str): The product name you are interested in
        url (str): URL of the waste disposal guide for the lga

    Returns:
        str: The response from gpt3 for waste disposal and the carbon and water footprint
    """
    return ai_disposal(prod_name, url), ai_cf_wf(prod_name)
