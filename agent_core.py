import re
from memory import chat_history_sqlite as db

class CoreAgent():

    def __init__(self, user_id, session_id, tools = None,):
        """
        CoreAgent is a class for chatbot
        :param user_id: the id to identify different user.
        :param session_id: the id to idendify different conversation session.
        :param tools: the tools might be needed for the chatbot.
        """
        self.user_id = user_id
        self.session_id = session_id
        self.history_id = 0
        self.bot_name = "Slug"
        if tools != None:
            self.tools = tools
        else:
            # Initial resources here.
            pass

        self.goodbye_pattern = re.compile(r'\b(bye|quit|goodbye|good bye|stop|exit)\b', re.IGNORECASE)
        self.shall_stop = False


    def give_greeting(self):
        """
        :return: greeting message when ever the chatbot is initialized.
        """
        return "Hello. Let's chat."

    def get_input(self, chat_input):
        """
        Get the user input and store it in the SQLite DB. Please note that the self.history_id must increase by 1.
        :param chat_input:
        :return:
        """
        # TODO: ananlyse the user input utterance
        db.insert_chat(self.user_id, self.session_id, self.history_id, chat_input=chat_input)
        self.history_id += 1

        # When user says bye|quit|goodbye|good bye|stop|exit without punctuation, the system shall exit.
        if self.goodbye_pattern.match(chat_input) is not None:
            self.shall_stop = True
        pass

    def give_response(self):
        """
        Generate response for the most current user input. Now it only echo the user input.
        Please note that the self.history_id must increase by 1.
        history_id can be used for fetch the previous utterance.
        :return:
        """
        chat_input = db.query_last_chat_input(self.user_id, self.session_id)
        # TODO: generate the response according to user input.
        chat_response = "Echo " + chat_input

        db.insert_chat(self.user_id, self.session_id, self.history_id, chat_response=chat_response)
        self.history_id += 1
        return chat_response





