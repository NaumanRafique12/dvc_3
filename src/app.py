import pandas as pd
import numpy as np
import os

df = pd.read_csv('https://raw.githubusercontent.com/araj2/customer-database/master/Ecommerce%20Customers.csv')

d = pd.DataFrame()
d['second'] = df[['Length of Membership']]

d.to_csv(os.path.join('data','customer.csv'))