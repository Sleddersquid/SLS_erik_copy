# -*- coding: utf-8 -*-
"""
Created on Fri Sep 16 14:39:29 2022

@author: aditi
"""

import mysql.connector as mc
conn = mc.connect(host = "localhost",user="root",passwd="password123")
print(conn)
