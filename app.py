import streamlit as st
import pandas as pd
import numpy as np

st.header('Finding Limits')

# create string to display limit using randomized variables
lim_disp = r'\lim_{x \to %s} \sqrt{ \dfrac{x+%s}{x^{2}+%sx+%s} }' % ("1", "2", "3", "4")

main_container = st.container(border=True, horizontal_alignment="center")
main_container.markdown("Solve the limit:", text_alignment="center")
main_container.latex(lim_disp, width="content")

#create 2 columns (centered on the screen) for "your answer:" and input box
left, right = st.columns(3, vertical_alignment="bottom")

left.markdown("Your answer: ")
number = right.number_input(label="", value=0.0, placeholder="Ex: 3.4", width=220)

#input_container.markdown("Your answer: ")
#number = input_container.number_input(label="", value=0.0, placeholder="Ex: 3.4", width=220)

st.write("Provided answer: ", number)

