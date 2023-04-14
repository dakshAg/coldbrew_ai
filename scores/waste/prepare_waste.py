# Import the scrape_data and put it into a list
import pandas as pd
df = pd.read_csv('scrape_data.csv')

text_data = df['text'].tolist()

#Split the list at each full stop.
data = []
for item in text_data:
    data.append(item.split('.'))

# Remove the empty strings from the list
data = [x for x in data if x != ['']]

# Print the first 5 items in the list
print(data[0][:5])

# Split every time there is a character before uppercase letter without a space
import re
data2 = []
for item in data[0]:
    data2.append(re.split('(?<=[a-z])(?=[A-Z])', item))

print(data2)