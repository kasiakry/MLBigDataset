# -*- coding: utf-8 -*-
"""
Created on Sun Jun  2 16:45:46 2019

@author: xx
"""

import sqlite3
import pandas as pd
connection = sqlite3.connect("D:\WNE\lending-club-loan-data\database.sqlite")
cursor = connection.cursor()
cursor.execute("SELECT * FROM loan")
result = cursor.fetchall()
connection.close()

data = pd.DataFrame(result)