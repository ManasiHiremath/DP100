# -*- coding: utf-8 -*-
"""
Created on Thu Jun 10 20:34:26 2021

@author: Manasi Hiremath
"""
#import workspace, Datastore and dataset class
from azureml.core import Workspace, Datastore, Dataset
import os

#provide workspace details.
ws= Workspace.from_config(path="C:\\Users\\rajhi\\Manasi\\dp100\\config")

ds_store=Datastore.get(workspace=ws, 
                       datastore_name='azure_ml_sdk_datastore')

##data file 
## provide datastore name and path of the file from 
csv_path=[(ds_store,"train_data/train.csv")]

titanic_data= Dataset.Tabular.from_delimited_files(path=csv_path)
titanic_data=titanic_data.register(workspace=ws, 
                                   name="titanic_data",
                                   create_new_version=True)

