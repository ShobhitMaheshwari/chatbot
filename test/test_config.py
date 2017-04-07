import unittest, os
import config

class TestConfig(unittest.TestCase):
    def setUp(self):
        pass

    def test_root_path(self):
        print("Root")
        print(config.MAIN_DIR)
        self.assertTrue(os.path.exists(config.MAIN_DIR))

        folder_name = os.path.basename(config.MAIN_DIR)
        self.assertEqual(folder_name, "chatbots")
        print()

    def assertPathExist(self, dir):
        print(dir)
        self.assertTrue(os.path.exists(dir))
        print()

    def test_all_path(self):
        print("Log")
        self.assertPathExist(config.LOGGER_DIR)

        print("Resource")
        self.assertPathExist(config.RESOURCES)

        print("Memory")
        self.assertPathExist(config.MEMORY)

        print("SQLite")
        self.assertPathExist(config.SQLITE_DB_DIR)

        print("Chat history db")
        self.assertPathExist(config.CHAT_HISTORY_SQLITE_DB_DIR)


if __name__ == '__main__':
    unittest.main()