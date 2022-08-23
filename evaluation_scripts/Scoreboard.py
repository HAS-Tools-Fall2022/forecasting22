# This script calcualtes the total scores for everyone using
# the summary outputs from the score_weekly.py

# %%
import pandas as pd
import numpy as np
from glob import glob
import os
import matplotlib.pyplot as plt
from pandas.plotting import table

# %%
# Make a list of all the files in the results folder with names
# starting with forecast and ending with week.csv
# For more information on glob refer to:
# https://www.earthdatascience.org/courses/intro-to-earth-data-science/
# Chapter 12 lesson 3
file_list = glob(os.path.join('../weekly_results', 'forecast_week*.csv'))
file_listB = glob(os.path.join('../weekly_results', 'bonus*.csv'))

# Get the week numbers from the file list by splitting the strings
forecast_names = [file_list[i].split('_')[2] for i in range(len(file_list))]
bonus_names = [file_listB[i].split('_')[2][0:-4] for i in range(len(file_list))]

# Then get out just the week numbers and 
forecast_nums = [int(i[4::]) for i in forecast_names]
forecast_nums = np.sort(forecast_nums)
forecast_week = np.max(forecast_nums) #current forecast week

bonus_nums = [int(i[4::]) for i in bonus_names]
bonus_nums = np.sort(bonus_nums)

# %%
# setup a dataframe with all zeros for the scoreboard
# use the first summary file to make the name index
temp = pd.read_csv(file_list[0], index_col='name')
scoreboard = pd.DataFrame(data = np.zeros((len(temp),2)), 
                          index = temp.index, 
                          columns=['regular', 'bonus'])

# Setup a weekly scoreboard similar to above
score_weekly = pd.DataFrame(data=np.zeros(len(temp)),
                            index=temp.index,
                            columns=['Total'])

# %%
#calculate the scores
#loop through reading summaries and add in the regular points
#for file in file_list:
for f in range(np.min(forecast_nums), np.max(forecast_nums)+1):
    fname = 'forecast_week' + str(f) +  '_results.csv'
    filetemp = os.path.join('../weekly_results', fname)
    print(filetemp)
    temp=pd.read_csv(filetemp, index_col='name')
    scoreboard['regular'] += temp['1week_points']+ temp['2week_points']

    # add the values to the week table: 
    score_weekly = score_weekly.join(temp['1week_points'])
    score_weekly = score_weekly.rename(
        columns={'1week_points': ('wk' + str(f) + '_1wk.fcst')})
    score_weekly = score_weekly.join(temp['2week_points'])
    score_weekly = score_weekly.rename(
        columns={'2week_points': ('wk' + str(f) + '_2wk.fcst')})

# Add in thte bonus points
#for file in file_listB:
for f in range(np.min(bonus_nums), np.max(bonus_nums)+1):
    fname = 'bonus_week' + str(f) + '.csv'
    filetemp = os.path.join('../weekly_results', fname)
    print(filetemp)

    temp=pd.read_csv(filetemp, index_col='names')
    scoreboard['bonus'] += temp['points']

    # add the values to the week table:
    score_weekly = score_weekly.join(temp['points'])
    score_weekly = score_weekly.rename(
        columns={'points': ('wk' + str(f) + '_bonus')})



scoreboard['total'] = scoreboard['bonus'] + scoreboard['regular']


scoreboard['rank'] = scoreboard.total.rank(method='dense', ascending=False)
scoreboard = scoreboard.sort_values(by='total', ascending=False)
print(scoreboard)

# %%
# Write out the scoreboard
fname='scoreboard_week' + str(forecast_week) + '.csv'
filetemp = os.path.join('../weekly_results', fname)
scoreboard.to_csv(filetemp, index_label='name')

# Write out the scoreboard
fname = 'score_details.csv'
filetemp = os.path.join('../weekly_results', fname)
score_weekly.to_csv(filetemp, index_label='name')

# %%
