import streamlit as st
import random

from logic_utils import (
    get_range_for_difficulty,
    parse_guess,
    check_guess
)


# App configuration
st.set_page_config(
    page_title="Game Glitch Investigator",
    page_icon="🎮"
)


# Title
st.title("🎮 Game Glitch Investigator")
st.write(
    "Find the secret number by making guesses!"
)


# Session state setup
if "secret_number" not in st.session_state:
    st.session_state.secret_number = None

if "attempts" not in st.session_state:
    st.session_state.attempts = 0

if "difficulty" not in st.session_state:
    st.session_state.difficulty = "Easy"

if "range" not in st.session_state:
    st.session_state.range = (1, 20)


# Difficulty selector
difficulty = st.selectbox(
    "Select Difficulty:",
    [
        "Easy",
        "Normal",
        "Hard"
    ]
)


# Start game button
if st.button("Start New Game"):

    low, high = get_range_for_difficulty(difficulty)

    st.session_state.secret_number = random.randint(
        low,
        high
    )

    st.session_state.attempts = 0
    st.session_state.difficulty = difficulty
    st.session_state.range = (low, high)

    st.success(
        f"Game started! Guess a number between {low} and {high}"
    )


# Show guess section only after game starts
if st.session_state.secret_number is not None:

    low, high = st.session_state.range

    st.subheader("Make Your Guess")

    # THIS WAS MISSING
    guess_input = st.text_input(
        f"Enter a number ({low}-{high}):"
    )


    if st.button("Submit Guess"):

        valid, guess, message = parse_guess(guess_input)

        if not valid:
            st.error(message)

        else:
            st.session_state.attempts += 1

            result = check_guess(
                guess,
                st.session_state.secret_number
            )


            if result == "Win":
                st.success(
                    "🎉 Correct! You found the number!"
                )

            elif result == "Too High":
                st.warning(
                    "⬆️ Too High! Try a smaller number."
                )

            elif result == "Too Low":
                st.warning(
                    "⬇️ Too Low! Try a larger number."
                )


# Sidebar information
st.sidebar.header("Game Info")

st.sidebar.write(
    "Difficulty:",
    st.session_state.difficulty
)

st.sidebar.write(
    "Attempts:",
    st.session_state.attempts
)