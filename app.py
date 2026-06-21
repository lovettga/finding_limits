import streamlit as st
import pandas as pd
import numpy as np
import sympy as sp
#from sympy import simplify, symbols, limit, sqrt

# randomize c and b


# such that: (x+1) / (x^2+cx+b) = 0 at x=-1
# limit must simplify to 1/a




x = sp.symbols('x')
expr = sp.sqrt(  (x+1) / ( (x)**2 + 11*x + 10 ) )
result = sp.limit(expr, x, -1)


# page header
st.header('Finding Limits')

# create string to display limit using randomized variables
lim_disp = r'\lim_{x \to {-1}} \sqrt{ \dfrac{x+1}{x^{2}+%sx+%s} + 5y - 8n}' % ("1", "2")

# create main container for the question prompt and answer box
main_container = st.container(border=True, horizontal_alignment="center")
main_container.markdown("Solve the limit:", text_alignment="center")
main_container.latex(lim_disp, width="content")

#create 2 columns (centered on the screen) for "your answer:" and input box
left, right = main_container.columns(2, border=True, vertical_alignment="bottom")
left.markdown("Your answer: ", text_alignment="right")
number = right.number_input(label="", value=None, placeholder="Ex: 3.4", width=220)


st.write(f"The limit is: {result}")

st.write("Provided answer: ", number)

