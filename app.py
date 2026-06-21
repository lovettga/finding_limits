import streamlit as st
import pandas as pd
import numpy as np
from sympy import simplify, symbols, limit, sqrt

########################################
# AI Generated code to generate a limit problem

#def generate_limit_problem(a_value):

    #Generates coefficients c and d for f(x) = sqrt((x+1)/(x^2+cx+d))
    #such that the limit as x approaches -1 evaluates exactly to 1/a.
    
#    if a_value <= 0:
#        raise ValueError("The value of 'a' must be greater than 0 for a valid real square root output.")
        
#    x = sp.Symbol('x')
    
    # Calculate symbolic coefficients based on derived equations
#    c = a_value**2 + 2
#    d = a_value**2 + 1
    
    # Construct the mathematical function
#    numerator = x + 1
#    denominator = x**2 + c*x + d
#    f_x = sp.sqrt(numerator / denominator)
    
    # Evaluate the target limit using SymPy's limit logic
#    computed_limit = sp.limit(f_x, x, -1)

#######################################

# randomize c and b based on a
a = np.random.randint(low=1, high=20)

c = a**2 + 2
b = a**2 + 1

# such that: (x+1) / (x^2+cx+b) = 0 at x=-1
# limit must simplify to 1/a

# this works to solve the limit
x = symbols('x')
expr = sqrt(  (x+1) / ( (x)**2 + c*x + b ) )
result = limit(expr, x, -1)


# page header
st.header('Finding Limits')

# create string to display limit using randomized variables
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

