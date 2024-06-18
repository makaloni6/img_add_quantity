import pickle
import pandas as pd
import re 


with open('pickle/title.pickle', 'rb') as f:
    data = pickle.load(f)

c_pattern = r'\d+(?:ml|l|g)'
q_pattern = r'\d+(?:個|本|袋)'
c_pattern = r'[0-9.]+(?:ml|l|g|ｍｌ|リットル|g)'

temp_dict = {}
for asin, title in data.items():
    content = re.findall(c_pattern, title, re.I)
    q = re.findall(q_pattern, title, re.I)
    if len(content) > 0 and len(q) > 0:
        temp_dict[asin] = [content[0], q[0]]

df = pd.DataFrame(temp_dict.values(), index=temp_dict.keys())
df.to_csv('title.csv')

with open('pickle/contents.pickle', 'wb') as f:
    pickle.dump(temp_dict, f)
