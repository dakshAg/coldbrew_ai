import openai 
import pandas as pd
import scores.waste.secret as secret

# Import data.csv and turn it into a list
df = pd.read_csv('data.csv', header=None)
pages = df[0].tolist()
pages.pop(0)

# Set up OpenAI API credentials# Set up OpenAI API credentials
openai.api_key = secret.OPENAI_API()

# Make a function to get the response from gpt 3
def get_response(text_prompt):
    response = openai.Completion.create(
        engine="text-davinci-001",
        prompt=text_prompt,
        max_tokens=1024,
        n=1,
        stop=None,
        temperature=0.5,
    )
    result  = response.choices[0].text
    print(result)
    # Print the generated continuation
    return result

summary = []
for page in pages:
    text_prompt = "Hello World"
    summary.append(get_response(text_prompt))

# Save the summary to a csv file
df = pd.DataFrame(summary)
df.to_csv('refs.csv', index=False)