import streamlit as st
import pandas as pd
import numpy as np
from sympy import nsimplify, symbols, limit, sqrt

#############################################
### FUNCTIONS ###

# Generate the radomized values for the limit problem and calculate the solution
def generate_limit():
    # c and b are dependent on randomizing a
    a = np.random.randint(low=1, high=20)

    # c and b were derived and generated as follows:
    c = a**2 + 2
    b = a**2 + 1
    
    # solve the limit using the generated c and b values
    x = symbols('x')
    expr = sqrt(  (x+1) / ( (x)**2 + c*x + b ) )
    result = limit(expr, x, -1)

    return a, b, c, result

# Handle the callback for the answer box
def handle_text_change():
    # get text string from answer box
    current_text = st.session_state.answer_area
    
    # convert provided answer into a fraction
    # prevent error edge case if submit is pressed with no answer input
    if current_text is not None:
        current_answer = nsimplify(current_text)
    else:
        return
    # compare provided answer against correct answer
    answer = False
    if current_answer == st.session_state.result:
        answer = True
    
    # store results back in session state to display in the UI
    st.session_state.answer = answer
    st.session_state.curr_answer = current_answer

# Clear all session_state keys for question reset
def clear_session_state():
    # delete all items from the session state, app auto reruns
    for key in list(st.session_state.keys()):
        del st.session_state[key]

# toggles value used for solution display button
def toggle_content():
    st.session_state.show_content = not st.session_state.show_content

#############################################
### QUESTION PROMPT ###

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
lim_disp = r'\lim\limits_{x \to -1} \sqrt{ \dfrac{x+1}{x^{2}+%sx+%s} }' % (st.session_state.c, st.session_state.b)

# create main container to hold the entire question prompt
main_container = st.container(border=True, horizontal_alignment="center")
main_container.markdown("## Solve the limit:", text_alignment="center")
main_container.markdown(f"${lim_disp}$", text_alignment="center")

# create secondary container to hold "your answer: [answer input] [submit]"
left, right = main_container.columns(2, vertical_alignment="center")
left.markdown("### Your answer: ", text_alignment="right")

# create tertiary container to hold "[answer input] [submit]"
answer_box, submit_btn = right.columns([8,4]) 
number = answer_box.text_input(
    label="", label_visibility='collapsed',
    value=None, placeholder="Ex: 3.4", width=220, max_chars=25, 
    key="answer_area", on_change=handle_text_change)

if submit_btn.button("Submit"):
    handle_text_change()

#############################################
### RESPONSE AND TRY AGAIN ###

# display answer correctness
if st.session_state.answer is None:
    st.markdown("")
elif st.session_state.answer:
    st.markdown(f"Your Answer: ${st.session_state.curr_answer}$")
    st.markdown(f":green[:material/check: Correct]. The limit is ${st.session_state.result}$.")
else:
    st.markdown(f"Your Answer: ${st.session_state.curr_answer}$")
    st.markdown(f":red[:material/close: Incorrect]. The limit is ${st.session_state.result}$.")

# button to generate a new limit
st.button("Try Another", on_click=clear_session_state)

#############################################
### OPTIONAL SOLUTION ###

# initialize in session_state
if "show_content" not in st.session_state:
    st.session_state.show_content = False
# determine button label to be shown
if st.session_state.show_content: 
    button_label = "Hide Solution" 
else:
    button_label = "Show Solution"

st.button(button_label, on_click=toggle_content)

# display solution if toggled to show
if st.session_state.show_content:
    # solving for the solution of the limit
    exp_container = st.container(border=True, horizontal_alignment="left")
    exp_container.markdown("### Solution: ")

    exp_container.markdown(f"Given: ")
    exp_container.markdown(f"${lim_disp}$")

    exp_container.markdown(f"Simplify the function within the square root of the limit.")
    fx_disp = r'\sqrt{ \dfrac{x+1}{x^{2}+%sx+%s} }' % (st.session_state.c, st.session_state.b)
    sim_fx_disp = r'\sqrt{ \dfrac{1}{x+%s} }' % (st.session_state.b)
    exp_container.markdown(f"${fx_disp}$ -> ${sim_fx_disp}$")

    exp_container.markdown(f"Evaluate the simplified function where $x$ is equal to $-1$.")
    sim_fx_disp = r'\sqrt{ \dfrac{1}{-1+%s} }' % (st.session_state.b)
    exp_container.markdown(f"${sim_fx_disp} = {st.session_state.result}$")
