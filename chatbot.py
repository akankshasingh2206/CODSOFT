def chatbot():
    print("🤖 Chatbot: Hello! Type 'bye' to exit.")
    
    last_mood = None
    user_interest = ""
       
    while True:
        user_input = input("You: ").lower().strip()

        # Exit
        if user_input == "bye":
            print("🤖 Chatbot: Goodbye!")
            break

        # Greetings
        elif user_input in ["hello", "hi", "hey"]:           
            print("🤖 Chatbot: Hello! How can I help you?")

        # Asking Name of the chatbot
        elif "what's your name" in user_input:
            print("🤖 Chatbot: My name is RuleBot.")
        # Asking your name    
        elif "what's my name" in user_input:
            print("🤖 Chatbot: Your name is Akanksha.")

        # Asking time
        elif "what is the current time" in user_input:
            from datetime import datetime
            current_time = datetime.now().strftime("%H:%M:%S")
            print("🤖 Chatbot: Current time is", current_time)

        # Asking date
        elif "what is the date today" in user_input:
            from datetime import date
            today = date.today()
            print("🤖 Chatbot: Today's date is", today)
        
        #Happy Mood
        elif "happy" in user_input:
            last_mood = "happy"
            print("🤖 Chatbot: That's wonderful! I'm glad you're happy.")
        
        #Sad Mood
        elif "sad" in user_input:
            last_mood = "sad"
            print("🤖 Chatbot: I'm sorry to hear that. I hope things get better soon.")
        
        #Mood Checking
        elif "how am i feeling" in user_input:
            if last_mood:
              print(f"🤖 Chatbot: Earlier you mentioned that you were {last_mood}.")
            else:
              print("🤖 Chatbot: You haven't told me how you're feeling yet.")
        
        #Career Guidance based on favorites
        elif "i like coding" in user_input:
            user_interest = "coding"
            print("🤖 Chatbot: Based on your interest in coding, I recommend to builld your career in Software Development, AI, Data Science, or Cybersecurity.")

        elif "i like designing" in user_input:
            user_interest = "designing"
            print("🤖 Chatbot: Based on your interest in designing, I recommend to build your career in UI/UX Design, Graphic Design, or Animation.")

        elif "i like data entry" in user_input:
            user_interest = "data entry"
            print("🤖 Chatbot: Based on your interest in data entry, I recommend to build your career in Data Analysis, Database Administration, or Business Operations.")
        elif "career suggestion" in user_input:
            if user_interest == "":
                print("🤖 Chatbot: Please tell me your interest first (coding, designing, data entry).")

            elif user_interest == "coding":
                print("🤖 Chatbot: you can become: Software Developer, AI Engineer, Data Scientist, Cybersecurity Expert.")

            elif user_interest == "designing":
                print("🤖 Chatbot: you can become: UI/UX Designer, Graphic Designer, Animator, Product Designer.")

            elif user_interest == "data entry":
                print("🤖 Chatbot: you can become: Data Entry Operator, Data Analyst, Office Administrator, Business Executive.")
        # Help
        elif "help" in user_input:
            print("🤖 Chatbot: I can help you in answering greetings, time, date, moodtracking, careersuggestions, interests.")
        
        # Default
        else:
            print("🤖 Chatbot: Sorry, I don't understand what you want to say.Can u just repeat again?")

chatbot()