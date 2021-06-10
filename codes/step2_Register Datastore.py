# -*- coding: utf-8 -*-
"""
Created on Thu Jun 10 19:36:30 2021

@author: Manasi Hiremath
"""
#import Workspace and Datastore class
from azureml.core import Workspace, Datastore
import os

ws= Workspace.from_config(path=os.getcwd()+"/config")

ds= Datastore.register_azure_blob_container(workspace=ws, 
                                            datastore_name='azure_sdk_datastore',
                                            container_name="azuremlstacc001", 
                                            account_name="azuresdkblob",
                                            account_key="VmMnM20U1JuiPd/yDdI5y2ASUt7Lgie+Rllqt9qy3QZeJ4cGZ06b+BrXQE3XvHwNhxwROxbzoY7ROlMN1kMPDQ==")
