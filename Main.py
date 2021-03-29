# -*- coding: utf-8 -*-
"""
Created on Fri Mar 26 19:13:44 2021

@author: Solana
"""

import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("fraudTrain.csv")

"""
 * trans_date_trans_time
 * category
 * genders
 * city
 * state
 * job
 * dob
"""

months = pd.to_datetime(df["trans_date_trans_time"]).dt.month
m_freq = months.value_counts()
m_freq.plot.bar(rot=0)

"""
May day fraud is higer 
"""

hours = pd.to_datetime(df["trans_date_trans_time"]).dt.hour
h_freq = hours.value_counts()
h_freq.plot.bar(rot=0)

"""
23 22 18 16 21 19 17 15 13 12 20 fraud is higer
"""

categories = df["category"]
cate_freq = categories.value_counts()
cate_freq.plot.bar(rot="90")
"""
gas transfer frauded is higer
"""

genders = df["gender"]
gen_freq = genders.value_counts()
gen_freq.plot.bar(rot=0)

"""
female frauded is higer
"""

citys = df["city"]
citys_freq = citys.value_counts()
# citys_freq.plot.bar(rot="90")

"""
Birmingham frauded is higer
"""

state = df["state"]
state_freq = state.value_counts()
state_freq.plot.bar(rot=45)

"""
TX NY PA frauded is higer
"""

job = df["job"]
job_freq = job.value_counts()
job_freq.plot.bar(rot=90)

"""
Film/video editor
Exhibition designer
Naval architect
Surveyor, land/geomatics
"""  

dob = pd.to_datetime(df["dob"]).dt.year
d_freq = dob.value_counts()
d_freq.plot.bar(rot=0)

"""
1972 1984 1987 1985
"""
