#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Aug 24 10:38:57 2018

@author: eoneil
"""

#This is a loop takes merged health data and banned prescribers, and makes a good subscriber file.
#There is the same number of good and bad prescribers for a given year, with all prescriptions from eacn in the respective
#goodpeoplemerge and badpeoplemerge files.
import numpy as np
import pandas as pd
#for x in range(13,17):
for x in range(15,17):

    #generate file names
    fname4='/Users/ed/Google Drive/CSDA_1050/Data/PartDPrescriber/PartD_Prescriber_PUF_NPI_Drug_'+str(x)+'_goodpeoplemerge.txt'
    fname3='/Users/ed/Google Drive/CSDA_1050/Data/PartDPrescriber/PartD_Prescriber_PUF_NPI_Drug_'+str(x)+'_badpeoplemerge.txt'
    fname2='/Users/ed/Google Drive/CSDA_1050/Data/PartDPrescriber/PartD_Prescriber_PUF_NPI_Drug_'+str(x)+'_merge.txt'

    #load data
    partDBad=pd.read_csv(fname3, sep=',')
    partDall=pd.read_csv(fname2, sep=',')
    #how many unique bad prescribers
    totaluniqueBad=partDBad.npi.nunique()
    #find good prescribers
    good=partDall[partDall["EXCLDATE"].isnull()]
    uniqueGood=good.npi.unique()
    totaluniqueGood=good.npi.nunique()
    #create an index of good subscribers the same lenght as the bad ones
    random_index = np.random.choice(uniqueGood, totaluniqueBad)
    #find all prescriptions from good subscribers
    partDGood=partDall[partDall.npi.isin(random_index)]
    partDGood.to_csv(fname4)