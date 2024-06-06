def chatbot():
    greeting = "Hello!How can I help you today?"
    print(greeting)
    while True:
        user_input = input("You:")
        user_input = user_input.lower()

        if "hi" in user_input or "hello" in user_input: 
            print("chatbot:Hi there!")
        elif "weather" in user_input:
            print("chatbot:I can't provide weather information yet, but I'm still learning!")
        elif "time" in user_input:
            import datetime
            current_time = datetime.datetime.now().strftime("%H:%M:%S")
            print(f"chatbot:the current time is{current_time}")
        elif "bye" in user_input:
            print("chatbot:Bye! Have a nice day.")
            break
        else:
            print("chatbot:sorry,I don't understand, Try asking about the weather or time.")
chatbot()            
