# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
# Call Wokspace class to create ML workspace
from azureml.core import Workspace
import os

ws=Workspace.create(name='azureml-sdk-ws',
                    subscription_id='****************************',
                    resource_group='dp100-train',
                    create_resource_group=True,
                    location='eastus2'
                    )

ws.write_config(path=os.getcwd()+"/config")
