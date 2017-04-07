import os

MAIN_DIR = os.path.dirname(os.path.abspath(__file__))

LOGGER_DIR = os.path.join(MAIN_DIR, "logs/")
RESOURCES = os.path.join(MAIN_DIR, "resources/")
MEMORY = os.path.join(MAIN_DIR, "memory/")
SQLITE_DB_DIR = os.path.join(MAIN_DIR, "memory/sqlite_db")
CHAT_HISTORY_SQLITE_DB_DIR = os.path.join(MAIN_DIR, "memory/sqlite_db/chat_history.sqlite")
