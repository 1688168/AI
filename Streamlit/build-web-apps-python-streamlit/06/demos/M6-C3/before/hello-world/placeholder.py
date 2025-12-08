from random import randint
from time import sleep

import streamlit as st


def read_sensor():
    sleep(0.2)
    return randint(1, 10)


place = st.beta_container()
st.write('Some more content')

left_column, right_column = st.beta_columns(2)

data = []
for i in range(20):
    sensor = read_sensor()
    data.append(sensor)
    # place.write(f'Sensor data: {sensor}')

place.line_chart(data)
place.write('Done!')

left_column.write('Data:')
left_column.write(data)

with right_column:
    st.write('Chart:')
    st.area_chart(data)
