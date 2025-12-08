import json
import os

import streamlit as st


if not os.path.isfile('state.json'):
    with open('state.json', 'w') as f:
        json.dump({'clicks': 0}, f)

with open('state.json') as f:
    counter = json.load(f)['clicks']

if st.button('Click me'):
    counter += 1

st.write(f'The button was clicked {counter} times')

with open('state.json', 'w') as f:
    json.dump({'clicks': counter}, f)
