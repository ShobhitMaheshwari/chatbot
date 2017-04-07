import unittest
from agent_core import CoreAgent

class TestAgentCore(unittest.TestCase):
    def setUp(self):
        self.chatbot = CoreAgent("Banana Slug")

    def test_give_greeting(self):
        self.assertEqual("Hello. Let's chat.", self.chatbot.give_greeting())

    def test_goodbye(self):
        self.chatbot.get_input("Bye")
        self.assertTrue(self.chatbot.shall_stop)

if __name__ == '__main__':
    unittest.main()