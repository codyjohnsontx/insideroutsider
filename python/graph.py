#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
import plotly.graph_objs as go
from plotly.subplots import make_subplots


# In[3]:


amdData = pd.read_csv('csv/amd_trades_data (2).csv')
nvidiaData=pd.read_csv('csv/nvidia_trades_data.csv')
txData=pd.read_csv('csv/nvidia_trades_data.csv')


# In[4]:


def process_data(df):
    df['Transaction Date'] = pd.to_datetime(df['Transaction Date'], format='%b. %d, %Y')
    grouped = df.groupby(['Transaction Date', 'Transaction Type']).size().unstack(fill_value=0)
    return grouped.index, grouped.get('Purchase', 0), grouped.get('Sale', 0)


# In[5]:


#Process datasets using process_data
amdDate, amdBuy, amdSell = process_data(amdData)
nvidiaDate, nvidiaBuy, nvidiaSell = process_data(nvidiaData)
txDate, txBuy, txSell = process_data(txData)


# In[6]:


#Create subplots
fig = make_subplots(rows=3, cols=1, subplot_titles=('AMD Transactions', 'NVIDIA Transactions', 'Texas Instruments Transactions'))


# In[7]:


#Add AMD data
fig.add_trace(go.Scatter(x=amdDate, y=amdBuy, mode='lines+markers', name='AMD Buy', marker=dict(color='blue')), row=1, col=1)
fig.add_trace(go.Scatter(x=amdDate, y=amdSell, mode='lines+markers', name='AMD Sell', marker=dict(color='red')), row=1, col=1)

#Add NVIDIA
fig.add_trace(go.Scatter(x=nvidiaDate, y=nvidiaBuy, mode='lines+markers', name='NVIDIA Buy', marker=dict(color='blue')), row=2, col=1)
fig.add_trace(go.Scatter(x=nvidiaDate, y=nvidiaSell, mode='lines+markers', name='NVIDIA Sell', marker=dict(color='red')), row=2, col=1)

#Add Texas Instruments
fig.add_trace(go.Scatter(x=txDate, y=txBuy, mode='lines+markers', name='Texas Instruments Buy', marker=dict(color='blue')), row=3, col=1)
fig.add_trace(go.Scatter(x=txDate, y=txSell, mode='lines+markers', name='Texas Instruments Sell', marker=dict(color='red')), row=3, col=1)

#Update layout
fig.update_layout(height=900, width=800, title_text="Quantity of Trades for Semiconductor Companies", showlegend=True)
fig.update_xaxes(title_text="Date", row=3, col=1)
fig.update_yaxes(title_text="Number of Transactions", col=1)

#Show plot
fig.show()


# In[ ]:




