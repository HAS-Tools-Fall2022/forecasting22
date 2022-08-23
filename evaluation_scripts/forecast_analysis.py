
# %%
import pandas as pd
import seaborn as sns
import numpy as np
import matplotlib.pyplot as plt
import os
import eval_functions as ef

# %%
forecast_week = 2 #CHANGE to reflect current week

# %%
station_id = "09506000"

# list of students in the class
# get lists using functions in eval_functions.py
names = ef.getLastNames()
firstnames = ef.getFirstNames()
nstudent = len(names)

# get start and stop dates using functions in eval_functions.py
dates = ef.weekDates(forecast_week)
start_date = dates[0]
stop_date = dates[1]

print("Evaluating forecasts up to",  stop_date)

# %%
# Reading in all of the student forecasts 
# making two empty arrays to  hold the forecasts
forecasts_1 = np.zeros([nstudent, forecast_week])  # 1wk forecast for this week
forecasts_2 = np.zeros([nstudent, forecast_week])  # 2wk forecasts for this week

# Reading the individual student forecast csvs and making dataframe
for i in range(nstudent):
    temp = ef.student_csv(names[i])
    for n in range(1, forecast_week+1):
        forecasts_1[i, n-1] = temp.loc[(n), '1week']
        forecasts_2[i, n-1] = temp.loc[(n), '2week']

# compiling into data frames you can use for graphing
weekly_forecast1w = pd.DataFrame({}, index=firstnames) #forecasts issued with 1 week lead time
weekly_forecast2w = pd.DataFrame({}, index=firstnames) #forecasts issued with 2 weeks lead time

for i in range(forecast_week):
    weekly_forecast1w.insert(i, 'Week %s' % (i+1), forecasts_1[:, i], True)
    weekly_forecast2w.insert(i, 'Week %s' % (i+2), forecasts_2[:, i], True)

#NOTE: the coumn names refer to the week the forecast is issued for
# therfore the weekly_forecast2w first column is for week2 

# %%
# Read in the observed flows
weekly_flows = pd.read_csv("../weekly_results/weekly_observations.csv")

# %%
# Make boxplots of the forecasts over time 
#Create a combined and melted dataframe of the 1 and 2 week forecasts
week1plot = weekly_forecast1w.assign(Leadtime='1 week outlook')
week2plot = weekly_forecast2w.assign(Leadtime='2 week outlook')
cdf = pd.concat([week1plot, week2plot])
mdf = pd.melt(cdf, id_vars=['Leadtime'], var_name=['week'])
print(mdf.head())

#Plot
fig, ax = plt.subplots()
my_pal = {"1 week outlook": "lightgreen", "2 week outlook": "lightblue"}
ax = sns.boxplot(x="week", y="value", hue="Leadtime", data=mdf, palette=my_pal, 
                linewidth=0.3)
ax.set_xlabel('Forecast Week')
ax.set_ylabel('Flow (cfs)')
plt.scatter((weekly_flows.index - 0.2), weekly_flows['observed'], marker='*', s=100, color='darkred')

plt.show()

# Save the plot to a file
filename = 'Forecast_Boxplots_week' + str(forecast_week) + '.png'
filepath = os.path.join('../weekly_plots', filename)
fig.savefig(filepath)


# %%
# Read in the scoreboards to make a timeseries plot of the rankings

#create an empty dataframe
rankings = np.zeros([nstudent, forecast_week])  # 1wk forecast for this week

#loop through and read in the rankings for every week
for f in range(1, (forecast_week+1)):
    fname = 'scoreboard_week' + str(f) + '.csv'
    filetemp = os.path.join('../weekly_results', fname)
    temp = pd.read_csv(filetemp, index_col='name')

    if f ==1:
        ranks = temp

        print(ranks)
    else:
        print('here')
        ranks = ranks.join(temp['rank'], how='inner', rsuffix=('_'+str(f)))
        
#get rid of the extra columns from the first week     
ranks = ranks.rename(columns={'rank':'rank_1'})
ranks = ranks.drop(['regular', 'bonus', 'total'], axis=1)

#transpose the dataframe to make plotting easier
ranks_transpose = ranks.transpose()

#Plot the ranks over time
fig, ax = plt.subplots()
ranks_transpose.plot(kind='line', ax=ax, style='.-', 
                    xticks=range(forecast_week))
ax.set_xlabel("Forecast Week")
ax.set_xticks(range(forecast_week))
ax.set_xticklabels(range(1, forecast_week+1))
ax.set_ylabel("Class Ranking")
ax.set_title('Forceast Competition Rankings')
ax.invert_yaxis()
plt.legend(bbox_to_anchor=(1.05, 1.0), loc='upper left')

# Save the plot
filename = 'RankingEvolution_week' + str(forecast_week) + '.png'
filepath = os.path.join('../weekly_plots', filename)
fig.savefig(filepath)



# %%
