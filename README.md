# chatbot
Interface for chatbot

This repository provides a simple structure for chatbot. This chatbot will only echo whatever the user types in the terminal. We can run it as the following:

$python3 agent_driver.py


Python version: 3.4

**agent_core.py** chatbot that handle user input and generate response.

**agent_driver.py** main function that runs chatbot for users.

**memory/** SQLite files are kept in memory/, reference: https://www.sqlite.org/docs.html

**resources/** keeps resources like Stanford Corelp, etc.

**response/** maintain response generators that can be utilized by agent_core.py

**test/** It's nice to prevent bugs with unittest, reference: https://docs.python.org/3/library/unittest.html

**logs/** saves the log files for debugging.

**utiles/** keeps helper files.








