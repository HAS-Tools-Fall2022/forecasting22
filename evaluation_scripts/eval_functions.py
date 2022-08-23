# %%
from datetime import datetime
import pandas as pd
import os
import numpy as np
from glob import glob

# %%
# Forecast Functions Week 8

def getLastNames():
    """Get classlist of last names.
    ---------------------------------
    This function takes no input and returns the list of
    students' last names in the class.  This makes it easy to
    access the class list from any script.
    ---------------------------------
    Parameters:
    none
    ----------------------------------
    Outputs:
    lastNames = list of strings
                contains students's last names
    """
    lastNames = ['Arden', 'Bettis', 'Boyd', 'Carver', 'Dyer',
                 'Giralte', 'Hoopes', 'Morales', 'Schlottman',
                 'Serrano', 'XiZhang', 'XuZhang', 'Zhong']
    return lastNames


def getFirstNames():
    """Get classlist of first names.
    ---------------------------------
    This function takes no input and returns the list of
    students' first names in the class.  This makes it easy to
    access the class list from any script.
    ---------------------------------
    Parameters:
    none
    ----------------------------------
    Outputs:
    firstNames = list of strings
                 contains student's first names
    """
    firstNames = ['Josh', 'Sierra', 'Connal', 'Monique', 'Kevin', 
                   'Gigi', 'Andrew', 'David', 'Jason', 
                   'Stephanie', 'Xingyu', 'Xueyan', 'Xiang']
    return firstNames


def weekDates(weekNumber):
    """Compute the one and two week forecasts using model.
    ---------------------------------
    This function takes no input and returns the list of
    students' first names in the class.  This makes it easy to
    access the class list from any script.
    ---------------------------------
    Parameters:
    weekNumber = integer
                 number indicating the week of the semester
    ----------------------------------
    Outputs:
    startDate = string
                contains start date of forecast week
    stopDate = string
               contains end date of forecast week
    """

    datefile = os.path.join('..', 'Foercast_Dates.csv')
    forecast_dates = pd.read_csv(datefile,
                                 index_col='forecast_week')
    startDate = forecast_dates.loc[weekNumber, 'start_date']
    stopDate = forecast_dates.loc[weekNumber, 'end_date']

    #Make formated versions for USGS API
    start_temp = datetime.strptime(startDate, '%m/%d/%y')
    start_format = start_temp.strftime("%Y-%m-%d")
    end_temp = datetime.strptime(stopDate, '%m/%d/%y')
    end_format = end_temp.strftime("%Y-%m-%d")

    return startDate, stopDate, start_format, end_format


def write_bonus(bonus_names, all_names, weeknum):
    """" This function needs week forecast (weeknum) and the
    list of student's names (bonus_names) you want to give bonus
    points for this week """
    bonus = pd.DataFrame(data=np.zeros(len(all_names)),
                         index=all_names,
                         columns=['points'])
    bonus.index.name = 'names'
    bonus.loc[bonus_names, 'points'] = 1
    filename = 'bonus_week' + str(weeknum) + '.csv'
    bonus_file = os.path.join('../../weekly_results', filename)
    bonus.to_csv(bonus_file)
    print("Bonus File Written")


def student_csv(lastname):
    """ Reads the .cvs student file as a dataframe.
    ---------------------------------
    Parameters:
    lastname = string
               list of student's last name.
    ---------------------------------
    Returns:
    file_df = DataFrame
              contains student's forecast entries.
    """
    filename = lastname + '.csv'
    filepath = os.path.join('..', 'forecast_entries', filename)
    print(filepath)
    file_df = pd.read_csv(filepath, index_col='Forecast #')
    return file_df


def simpleRMSE(prediction, observation, decimals):
    """ Calculates the Root Mean Square Error (RMSE) of a dataset.
    ---------------------------------
    Parameters:
    prediction = DataFrame, array or list
                 A prediction dataset.
    observation = DataFrame, array or list
                 A observation dataset with the same length
                 that the prediction dataset.
    decimals = Integer
               Number of decimals in the result.
    ---------------------------------
    Returns:
    rmse = Float
    """
    rmse = round((((prediction - observation) ** 2).mean()
                 ** 0.5), decimals)
    return rmse


# %%
