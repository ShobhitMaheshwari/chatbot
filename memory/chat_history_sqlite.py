import sqlite3
import config
from utils.file_logger import get_logger

sqlite_conn = sqlite3.connect(config.CHAT_HISTORY_SQLITE_DB_DIR)

file_logger = get_logger("chat_history.log")

def create_table():
    cursor = sqlite_conn.cursor()
    cursor.execute('''create table ChatHistory
                      (
                      id integer PRIMARY KEY AUTOINCREMENT,
                      userId text,
                      sessionId text,
                      timestamp DATETIME DEFAULT CURRENT_TIMESTAMP,
                      subHistoryId integer,
                      chatInput text,
                      chatResponse text
                      )''')
    sqlite_conn.commit()
    print("News Table created!")

def insert_chat(user_id, session_id, sub_history_id=0, chat_input='', chat_response=''):
    cursor = sqlite_conn.cursor()
    query = 'INSERT INTO ChatHistory(userId, sessionId, subHistoryId, chatInput, chatResponse) VALUES (?, ?, ?, ?, ?)'
    chat_tuple = (user_id, session_id, sub_history_id, chat_input, chat_response)
    file_logger.info("Insert chat " + str(chat_tuple))
    cursor.execute(query, chat_tuple)
    sqlite_conn.commit()

def _get_where_clause(user_id=None, session_id=None, other=None):
    where = []
    if user_id is not None:
        where.append("userId='" + user_id + "'")
    if session_id is not None:
        where.append("sessionId='" + session_id + "'")
    if other is not None:
        where.append(other)
    if len(where) > 0:
        return " where " + (" and ".join(where))
    return ""

def query_chat(user_id=None, session_id=None):
    cursor = sqlite_conn.cursor()
    query = 'SELECT userId, sessionId, subHistoryId, timestamp, chatInput, chatResponse FROM ChatHistory {} order by timestamp desc'\
        .format(_get_where_clause(user_id, session_id))
    file_logger.info(query)
    cursor.execute(query)
    items = cursor.fetchall()
    return items

def query_last_chat_input(user_id, session_id):
    cursor = sqlite_conn.cursor()
    query = 'SELECT chatInput FROM ChatHistory {} order by id desc limit 1'\
        .format(_get_where_clause(user_id, session_id, "chatInput != ''"))
    file_logger.info(query)
    cursor.execute(query)
    item = cursor.fetchone()
    if item is not None:
        return item[0]
    return ""

def query_last_chat_response(user_id, session_id):
    cursor = sqlite_conn.cursor()
    query = 'SELECT chatResponse FROM ChatHistory {} order by id desc limit 1'\
        .format(_get_where_clause(user_id, session_id, "chatResponse != ''"))
    file_logger.info(query)
    cursor.execute(query)
    item = cursor.fetchone()
    if item is not None:
        return item[0]
    return ""

def query_chat_input_by_history_id(user_id, session_id, sub_history_id):
    cursor = sqlite_conn.cursor()
    query = 'SELECT chatInput FROM ChatHistory {} order by id desc limit 1'\
        .format(_get_where_clause(user_id, session_id, "chatInput != '' and subHistoryId=" + str(sub_history_id)))
    file_logger.info(query)
    cursor.execute(query)
    item = cursor.fetchone()
    if item is not None:
        return item[0]
    return ""

def query_chat_response_by_history_id(user_id, session_id, sub_history_id):
    cursor = sqlite_conn.cursor()
    query = 'SELECT chatResponse FROM ChatHistory {} order by timestamp desc limit 1'\
        .format(_get_where_clause(user_id, session_id, "chatResponse != '' and subHistoryId=" + str(sub_history_id)))
    file_logger.info(query)
    cursor.execute(query)
    item = cursor.fetchone()
    if item is not None:
        return item[0]
    return ""

def remove_chat(user_id=None, session_id=None):
    cursor = sqlite_conn.cursor()
    query = 'DELETE FROM ChatHistory {}'.format(_get_where_clause(user_id, session_id))
    row_num = cursor.execute(query).rowcount
    file_logger.info(query)
    sqlite_conn.commit()
    file_logger.info("Delete " + str(row_num) + " of chat history. user_id=" + str(user_id) + ", session_id=" + str(session_id))
    return row_num

if __name__ == "__main__":
    # create_table()
    # remove_chat()
    pass
