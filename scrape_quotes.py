from bs4 import BeautifulSoup
import pandas as pd
import sqlalchemy
from sqlalchemy import create_engine, text
import os

print("\n===============================================================")
with open('./data/words.html', 'r') as f:
    html_source = f.read()

soup = BeautifulSoup(html_source, 'html.parser')
print(type(soup))

quote_1 = soup.find('p', {'id': "box"})
#print(quote_1)

p_tags = soup.find_all('p', {'id': "box"})
print(len(p_tags))


def parse_tags(p_tag):
    title = p_tag.strong.text.strip()
    quote = p_tag.get_text()
    #quote = p_tag.get_text("\\", strip=True)
    #quote = quote[:1000]
    return {
        'title': title,
        'wisdom': quote,
    }

print("\n===============================================================")
#print(parse_tags(p_tags[5]))

all_quotes = [parse_tags(tag) for tag in p_tags]

#for top_quote in top_quotes:
#   print(top_quote['title'])

ex_quote = all_quotes[1]
#print(ex_quote['title'])
#print(len(ex_quote['quote']))

ex_quote2 = all_quotes[10]
#print(ex_quote2['title'])
#print(len(ex_quote2['quote']))

sel_quotes = all_quotes[:100]

"""
print("\n===============================================================")
x = 0
for entry in sel_quotes:
    x += 1
    if len(entry['wisdom']) > 1000:
        sel_quotes.remove(entry)
        #entry['wisdom'] = None
        print(x, len(entry['wisdom']))
    else:
        entry['wisdom'] = entry['wisdom']

#print(x)
"""

print("\n===============================================================")
quotes_df = pd.DataFrame(sel_quotes)
print(quotes_df.head())


print("\n===============================================================")
import re

def strip_text(quote):
    output = re.sub('(.+\d+\.\d+\.\d+)', "", quote)
    output = re.sub('\n', "", output)
    return output



quotes_df.wisdom = quotes_df.wisdom.map(strip_text)
print(quotes_df.sample(25))
print(len(quotes_df))


print("\n===============================================================")
db_connection_string = os.environ['DB_CONNECTION_STRING']

engine = create_engine(db_connection_string)

print("\n===============================================================")
quotes_df.to_sql(con=engine, name='domdoms3', if_exists='append', index=False)
#quotes_df.to_sql(con=engine, name='domdoms2', if_exists='append', index=True, index_label='id')

dataBase = pd.read_sql('SELECT * FROM domdoms3', engine)
print(dataBase)