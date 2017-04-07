from agent_core import CoreAgent
import random


def run_bot(user_id, session_id):
    chatbot = CoreAgent(user_id, session_id)
    # Greeting
    print(chatbot.bot_name + ": " + chatbot.give_greeting())
    while (True):
        # User Input
        input_utterance = input("User: ")
        chatbot.get_input(input_utterance)
        # When user says bye|quit|goodbye|good bye|stop|exit without punctuation, the system exit.
        if chatbot.shall_stop:
            break
        # Bot response
        response = chatbot.give_response()
        print(chatbot.bot_name + ": " + response)

if __name__ == '__main__':

    user_id = str(random.randint(1, 10))
    session_id = str(random.randint(1, 10))
    run_bot(user_id, session_id)





