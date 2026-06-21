import streamlit as st
import pandas as pd
import numpy as np

st.header('Finding Limits')

# create string to display limit using randomized variables
lim_disp = r'\lim_{x \to %s} \sqrt{ \dfrac{x+%s}{x^{2}+%sx+%s} }' % ("1", "2", "3", "4")

main_container = st.container(border=True, horizontal_alignment="center")
main_container.markdown("Solve the limit:", text_alignment="center")
main_container.latex(lim_disp, width="content")


input_container = st.container(border=True, horizontal=True, horizontal_alignment="distribute")
input_container.markdown("Your answer: ")
number = input_container.number_input(placeholder="Ex: 3.4", width=220)

st.write("Provided answer: ", number)

