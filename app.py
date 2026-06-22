import streamlit as st
import pandas as pd
import numpy as np
from sympy import nsimplify, symbols, limit, sqrt

#############################################
# Generate the limit problem and calculate solution
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

# store values in session state
st.session_state.a = a
st.session_state.c = c
st.session_state.b = b
st.session_state.result = a
#############################################
# Handle the callback for the answer box
def handle_text_change():
    # Access the text using the widget's unique key
    current_text = st.session_state.answer_area
    
    # DO SOMETHING WITH THE ANSWER, LIKE DETERMINE IF IT IS CORRECT OR NOT :)
    # convert provided answer into a fraction and them compare against correct answer
    current_answer = nsimplify(current_text)
    answer = False
    if current_answer == st.session_state.result:
        answer = True
    
    # Store results back in session state to display in the UI
    st.session_state.answer = answer

# initialize session state variables if they do not exist
if "answer" not in st.session_state:
    st.session_state.answer = None
#############################################
# Create display for question prompt
# page header
st.header('Finding Limits')

# create string to display limit using randomized variables in LaTeX
lim_disp = r'\lim_{x \to {-1}} \sqrt{ \dfrac{x+1}{x^{2}+%sx+%s} }' % (c, b)

# create main container for the question prompt and answer box
main_container = st.container(border=True, horizontal_alignment="center")
main_container.markdown("## Solve the limit:", text_alignment="center")
main_container.latex(lim_disp, width="content")

#create 2 columns (centered on the screen) for "your answer:" and input box
left, right = main_container.columns(2, border=True, vertical_alignment="bottom")
left.markdown("### Your answer: ", text_alignment="right")

# TODO: update to str_input in order to accept fractions as values
#from sympy import nsimplify
#approx_dec = 0.333333333333
#clean_frac = nsimplify(approx_dec) # Returns: 1/3
# number = right.number_input(label="", value=None, placeholder="Ex: 3.4", width=220)
number = right.text_area(
    label="", value=None, placeholder="Ex: 3.4", width=300, height="content", 
    max_chars=10, key="answer_area", on_change=handle_text_change)

# TESTING: displays correct answer for the limit
st.write(f"The limit is: {result}")

# TODO: the page resets when you click outside of the box to "submit" the answer
# figure out how to display the correct/incorrect?
st.write("Provided answer: ", number)

#st.write(f"**Your answer (updated on change):** {st.session_state.answer}")
if st.session_state.answer is None:
    # display nothing
elif st.session_state.answer:
    st.write("Provided answer: is correct ")
else:
    st.write("Provided answer: is correct ")
###############################################

###########################
# TESTING AI Code
import streamlit as st

# 1. Initialize the value in session state so it doesn't get re-initialized on every click
if 'my_value' not in st.session_state:
    st.session_state.my_value = "Default Value"

# 2. Define a callback function to update the session state
def update_value():
    st.session_state.my_value = st.session_state.widget_key

# 3. Widget with matching key and callback
st.text_input(
    "Enter text:", 
    value=st.session_state.my_value, 
    key="widget_key", 
    on_change=update_value
)

st.write(f"Persisted value: {st.session_state.my_value}")





#############################

