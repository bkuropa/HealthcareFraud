#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Aug 24 14:32:13 2018

@author: eoneil
"""
import pandas as pd
#make empty dataframe populated with real data
fname='/Users/ed/Google Drive/CSDA_1050/Data/superframe.csv'
superframe=pd.read_csv(fname, sep=',')

colnm=list(superframe)

colAgg={'ADDRESS':'first',
        'ActiveIngredient':'first',
        'BUSNAME':'first',
        'DOB':'first',
        'DrugName':'first',
        'EXCLDATE':'first',
        'EXCLTYPE':'first',
        'GENERAL':'first',
        'REINDATE':'first',
        'WAIVERDATE':'first',
        'WVRSTATE':'first',
        'ZIP':'first',
        'description_flag':'first',
        'drug_name':'first',
        'generic_name':'first',
        'good':'first',
        'infoYear':'first',
        'key':'first',
        'npi':'first',
        'nppes_provider_city':'first',
        'nppes_provider_first_name':'first',
        'nppes_provider_last_org_name':'first',
        'nppes_provider_state':'first',
        'specialty_description':'first',
        'total_30_day_fill_count':'sum',
        'total_claim_count':'sum',
        'total_day_supply':'sum',
        'total_drug_cost':'sum',
        }



df_new = superframe.groupby(['npi', 'generic_name']).aggregate(colAgg)#.reindex(columns=superframe.columns)
#result.groupby(['key', 'generic_name'])['total_claim_count'].agg('sum')

#.reindex(columns=df.columns)
df_new.to_csv('/Users/ed/Google Drive/CSDA_1050/Data/DataCollaspedbyGenericPerDoctor.csv')


#unused attempt at a zip 
#agglist=[:'first','first','first','first','first',
#         'first','first','first','first','first',
##         'first','first','first','first','first',
  #       'first','first','first','first','first',
#         'first','first','first','first','first',
#         'first','first','first','first','first',
#         'first','first','first','first','first',
#         'first','first','first','first','first',
#         'first','sum','first',:'sum','first',
#         'sum','first']

#colAgg=dict(zip(colnm,agglist))


#entriesToRemove = ('key', 'bene_count_ge65','bene_count_ge65_suppress_flag',
 #                  'total_claim_count_ge65','ge65_suppress_flag',
 ##                  'total_30_day_fill_count_ge65','total_day_supply_ge65',
 #                  'total_drug_cost_ge65','bene_count','generic_name','npi')
#for k in entriesToRemove:
#    colAgg.pop(k, None)