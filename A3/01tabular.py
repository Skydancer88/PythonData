# Relevant imports
import shutil
import seaborn as sns
import pandas as pd
import numpy as np
import wget
import os

# Download and extract the .csv file if does not exist
if os.path.isfile('fryziggafl.csv') == False:
    shutil.unpack_archive('fryziggafl.zip')

# Load the .csv file into a pandas dataframe named afl
afl = pd.read_csv('fryziggafl.csv')

# Filter to just use matches post 2000, because there is A LOT of data
# You can adjust this to use even less of the data while you are 
#   prototyping
afl_post_2000 = afl[(afl['match_date'] > '2000-01-01')]
print (afl_post_2000)
