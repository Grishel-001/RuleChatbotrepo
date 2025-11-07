def get_bot_response(user_input):
    """
    Analyzes the user's input and returns a rule-based response.
    """
    # Clean and normalize the user's input
    cleaned_input = user_input.lower().strip()

    # --- Rule Set ---

    # 1. Greetings
    if cleaned_input in ["hello", "hi", "hey", "greetings"]:
        return "Hello there! How can I help you today?"

    # 2. Farewells (The main loop also checks for this)
    if cleaned_input in ["bye", "goodbye", "exit", "quit"]:
        return "Goodbye! Have a great day."

    # 3. 'How are you?'
    if "how are you" in cleaned_input:
        return "I'm just a bunch of code, but I'm running perfectly! Thanks for asking."

    # 4. 'What is your name?' / 'Who are you?'
    if "your name" in cleaned_input or "who are you" in cleaned_input:
        return "I am a simple rule-based chatbot, created in Python!"

    # 5. 'What is the time?'
    if "time" in cleaned_input:
        # A real bot would use the `datetime` library.
        # For a simple rule-based bot, a canned answer is fine.
        return "I'm not connected to a live clock, but it's always time to code!"

    # 6. 'What is your purpose?' / 'What can you do?' / 'Help'
    if ("purpose" in cleaned_input) or ("what can you do" in cleaned_input) or (cleaned_input == "help"):
        return "I am here to demonstrate a simple rule-based chatbot. You can ask me my name, how I am, or say hello/bye."
    
    # 7. Creator / 'Who made you?'
    if "creator" in cleaned_input or "made you" in cleaned_input or "built you" in cleaned_input:
        return "I was built by a developer as an example of a simple AI."

    # 8. The Default/Fallback Rule
    else:
        return "I'm sorry, I don't understand that. Please try rephrasing, or type 'help' to see what I can do."


def main():
    """
    The main loop that runs the chatbot.
    """
    print("🤖 Chatbot: Hi! I'm a simple chatbot. Type 'bye' to exit.")
    print("--------------------------------------------------")

    while True:
        # Get input from the user
        user_message = input("You: ")
        
        # Check for exit condition
        if user_message.lower().strip() in ["bye", "goodbye", "exit", "quit"]:
            print("Chatbot: Goodbye! Have a great day.")
            break  # Exit the while loop

        # Get the bot's response
        bot_response = get_bot_response(user_message)
        
        # Print the response
        print(f"Chatbot: {bot_response}")

# This makes the script runnable
if __name__ == "__main__":
    main()