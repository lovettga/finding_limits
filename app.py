import streamlit as st
import pandas as pd
import numpy as np
from sympy import simplify, symbols, limit, sqrt

#############################################
# Generate the limit problem and solution
# randomize c and b based on a
a = np.random.randint(low=1, high=20)

# utilized AI Generated code to generate a limit problem
# such that: (x+1) / (x^2+cx+b) = 0 at x=-1
# limit must simplify to 1/a
# c and b were derived and generated as follows:
c = a**2 + 2
b = a**2 + 1

# this works to solve the limit using the generated c and b values
x = symbols('x')
expr = sqrt(  (x+1) / ( (x)**2 + c*x + b ) )
result = limit(expr, x, -1)
#############################################

# page header
st.header('Finding Limits')

# create string to display limit using randomized variables in LaTeX
lim_disp = r'\lim_{x \to {-1}} \sqrt{ \dfrac{x+1}{x^{2}+%sx+%s} }' % (c, b)

# create main container for the question prompt and answer box
main_container = st.container(border=True, horizontal_alignment="center")
main_container.markdown("Solve the limit:", text_alignment="center")
main_container.latex(lim_disp, width="content")

#create 2 columns (centered on the screen) for "your answer:" and input box
left, right = main_container.columns(2, border=True, vertical_alignment="bottom")
left.markdown("Your answer: ", text_alignment="right")

# TODO: update to str_input in order to accept fractions as values
#from sympy import nsimplify
#approx_dec = 0.333333333333
#clean_frac = nsimplify(approx_dec) # Returns: 1/3
number = right.number_input(label="", value=None, placeholder="Ex: 3.4", width=220)

# TESTING: displays correct answer for the limit
st.write(f"The limit is: {result}")

st.write("Provided answer: ", number)

