import streamlit as st
from utils import write_message
# tag::import_agent[]
from agent import generate_response
# end::import_agent[]

# tag::setup[]
# Page Config
st.set_page_config("Khonsu", page_icon=":car:")
# end::setup[]

# tag::session[]
# Set up Session State
if "messages" not in st.session_state:
    st.session_state.messages = [
        {"role": "assistant", "content": "Hi, I'm Khonsu!  How can I assit you today?"},
    ]
# end::session[]

# tag::submit[]
# Submit handler
def handle_submit(message):
    """
    Submit handler
    """

    # Handle the response
    with st.spinner('Pondering...'):
        # Call the agent
        response = generate_response(message)
        write_message('assistant', response)
        
# end::submit[]


# tag::chat[]
# Display messages in Session State
for message in st.session_state.messages:
    write_message(message['role'], message['content'], save=False)

# Handle any user input
if prompt := st.chat_input("What is up?"):
    # Display user message in chat message container
    write_message('user', prompt)

    # Generate a response
    handle_submit(prompt)
# end::chat[]
