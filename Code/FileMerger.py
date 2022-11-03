#This is a loop that merges the health data and saves off banned prescribers.
import pandas as pd
for x in range(13,17):
    
    #generate file names
    fname='/Users/ed/Google Drive/CSDA_1050/Data/PartDPrescriber/PartD_Prescriber_PUF_NPI_Drug_'+str(x)+'.txt'
    fname2='/Users/ed/Google Drive/CSDA_1050/Data/PartDPrescriber/PartD_Prescriber_PUF_NPI_Drug_'+str(x)+'_merge.txt'
    fname3='/Users/ed/Google Drive/CSDA_1050/Data/PartDPrescriber/PartD_Prescriber_PUF_NPI_Drug_'+str(x)+'_badpeoplemerge.txt'
    
    #load data
    partD=pd.read_csv(fname, sep='\t')
    leie=pd.read_csv('/Users/ed/Google Drive/CSDA_1050/Data/LEIE/UPDATED.csv')
    fda=pd.read_csv('/Users/ed/Google Drive/CSDA_1050/Data/FDA_ingredients/FDAProducts.csv')

    #generate unique drug names     
    prtDdrugs=partD.drug_name.unique()
    prtDdrugs.sort()
    prtDdrugs
    
        
    prtDdrugs_g=partD.generic_name.unique()
    prtDdrugs_g.sort()
    prtDdrugs_g
    
    fdaDrugs=fda.DrugName.unique()
    
    fda_1=fda[['DrugName','ActiveIngredient']]
    fda_2=fda_1.drop_duplicates(keep=False)
    
    #Merge prescription and active ingredient
    partD_drug = pd.merge(partD, fda_2[['DrugName', 'ActiveIngredient']], how='left', left_on='drug_name', right_on='DrugName')                 

    #focus on LEIE since 2012
    leie.year=pd.to_datetime(leie['EXCLDATE'].astype(str), format='%Y%m%d').dt.year
    newleie=leie[leie.year>2012]
    newleie=newleie.dropna(subset=['LASTNAME'])
    
    #make merge keys for prescrptions and banned subscriber list
    partD_drug["key"]=partD_drug["nppes_provider_last_org_name"]+partD_drug["nppes_provider_first_name"]+partD_drug["nppes_provider_city"]
    newleie["key"]=newleie["LASTNAME"]+ newleie["FIRSTNAME"]+ newleie["CITY"]
    
    
    #merge
    merge_partD=pd.merge(partD_drug, newleie, on='key', how='left')
    
    list(merge_partD)
    list(partD_drug)
    merge_partD.head()
   
    #save
    merge_partD.to_csv(fname2)
    badpeople=merge_partD.dropna(subset=["LASTNAME"])
    badpeople.to_csv(fname3)
