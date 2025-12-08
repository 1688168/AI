from random import randint
from time import sleep

import streamlit as st


def read_sensor():
    sleep(0.2)
    return randint(1, 10)

place = st.empty()

data = []
for i in range(20):
    sensor = read_sensor()
    data.append(sensor)
    # place.write(f'Sensor data: {sensor}')
    place.line_chart(data)

place.write('Done!')
