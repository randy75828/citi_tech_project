#          'age',
#         'gender',
#         'monthlyIncome',
#         'essentialExpenses',
#         'personalSavings',
#         'availDownPay',
#         'existingLoan',
#         'locations'

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_excel("testA.xlsx") #open file
<<<<<<< HEAD
=======
df =df[1:]
df.columns = ["datetime","age","gender","monthlyIncome","essentialExpenses","personalSavings","availDownPay",\
                "existingLoan","locations"]
>>>>>>> d0153550ebce7fe1d54dbca6200f1022bbf4b440

date_time_hour=df["datetime"].str.split("-",expand=True)
date = date_time_hour[0] + "-" + date_time_hour[1] + "-" + date_time_hour[2]
time = date_time_hour[3]

df["date"] = date #create new series "date"
df["time"] = time #create new series "time"

input_date = input("Insert date of query (YYYY-MM-DD): ")
parameter = input("Insert parameter to query: ")

def hourly_traffic_by_date(input_date): #Visualizing user traffic by hour on a specific day
    data = df[df["date"]==input_date]
<<<<<<< HEAD
    pd.value_counts(data['time']).plot.bar()
=======
    pd.value_counts(data["time"]).sort_index().plot.bar()
    plt.xlabel("Hour of the Day")
    plt.ylabel("User Traffic per Hour")
>>>>>>> d0153550ebce7fe1d54dbca6200f1022bbf4b440

def user_profile(parameter): #Visualizing a summary of user count categorised by given parameter
    print (df.groupby([parameter]).size().sort_values(ascending=False))
    
def correlation(inputA, inputB): #Plot correlation plot of any two given inputs
    df.plot(kind="scatter",x=inputA, y=inputB)

