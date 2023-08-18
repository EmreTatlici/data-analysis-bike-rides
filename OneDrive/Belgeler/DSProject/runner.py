# -*- coding: utf-8 -*-
"""
Created on Thu Aug 17 13:48:47 2023

@author: emre-
"""

import glassdoor_scraper as gs


path = "C:/Users/emre-/OneDrive/Masaüstü/DSProject/chromedriver.exe"
df = gs.get_jobs("data scientist", 7, False, path, 3)
print(df)