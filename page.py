import cv2
import numpy as np
import tensorflow as tf
import os
from datetime import datetime
import streamlit as st
import xgboost as xgb
import sklearn

st.header("Oculous")
name = st.text_input("Enter your Name: ", key="name")

if name:
    with open("name.txt", "w") as file:
        file.write(name)
        st.success("Name stored successfully!")

st.header("write the path to your dataset")
dataset = st.text_input("Path: ", key="dataset")

