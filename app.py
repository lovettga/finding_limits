import streamlit as st
import pandas as pd
import numpy as np
from sympy import nsimplify, symbols, limit, sqrt

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
number = right.text_area(label="", value=None, placeholder="Ex: 3.4", width=220, max_chars=10)

# TESTING: displays correct answer for the limit
st.write(f"The limit is: {result}")

st.write("Provided answer: ", number)



###########################
# TESTING on_change funcitonality of string input
import streamlit as st

# 1. Define the callback function
def handle_text_change():
    # Access the text using the widget's unique key
    current_text = st.session_state.my_text_area
    
    # Calculate word count
    word_count = len(current_text.split())
    
    # Store results back in session state to display in the UI
    st.session_state.words = word_count

# 2. Initialize session state variables if they do not exist
if "words" not in st.session_state:
    st.session_state.words = 0

st.title("Streamlit Text Area Callback Example")

# 3. Create the text area with the on_change argument
text_input = st.text_area(
    label="Enter your text below:",
    placeholder="Type something here...",
    key="my_text_area",
    on_change=handle_text_change
)

# 4. Display the results updated by the callback
st.write(f"**Word Count (updated on change):** {st.session_state.words}")
st.write(f"**Current Text length:** {len(text_input)} characters")




#############################

