import re

def simple_chatbot():
    print("Chatbot: Hello! Ask me something or type 'bye' to exit.")

    while True:
        user_input = input("You: ").lower()

        if re.search(r'\b(hi|hello|hey)\b', user_input):
            print("Chatbot: Hello there!")
        elif re.search(r'\bhow are you\b', user_input):
            print("Chatbot: I'm doing well, thank you!")
        elif re.search(r'\b(your name|who are you)\b', user_input):
            print("Chatbot: I'm a created chatbot.")
        elif re.search(r'\b(who created you?)\b', user_input):
            print("Chatbot: my program creator.")
        elif re.search(r'\bbye\b', user_input):
            print("Chatbot: goodbye! Have a nice day.")
            break
        else:
            print("Chatbot: Sorry, I didn't understand that.")

simple_chatbot()