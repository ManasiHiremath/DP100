# -*- coding: utf-8 -*-
"""
Created on Fri Jun 11 21:34:37 2021

@author: Manasi Hiremath
"""
from azureml.core import Workspace, Datastore, Dataset, Experiment,Run
import os

#get workspace and required details
ws= Workspace.from_config(path="C:\\Users\\rajhi\\Manasi\\dp100\\config")
ds_datastore= Datastore.get(ws,'azure_ml_sdk_datastore')
Data = Dataset.get_by_name(ws,name='titanic_data')

## Create Experiment
experiment=Experiment(workspace=ws,
               name='titanic_exp')

##Run an experiment
run=experiment.start_logging(snapshot_directory=None) ## specify snapshot_directory as none else experiment will keep on running
run.log(name='task', value="hi")
## Complete an experiment
run.complete()

