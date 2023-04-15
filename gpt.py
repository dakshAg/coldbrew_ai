# This script will set up the OpenAI API and get the response from gpt 3
def get_response(temp, text_prompt):
    """This function will take a temperature and prompt and return the response from gpt 3

    Args:
        temp (str): A string that is a float from 0 to 1. It determines how random the response will be. 0 is the least random and 1 is the most random.
        text_prompt (str): The string of the prompt that will be given to gpt 3.

    Returns:
        str: The response string from gpt 3.
    """
    # Dependencies
    import openai 
    import secret
    # Set up OpenAI API credentials
    openai.api_key = secret.OPENAI_API()
    
    response = openai.Completion.create(
        engine="text-davinci-003",
        prompt=text_prompt,
        max_tokens=1000,
        n=1,
        stop=None,
        temperature=temp,
    )
    result  = response.choices[0].text
    # Print the generated response
    return result