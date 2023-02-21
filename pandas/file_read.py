

####  Next let's import the Pandas library and rename it as 'pd'. You can either copy and paste and press enter or simply click the code below:

import pandas as pd

#### For our demonstration we will be using the Austin Animal Shelter data set. Let's import the data into a data frame:

df = pd.read_csv('aac_shelter_outcomes.csv')

print(df.head())

#### We will notice that a few of the columns are hidden. We can show all columns by executing the following:

pd.set_option('display.max_columns', None)

pd.set_option('display.max_rows', None)

#### This sets the column and row limits to None. Now let's print the first five rows:

print(df.head())