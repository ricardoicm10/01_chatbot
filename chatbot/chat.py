from nltk.chat.util import Chat, reflections

pairs = [
    (r"(hi|hello|hey|good morning|good evening)", ["Hello! How can I help you with flight bookings today?"]),
    
    (r"(buy|book) a flight to (.*)", ["From where would you like to fly?"]),
    
    (r"from (.*)", ["Got it! What dates are you planning to travel on?"]),
    
    (r"my travel date is (.*)", ["Thank you! I can help with pricing. What is your preferred class (economy, business, or first)?"]),
    
    (r"(economy|business|first)", ["Great! I'll check available flights in that class."]),
    
    (r"(how much|what is the cost) for a flight to (.*) on (.*)", ["Let me check the prices for you."]),
    
    (r"(thank you|thanks)", ["You're welcome! Let me know if you need further help."]),
    
    (r"(bye|goodbye)", ["Goodbye! Have a great day and safe travels!"])
]

chatbot = Chat(pairs, reflections)

# Start chatting with the bot
def start_chat():
    print("Hi! I'm here to help you with booking flights. Type 'quit' to end the chat.")
    while True:
        user_input = input("You: ")
        if user_input.lower() == 'quit':
            print("Goodbye!")
            break
        response = chatbot.respond(user_input)

        if not response:
            response = "Sorry, I didn't quite understand that. Could you please clarify?"
            
        print(f"Bot: {response}")

# Start the conversation
start_chat()





