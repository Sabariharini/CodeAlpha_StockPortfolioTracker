def chat():
    print("Welcome to ChatBox")
    print("Type 'exit' to leave the chat.")

while True:
    user_input = input("You: ")
    if user_input.lower() == 'hello':
        print("Hi Dear! How can I help you today?")


    elif user_input.lower() == 'bye':
        print("Exiting the chat. Goodbye!")
        break

    elif user_input.lower() == 'how are you':
        print("I'm just a program, but I'm doing well! How about you?")     

    elif user_input.lower() == 'what is your name?':
        print("I am ChatBox, your friendly chatbot.")

    else:
        print("I'm sorry, I didn't understand that. Please try again.")                 

chat()