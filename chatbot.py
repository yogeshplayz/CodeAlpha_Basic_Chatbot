def get_bot_response(user_input):
    """
    Determines the chatbot's response based on the user's input.
    Uses .lower() and .strip() to handle variations in user formatting.
    """
    # Clean the input by removing extra spaces and changing it to lowercase
    cleaned_input = user_input.strip().lower()
    
    # Rule-based logic using if-elif-else statements
    if cleaned_input == "hello":
        return "Hi there! How can i assit you today?"
    elif cleaned_input == "how are you":
        return "I'm fine, thanks!"
    elif cleaned_input == "what is your name"
        return "I'm CodeAlpha Basic Chatbot."    
    elif cleaned_input == "bye":
        return "Goodbye!"
    else:
        return "I am a simple rule-based bot. I don't understand that yet."

def start_chatbot():
    """
    Main loop to control the user interaction and execution of the chatbot.
    """
    print("🤖 Chatbot: Hello! Type 'bye' to exit the conversation.")
    
    # Loop continuously until the user says 'bye'
    while True:
        # Capture input from the user
        user_message = input("You: ")
        
        # Get the predefined reply from our function
        bot_reply = get_bot_response(user_message)
        
        # Output the bot's reply
        print(f"🤖 Chatbot: {bot_reply}")
        
        # Break the loop if the user typed "bye" (ignoring spaces/case)
        if user_message.strip().lower() == "bye":
            break

# Execute the chatbot function
if __name__ == "__main__":
    start_chatbot()
