import streamlit as st
import pandas as pd
import numpy as np

st.title('Finding Limits')


container = st.container(border=True, horizontal_alignment="center")
container.write("Solve the limit:")
container.write("Enter Latex here to display limit")
number = container.number_input(
    "Your answer", value=None, placeholder="Type a number..."
)
st.write("This is outside the container")

