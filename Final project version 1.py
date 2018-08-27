
# coding: utf-8

# In[85]:


import numpy as np
import pandas as pd
import os 
import copy


# In[90]:


path='/home/umanagendramalla/Desktop/Final project/'

os.chdir(os.path.join(path,'Input files'))


# In[91]:


##na removal by columns:
##na removal by rows
data=pd.read_csv('clp_classification.csv')


# In[94]:


##dropped columns when null are more than threshold  (0.3)
def na_handling_col_removal(df,threshold):
    for col in df.columns:
        print(df.shape)
        col_data=df[col].isna().sum()/len(df[col])
        if col_data>=threshold:
            df.drop(col,axis=1,inplace=True)
    
    if(threshold<1):
        threshold=np.round(threshold*len(df.columns))
        df.dropna(axis=0,thresh=len(df.columns)-threshold,inplace=True)
            
os.chdir(os.path.join(path,'Layer1'))
data.to_csv('row_col_drop.csv')

        
        

