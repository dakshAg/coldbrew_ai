# This script will set up the OpenAI API and get the response from gpt 3

# Make a function to get the response from gpt 3
def get_response(temp, text_prompt):
    # Dependencies
    import openai 
    # Import secret.py from the parent directory
    import sys
    from . import secret
    # Set up OpenAI API credentials# Set up OpenAI API credentials
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
    # Print the generated continuation
    return result