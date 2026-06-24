# 💭 Reflection: Game Glitch Investigator

Answer each question in 3 to 5 sentences. Be specific and honest about what actually happened while you worked. This is about your process, not trying to sound perfect.

## 1. What was broken when you started?

When I first ran the game, the Streamlit app opened, but the gameplay was not working correctly. The biggest issue was that after entering the first guess, the app did not properly display whether the secret number was higher or lower, so the user could not continue playing. Another bug was that the hint logic was incorrect because some guesses were receiving the wrong feedback, and the game state was not being saved correctly between Streamlit reruns.

- What did the game look like the first time you ran it?

- List at least two concrete bugs you noticed at the start  
  (for example: "the hints were backwards").

**Bug Reproduction Log**

Document at least 3 bugs you found. Add rows as needed.

| Input | Expected Behavior | Actual Behavior | Console Output / Error |
|-------|-------------------|-----------------|------------------------|
| | | | |
| | | | |
| | | | |
Input	Expected Behavior	Actual Behavior	Console Output / Error
Guess: 50, Secret: 70	Display "Too Low" and allow another guess	No hint appeared after submitting the guess	No console error, Streamlit reran and reset values
Guess: 80, Secret: 50	Display "Too High"	Hint was incorrect because comparison logic was reversed	No error, incorrect output from game logic
Guess: 50, Secret: 50	Display "Win" and end the game	Game did not consistently recognize the correct guess	Pytest initially failed because check_guess() returned the wrong result

---

## 2. How did you use AI as a teammate?

- Which AI tools did you use on this project (for example: ChatGPT, Gemini, Copilot)?
- Give one example of an AI suggestion that was correct (including what the AI suggested and how you verified the result).
- Give one example of an AI suggestion that was incorrect or misleading (including what the AI suggested and how you verified the result).

I used Claud as an AI assistant to help me understand the existing code, identify bugs, and suggest fixes for the Streamlit app. One correct suggestion from AI was to add Streamlit session state to store the secret number and previous guesses, since Streamlit re-runs the entire script after each button click. I verified this by testing the app multiple times and confirming that the secret number remained the same during each guess.

One misleading suggestion from AI was to change only the display code to fix the missing hints. After testing, I realized the problem was not only the UI but also the game logic and state management. I verified this by running the program and checking that the hint still failed until I fixed the logic functions and session state.


---

## 3. Debugging and testing your fixes

- How did you decide whether a bug was really fixed?
- Describe at least one test you ran (manual or using pytest)  
  and what it showed you about your code.
- Did AI help you design or understand any tests? How?

I decided a bug was fixed when I could reproduce the original problem, apply the change, and then confirm the expected behavior happened consistently. I tested different guesses manually, including guesses that were too high, too low, and the exact secret number. I also used pytest with functions like check_guess() to verify that the game logic returned "Win," "Too High," and "Too Low" correctly.

AI helped me understand how to write and organize tests by explaining what each test should check. For example, AI helped create tests where the secret number was fixed at 50, and different guesses were used to verify each possible result.
---

## 4. What did you learn about Streamlit and state?

- How would you explain Streamlit "reruns" and session state to a friend who has never used Streamlit?
I learned that Streamlit re-runs the entire Python script every time the user interacts with a widget like a button or input box. Without session state, the variables, including the secret number, are reinitialized, making the game start again from scratch. The session state can be explained as temporary memory of the app regarding the user.

---

## 5. Looking ahead: your developer habits

- What is one habit or strategy from this project that you want to reuse in future labs or projects?
  - This could be a testing habit, a prompting strategy, or a way you used Git.
- What is one thing you would do differently next time you work with AI on a coding task?
- In one or two sentences, describe how this project changed the way you think about AI generated code.
One habit I want to reuse in future projects is testing small parts of my code before connecting everything together. Writing and running tests for individual functions made it easier to find whether the problem was in the logic or the user interface.

Next time I work with AI on a coding task, I would ask more specific questions, verify every suggestion, and keep a log of the suggestions. This project changed my view of AI-generated code because I learned that AI can help speed up the debugging process and explain concepts when I am stuck, but I still need to make sure I understand the code, test it, and validate the code to make sure it’s how I want it to be. 
