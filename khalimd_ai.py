import streamlit as st

st.set_page_config(page_title="Khalimd AI", page_icon="🤖")

st.title("Khalimd AI")
st.write("Your personal AI assistant for learning and solving maths.")

name = st.text_input("What is your name?")
if name:
    st.success(f"Welcome to Khalimd AI, {name}!")

feature = st.selectbox(
    "Choose an option",
    ["Chat with me", "Solve a math problem"]
)

if feature == "Chat with me":
    st.subheader("Chat with me")
    st.write("Hello! I'm Khalimd AI. Ask me a question.")

    message = st.chat_input("Type your message here")

    if message:
        st.write("You:", message)

        question = message.lower()

        if "hello" in question or "hi" in question:
            st.write("Khalimd AI: Hello! How can I help you today?")
        elif "your name" in question:
            st.write("Khalimd AI: My name is Khalimd AI!")
        elif "python" in question:
            st.write("Khalimd AI: Python is a programming language used to build apps and websites.")
        elif "thank" in question:
            st.write("Khalimd AI: You're welcome!")
        else:
            st.write(
                "Khalimd AI: I'm still learning. "
                "Try asking me about Python, or say hello!"
            )

elif feature == "Solve a math problem":
    st.subheader("Khalimd Maths Solver")

    num1 = st.number_input("Enter the first number", key="number_one")
    num2 = st.number_input("Enter the second number", key="number_two")

    operation = st.selectbox(
        "Choose an operation",
        ["Add", "Subtract", "Multiply", "Divide"],
        key="math_operation"
    )

    if st.button("Calculate"):
        if operation == "Add":
            st.success(f"Answer: {num1 + num2}")
        elif operation == "Subtract":
            st.success(f"Answer: {num1 - num2}")
        elif operation == "Multiply":
            st.success(f"Answer: {num1 * num2}")
        elif operation == "Divide":
            if num2 != 0:
                st.success(f"Answer: {num1 / num2}")
            else:
                st.error("You cannot divide by zero.")
