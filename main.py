import streamlit as st
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd

import kagglehub
from kagglehub import KaggleDatasetAdapter

st.title("Data Visualisation of Virat Kohli's Career to help him improve his game in the future")

file_path = "Virat Kohli DataSet.csv"

data_file_cric = kagglehub.load_dataset(
  KaggleDatasetAdapter.PANDAS,
  "amirmotefaker/virat-kohli-dataset",
  file_path,
)

print(data_file_cric.head())