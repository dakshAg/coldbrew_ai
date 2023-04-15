# This script will get all of the metrics for a given product
import gpt
import re


# def extract_numbers(string):
#     """This takes a string and extracts the numbers from it

#     Args:
#         string (str): The string that will be searched for numbers

#     Returns:
#         list: The list of numbers that were extracted from the string
#     """
#     # Remove all non-numeric characters from the string using a regular expression
#     string = re.sub(r'\D', '', string)
#     # Convert the resulting string of numbers to a list of integers
#     numbers = [int(digit) for digit in string]
#     return numbers


# Given the ingredients and location, we need to get gpt to give us a waste disposal guide
def ai_disposal(prod_name, lga_url):
    """Takes a product name and lga url and returns the waste disposal guide

    Args:
        prod_name (str): The product name you are interested in
        lga_url (str): String of the url to the waste disposal guide for the lga

    Returns:
        str: Response from gpt3
    """
    disposal_prompt = "First classify this proudct (" + prod_name + ") into a general category on the following website then use information from this site to tell me what I should do with it (disposal guide) in 100 words: " + lga_url + "\n\nDisposal guide: [fill in the blank]"
    return gpt.get_response(0.5, disposal_prompt)


# Now we need a function for the carbon and water footprint
def ai_cf_wf(prod_name):
    """This takes a product name and uses gpt3 to approximate carbon and water footprint

    Args:
        prod_name (str): The name of the product you are interested in

    Returns:
        str: The response for carbon footprint and water footprint
    """
    cf_prompt = "Instruction 1: Approximate carbon footprint of this product (in kgCO2e): Coca-Cola Classic Soft Drink Can 375mL or similar product.\nResponse 1: 0.17 kgCO2e\n\nInstruction 2: Approximate carbon footprint of this product (in kgCO2e): " + prod_name + " or similar product.\nResponse 2: [fill the blank]."
    wf_prompt = "Instruction 1: Approximate water footprint of this product (in L): Coca-Cola Classic Soft Drink Can 375mL or similar product.\nResponse 1: 170 L\n\nInstruction 2: Approximate water footprint of this product (in L): " + prod_name + " or similar product.\nResponse 2: [fill the blank]."
    response_carbon = gpt.get_response(0.2, cf_prompt)
    response_water = gpt.get_response(0.2, wf_prompt)

    return response_carbon, response_water
    # Extract the numbers from the response
    # score_carbon = extract_numbers(response_carbon)
    # score_water = extract_numbers(response_water)
    # return score_carbon, score_water


def final_report(prod_name, url):
    """The combination of ai_disposal and ai_cf_wf

    Args:
        prod_name (str): The product name you are interested in
        url (str): URL of the waste disposal guide for the lga

    Returns:
        str: The response from gpt3 for waste disposal and the carbon and water footprint
    """
    return {
        'disposal': ai_disposal(prod_name, url),
        'cf_wf': ai_cf_wf(prod_name)
    }
