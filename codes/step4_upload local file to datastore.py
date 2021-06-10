# -*- coding: utf-8 -*-
"""
Created on Thu Jun 10 22:09:28 2021

@author: Manasi Hiremath
"""
#import required packages
from azureml.core import Workspace, Datastore, Dataset
import os

ws= Workspace.from_config(path="C:\\Users\\rajhi\\Manasi\\dp100\\config")
ds_datastore=Datastore.get(workspace=ws,
                           datastore_name='azure_ml_sdk_datastore')

##upload local file
files_list = [os.getcwd()+"\\Manasi\\dp100\\data\\test.csv"]
ds_datastore.upload_files(files=files_list,
                      target_path="/train_data/",
                      overwrite=True)


# -----------------------------------------------------
# Upload folder or directory to the storage account
# -----------------------------------------------------
ds_datastore.upload(src_dir=os.getcwd()+"\\Manasi\\dp100\\data\\",
                target_path="train_data/titanic_data",
                overwrite=True)




