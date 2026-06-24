# 🎮 Game Glitch Investigator: The Impossible Guesser

## 🚨 The Situation

You asked an AI to build a simple "Number Guessing Game" using Streamlit.
It wrote the code, ran away, and now the game is unplayable. 

- You can't win.
- The hints lie to you.
- The secret number seems to have commitment issues.

## 🛠️ Setup

1. Install dependencies: `pip install -r requirements.txt`
2. Run the broken app: `python -m streamlit run app.py`

## 🕵️‍♂️ Your Mission

1. **Play the game.** Open the "Developer Debug Info" tab in the app to see the secret number. Try to win.
2. **Find the State Bug.** Why does the secret number change every time you click "Submit"? Ask ChatGPT: *"How do I keep a variable from resetting in Streamlit when I click a button?"*
3. **Fix the Logic.** The hints ("Higher/Lower") are wrong. Fix them.
4. **Refactor & Test.** - Move the logic into `logic_utils.py`.
   - Run `pytest` in your terminal.
   - Keep fixing until all tests pass!

## 📝 Document Your Experience

- The game lets players guess a secret number based on a difficulty level. Players get hints telling them if their guess is too high or too low until they find the correct number.
- The secret number changed every time a button was clicked, making the game impossible to win. The hints were sometimes wrong, and there was no input box for players to enter their guesses.
- I used st.session_state to keep the secret number the same during the game. I fixed the hint logic so it correctly shows "Too High" or "Too Low" and added a guess input box for players.

## 📸 Demo Walkthrough

Describe your fixed game in numbered steps so a reader can follow along without watching a video:

1. The player opens the Streamlit app and selects a difficulty level (Easy, Normal, or Hard). 
2.The player clicks the "Start New Game" button, which creates and saves a secret number using Streamlit session state. 
3.The player enters a guess in the guess input box and clicks "Submit Guess". 
4. The game checks the guess and displays whether the number is "Too High", "Too Low", or correct. 
5. The player continues guessing until they find the secret number, and the attempts counter updates after each guess.

**Screenshot** *(optional)*: <!-- Insert a screenshot of your fixed, winning game here -->
![alt text](<Screenshot 2026-06-23 at 10.00.07 PM.png>)

## 🧪 Test Results
![alt text](<Screenshot 2026-06-23 at 10.24.48 PM.png>)
![alt text](<AI lab1.gif>)

```


## 🚀 Stretch Features

- [ ] [If you choose to complete Challenge 4, describe the Enhanced UI changes here — a screenshot is optional]
