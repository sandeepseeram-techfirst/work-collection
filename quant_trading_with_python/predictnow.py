# TO BEGIN ANY WORK WITH PREDICTNOW.AI CLIENT, WE START BY IMPORTING AND CREATING A CLASS INSTANCE
from predictnow.pdapi import PredictNowClient
import pandas as pd
api_key = "xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx" 
api_host = "http://12.34.567.890:1000" # our SaaS server
username = "helloWorld"
email = "helloWorld@yourmail.com"
client = PredictNowClient(api_host,api_key)
# You will need to edit this input dataset file path and labelname!
file_path = 'my_amazing_features.xlsx'
labelname = 'Next_day_strategy_return'

import os
 
params = {'timeseries': 'yes', 'type': 'regression', 'feature_selection': 'none', 'analysis': 'none', 'boost': 'gbdt', 'testsize': '0.2', 'weights': 'no', 'eda': 'yes', 'prob_calib': 'no', 'mode': 'train'}

# LET'S CREATE THE MODEL BY SENDING THE PARAMETERS TO PREDICTNOW.AI
response = client.create_model(
 username=username, # only letters, numbers, or underscores
 model_name="test1",
 params=params,
)
 
# LET'S LOAD UP THE FILE TO PANDAS IN THE LOCAL ENVIRONMENT
from pandas import read_csv # If you have the Excel file, replace read_csv with read_excel
from pandas import read_excel
df = read_excel(file_path, engine="openpyxl") # Same here
df.name = "testdataframe" # Optional, but recommended
response = client.train(
 model_name="test1",
 input_df=df,
 label=labelname,
 username=username,
 email=email,
 return_output=False,
)
print("FANTASTIC! YOUR FIRST-EVER MODEL TRAINING AT PREDICTNOW.AI HAS BEEN COMPLETED!")
print(response)
# User can now examine the train/test sets results from the model by calling the getresult function (and providing the name of the model that resides on Predictnow.ai server
status = client.getstatus(username=username, train_id=response["train_id"])
if status["state"] == "COMPLETED":
 response = client.getresult(

model_name="test1",
 username=username,
  )
  import pandas as pd
  predicted_targets_cv = pd.read_json(response. predicted_targets_cv)
  print("predicted_targets_cv")
  print(predicted_targets_cv)
  predicted_targets_test = pd.read_json(response. predicted_targets_test)
  print("predicted_targets_test")
  print(predicted_targets_test)
  performance:metrics = pd.read_json(response. performance:metrics)
  print("performance:metrics")
  print(performance:metrics)

# # Now we can make LIVE predictions for many combinations of the parameters by populating many rows in the example_input_live.csv file with these parameter combinations
if status["state"] == "COMPLETED":
  df = read_csv("example_input_live.csv") # Input data for live prediction
  df.name = "myfirstpredictname" # optional, but  recommended

 