# Use this script to test the following sample expression:
# Average container humidity = (outer humidity + inner humidity) / 2
# Create a similar script to test your own custom expressions.


# Import Python libraries and packages.
import pandas as pd
import numpy as np
import datetime as dt
import re
from IPython.display import display

# Define the data type of each data item.
numeric_data_items = ['outer_humidity','inner_humidity']
bool_data_items = ['active_status','battery_status']
str_data_items = ['device_name','location']
dt_data_items = ['published_time','generated_time']

# Add device_ID and timestamp. The Analytics Service adds these automatically.
str_data_items.append('deviceid')
dt_data_items.append('_timestamp')

# Define some random data for the data items.
row_count = 5
alpha = list('abcdefghijklmnopqrstuvwxyz')
data = {}
for n in numeric_data_items:
    data[n] = np.random.normal(0,1,row_count)
for b in bool_data_items:
    data[b] = np.random.choice([True,False],row_count)
for s in str_data_items:
    data[s] = np.random.choice(alpha,row_count)
for d in dt_data_items:
    data[d] = []
    for i in list(range(row_count)):
        dt_value = dt.datetime.now() - dt.timedelta(days=np.random.normal(5,1))
        data[d].append(dt_value)

# Generate the random data for the data items and display the data
df = pd.DataFrame(data)
display(df)

# Add an expression.
avg_humidity = "((df['outer_humidity']+df['inner_humidity'])/2)>1"

# Add a function to call the expression.
result = eval(avg_humidity)

# Call the expression and view the output
if not isinstance(result,pd.Series):
    raise TypeError('It looks like something went wrong with your expression. It returned % instead of returning a pandas series. ' %result)
df['avg_humidity'] = result
display(df)
