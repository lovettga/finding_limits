import streamlit as st
import pandas as pd
import numpy as np
from sympy import nsimplify, symbols, limit, sqrt

#############################################
# Generate the limit problem and calculate solution
def generate_limit():
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

    return a, b, c, result
#############################################
# Handle the callback for the answer box
def handle_text_change():
    # Access the text using the widget's unique key
    current_text = st.session_state.answer_area
    
    # DO SOMETHING WITH THE ANSWER, LIKE DETERMINE IF IT IS CORRECT OR NOT :)
    # convert provided answer into a fraction and them compare against correct answer
    # prevent error edge case if submit is pressed with no answer input
    if current_text is not None:
        current_answer = nsimplify(current_text)
    else:
        return
    answer = False
    if current_answer == st.session_state.result:
        answer = True
    
    # Store results back in session state to display in the UI
    st.session_state.answer = answer
    st.session_state.curr_answer = current_answer
#############################################
# Create display for question prompt

# initialize values and store values in session state
if 'result' not in st.session_state:
    limit_info = generate_limit()
    st.session_state.a = limit_info[0]
    st.session_state.b = limit_info[1]
    st.session_state.c = limit_info[2]
    st.session_state.result = limit_info[3]
    st.session_state.answer = None
    st.session_state.curr_answer = None

# page header
st.header('Finding Limits')

# create string to display limit using randomized variables in LaTeX
lim_disp = r'\lim_{x \to {-1}} \sqrt{ \dfrac{x+1}{x^{2}+%sx+%s} }' % (st.session_state.c, st.session_state.b)

# create main container for the question prompt and answer box
main_container = st.container(border=True, horizontal_alignment="center")
main_container.markdown("## Solve the limit:", text_alignment="center")
main_container.latex(lim_disp, width="content")

# create 2 columns (centered on the screen) for "your answer:" and input box
left, right = main_container.columns(2, vertical_alignment="center")
left.markdown("### Your answer: ", text_alignment="right")

# create 2 columns within the right column above to contain the input field and the submit button
answer_box, submit_btn = right.columns([8,4]) 
number = answer_box.text_input(
    label="", label_visibility='collapsed',
    value=None, placeholder="Ex: 3.4", width=220, max_chars=25, 
    key="answer_area", on_change=handle_text_change)

if submit_btn.button("Submit"):
    handle_text_change()

#number = right.text_input(
#    label="", label_visibility='collapsed',
#    value=None, placeholder="Ex: 3.4", width=220, max_chars=15, 
#    key="answer_area", on_change=handle_text_change)
#if right.button("Submit"):
#    handle_text_change()

# TESTING: displays correct answer for the limit
st.write(f"The limit is: {st.session_state.result}")

# display answer correctness
if st.session_state.answer is None:
    st.markdown("")
elif st.session_state.answer:
    st.markdown(f"Your Answer: ${st.session_state.curr_answer}$")
    st.markdown(f":green[:material/check: Correct]. The limit is {st.session_state.result}.")
else:
    st.markdown(f"Your Answer: ${st.session_state.curr_answer}$")
    st.markdown(f":red[:material/close: Incorrect]. The limit is {st.session_state.result}.")
###############################################

###########################
# TESTING AI Code

#############################

