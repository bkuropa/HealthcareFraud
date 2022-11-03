#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Aug 28 20:42:49 2018

@author: eoneil
"""
import pandas as pd
import numpy as np

df=pd.read_csv("/Users/ed/Google Drive/CSDA_1050/Data/df_new2.csv")
fda=pd.read_csv('/Users/ed/Google Drive/CSDA_1050/Data/FDA_ingredients/FDAProducts.csv')
drugs=pd.read_csv("/Users/ed/Google Drive/CSDA_1050/Data/ERLA_DrugName_opiodList.txt", header=None)
drugs.columns=['drugs']


df['flag1']=df.generic_name.isin(drugs['drugs'])
df['flag2']=df.drug_name.isin(drugs['drugs'])
df['flag']=np.where((df['flag1']==True)|  (df['flag2']==True),1,0)
df.to_csv("/Users/ed/Google Drive/CSDA_1050/Data/df_newOpFlag.csv")
#partD_drug = pd.merge(df, fda[['DrugName', 'ActiveIngredient','ApplNo']], how='left', left_on='drug_name', right_on='DrugName') 
                
#drugs['drugs'].apply(lambda x: x.upper(),drugs['drugs'])


#outpt=df.isin(drugs)
#drugs['drugs']=drugs.index
