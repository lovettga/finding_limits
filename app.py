import streamlit as st
import pandas as pd
import numpy as np

st.header('Finding Limits')


container = st.container(border=True, horizontal_alignment="center")
container.markdown("Solve the limit:", text_alignment="center")
container.write("x**2 + 3*x - 1/2")
number = container.number_input(
    "Your answer", value=None, placeholder="Ex: 300", width="200"
)
st.write("This is outside the container")

