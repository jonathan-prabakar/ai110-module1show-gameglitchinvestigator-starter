# 💭 Reflection: Game Glitch Investigator

Answer each question in 3 to 5 sentences. Be specific and honest about what actually happened while you worked. This is about your process, not trying to sound perfect.

I went with 77 and then it told me to go higher every time until I reached 100 and it said go lower. I also said 99 but it said higher so the logic for that is not there at all. I then went to a way lower number at 34, but it said higher again so I ran out of attempts finding the right number. The number was then 20 which did not make sense.

## 1. What was broken when you started?

- What did the game look like the first time you ran it?
- List at least two concrete bugs you noticed at the start  
  (for example: "the hints were backwards").

- It asked me to guess a number and the difficulty was normal.
- The show hints button did not work and the developer debug info attemps did not match the attempts left from the user display 

## 2. How did you use AI as a teammate?

- Which AI tools did you use on this project (for example: ChatGPT, Gemini, Copilot)? 
- Give one example of an AI suggestion that was correct (including what the AI suggested and how you verified the result).
- Give one example of an AI suggestion that was incorrect or misleading (including what the AI suggested and how you verified the result).

--- I used Copilot VS code agent
- One AI Suggestion that was correct while the check_guess function returned a tuple, the tests were only asserting the outcome string((win or loss))
- The AI suggestions was not incorrect any time

## 3. Debugging and testing your fixes

- How did you decide whether a bug was really fixed?
- Describe at least one test you ran (manual or using pytest)  
  and what it showed you about your code.
- Did AI help you design or understand any tests? How?

--- I looked at the old and new code and see how the logic is changed
- I used pytest in testgame py file to see if the tests are good
- Yes, if the guess is lower or higher or same, it would return a corresponding message

## 4. What did you learn about Streamlit and state?

- How would you explain Streamlit "reruns" and session state to a friend who has never used Streamlit?

--- Everytime there are changes made to the code, the app reruns the app so that changes are reflceted real-time

## 5. Looking ahead: your developer habits

- What is one habit or strategy from this project that you want to reuse in future labs or projects?
  - This could be a testing habit, a prompting strategy, or a way you used Git.
- What is one thing you would do differently next time you work with AI on a coding task?
- In one or two sentences, describe how this project changed the way you think about AI generated code.

- I would definitely implement test cases in my future 
- I would use context using # when prompting
- Giving it more context leads to more accurate answers