# boot.py

import sys
import importlib
import pysqlite3

# Forcefully patch sqlite3 to use pysqlite3
sys.modules["sqlite3"] = pysqlite3
importlib.reload(pysqlite3)
