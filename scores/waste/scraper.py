import requests
from bs4 import BeautifulSoup
import pandas as pd
import re
import numpy as np
import test as test

url = "https://www.melbourne.vic.gov.au/residents/waste-recycling/Pages/a-z-waste-disposal.aspx"
response = requests.get(url)
soup = BeautifulSoup(response.content, 'html.parser')

accordion_container = soup.find('div', {'class': 'accordionContainer'})

text_data = []
for accordion_item in accordion_container.find_all('div', {'class': 'accordionQuestionAdhoc'}):
    result = accordion_item.find('div', {'class': 'accordionAnswer'}).text.strip()
    # Remove every instance of "/xa0" from the string
    result = result.replace('\xa0', ' ')
    # Remove every space before an uppercase letter
    result = test.split_string(result)
    print(result)
    # Split the text every time there is a character before an uppercase letter
    split_text =re.findall('.+?(?=[A-Z])|[A-Z][^A-Z]*', result)

    text_data.append(split_text)
print(np.shape(text_data))
print(text_data[0])
# #Turn the list into a pandas dataframe
# df = pd.DataFrame(text_data, columns=['text'])
# df.to_csv('scrape_data.csv', index=False)