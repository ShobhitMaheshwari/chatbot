import unittest
from memory import chat_history_sqlite as db

class TestAgentCore(unittest.TestCase):
    def setUp(self):
        self.user_id = "slug_id"
        self.session_id = "ABC123"
        self.history_id = 0
        pass

    def test_insert_chat(self):
        db.insert_chat(self.user_id, self.session_id, self.history_id, chat_input="Hello")
        self.history_id += 1
        db.insert_chat(self.user_id, self.session_id, self.history_id, chat_response="Hi")
        self.history_id += 1

        db.insert_chat(self.user_id, self.session_id, self.history_id, chat_input="Let's chat.")
        self.history_id += 1
        db.insert_chat(self.user_id, self.session_id, self.history_id, chat_response="Ok. Let's chat.")
        self.history_id += 1

    def test_query_chat_by_userId_session_id(self):
        items = db.query_chat(self.user_id, self.session_id)
        for item in items:
            print(item)
        self.assertEqual(4, len(items))

    def test_query_chat_by_userId(self):
        items = db.query_chat(user_id=self.user_id)
        self.assertEqual(4, len(items))

    def test_query_chat_by_sessionId(self):
        items = db.query_chat(session_id=self.session_id)
        self.assertEqual(4, len(items))

    def test_query_chat(self):
        items = db.query_chat()
        self.assertTrue(len(items) >= 4)

    def test_query_last_chat_input(self):
        item = db.query_last_chat_input(self.user_id, self.session_id)
        self.assertEqual("Let's chat.", item)

    def test_query_last_chat_response(self):
        item = db.query_last_chat_response(self.user_id, self.session_id)
        self.assertEqual("Ok. Let's chat.", item)

    def test_query_chat_input_by_history(self):
        sub_history_id = 0
        item = db.query_chat_input_by_history_id(self.user_id, self.session_id, sub_history_id)
        self.assertEqual("Hello", item)

        sub_history_id = 1
        item = db.query_chat_input_by_history_id(self.user_id, self.session_id, sub_history_id)
        self.assertEqual("", item)

    def test_query_chat_response_by_history(self):
        sub_history_id = 0
        item = db.query_chat_response_by_history_id(self.user_id, self.session_id, sub_history_id)
        self.assertEqual("", item)

        sub_history_id = 1
        item = db.query_chat_response_by_history_id(self.user_id, self.session_id, sub_history_id)
        self.assertEqual("Hi", item)

    def test_remove_chat(self):
        row_count = db.remove_chat(self.user_id, self.session_id)
        self.assertEqual(4, row_count)
        self.assertEqual([], db.query_chat(self.user_id, self.session_id))

if __name__ == '__main__':
    unittest.main()