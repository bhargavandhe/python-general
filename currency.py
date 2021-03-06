"""Problem statement: 
   Date: 06/10/20
   Author: Bhargav Andhe"""
import json

import matplotlib.pyplot as plt
from requests import *

link = 'https://api.exchangeratesapi.io/history?start_at=2018-01-01&end_at=2018-01-10&base=USD'
data = json.loads(get(link).text)
dates = sorted([date for date in data['rates']])

x = [date for date in dates]
y1 = [data['rates'][date]['INR'] for date in dates]
y2 = [data['rates'][date]['RUB'] for date in dates]

plt.title('Currency converter')
plt.xlabel('Dates')
plt.ylabel('Rates')
plt.plot(x, y1)
plt.plot(x, y2)
plt.show()
