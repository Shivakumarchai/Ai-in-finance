import random

# define some responses for the chatbot
greetings = ["hello", "hi", "hey", "what's up","good morning","good afternoon"]
thanks = ["thank you", "thanks", "great", "awesome"]
goodbyes = ["goodbye", "bye", "see you later"]
balance_enquiries = ["what is my balance?", "how much do I have?", "can you tell me my balance?","check my balance","my balance"]
account_questions = ["what types of accounts do you offer?", "how can I open an account?",
                     "what are the requirements for opening an account?"]
loan_enquiries = ["what types of loans do you offer?", "how can I apply for a loan?",
                  "what are the requirements for getting a loan?"]


# define a function to randomly select a response from a list of responses
def get_response(lst):
    return random.choice(lst)


# define the main function for the chatbot
def bank_assistant():
    print("Hello !,My name is Shiva, I'm your bank assistant. How can I help you today?")

    # loop until the user says goodbye
    while True:
        user_input = input().lower()

        # check for greetings
        if any(greeting in user_input for greeting in greetings):
            print(get_response(greetings))

        # check for thanks
        elif any(thank in user_input for thank in thanks):
            print(get_response(thanks))

        # check for balance enquiries
        elif any(balance_enquiry in user_input for balance_enquiry in balance_enquiries):
            print("Your current balance is $1000.")

        # check for account questions
        elif any(account_question in user_input for account_question in account_questions):
            print(
                "We offer savings, checking, and money market accounts. You can open an account online or at any of our branches. Please bring two forms of ID and proof of address and Bring 2 Passport size Photos.")

        # check for loan enquiries
        elif any(loan_enquiry in user_input for loan_enquiry in loan_enquiries):
            print(
                "We offer personal loans, home loans, and business loans. You can apply online or at any of our branches. Please bring proof of income and a credit report.")

        # check for goodbyes
        elif any(goodbye in user_input for goodbye in goodbyes):
            print(get_response(goodbyes))
            break

        # if the user's input doesn't match any of the above, ask them to repeat
        else:
            print("I'm sorry, I didn't understand. Can you please repeat? OR ")
            print("I'm unable to response.Please contact to our nearest branch ");


# call the main function to start the chatbot
bank_assistant()
