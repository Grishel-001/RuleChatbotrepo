Simple Rule-Based Chatbot

This is a simple, console-based chatbot built in Python. It responds to user input based on a predefined set of rules, demonstrating the fundamentals of natural language processing (NLP) and conversational AI.

Features

Conversational Flow: Handles common interactions like greetings, goodbyes, and simple questions.

Rule-Based Matching: Uses basic string matching (the in operator) to identify user intent.

Input Normalization: Cleans user input (converts to lowercase, strips whitespace) to make matching more robust.

Fallback Response: Provides a generic "I don't understand" message when no rules are matched, which is a critical part of any chatbot.

Core Logic

The bot's "brain" is a single function, get_bot_response(), which uses a series of if/elif/else statements.

It checks the normalized user input against a list of keywords. For example, if the user's message contains the word "time", the bot will return its pre-programmed response about time. If no keywords are matched, it returns the final else (fallback) response.

How to Run

Clone the repository:

git clone [https://github.com/YourUsername/YourRepoName.git](https://github.com/YourUsername/YourRepoName.git)


Navigate to the directory:

cd YourRepoName


Run the script:

python rule_based_chatbot.py


Start chatting! Type bye or quit to exit the program.

Purpose

This project is a foundational exercise in AI and NLP. It serves as an excellent starting point for understanding how more complex systems (like virtual assistants and customer service bots) are built.
