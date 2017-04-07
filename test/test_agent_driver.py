import unittest
import random
from agent_driver import run_bot
from unittest.mock import patch

class TestAgentDriver(unittest.TestCase):
    def setUp(self):
        self.user_id = str(random.randint(1, 10))
        self.session_id = str(random.randint(1, 10))

    def test_goodbye(self):
        with unittest.mock.patch('builtins.input', prompt="User: ", return_value='Bye'):
            run_bot(self.user_id, self.session_id)

if __name__ == '__main__':
    unittest.main()