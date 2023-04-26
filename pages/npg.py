import streamlit as st
import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt

st.title('🚗MPG 자동차연비🚗')

st.markdown("# MPG 🚗")
st.sidebar.markdown("# MPG 🚗")

# mpg = sns.load_dataset('mpg')
mpg = pd.read_csv("https://raw.githubusercontent.com/mwaskom/seaborn-data/master/raw/mpg.csv")

st.sidebar.header('Select Year')
selected_year = st.sidebar.selectbox('Year',
   list(reversed(range(mpg.model_year.min(),mpg.model_year.max())))
   )

# Sidebar - origin
sorted_unique_origin = sorted(mpg.origin.unique())
selected_origin = st.sidebar.multiselect('origin', sorted_unique_origin, sorted_unique_origin)


if selected_year > 0 :
   mpg = mpg[mpg.model_year == selected_year]

if len(selected_origin) > 0:
   mpg = mpg[mpg.origin.isin(selected_origin)]

st.dataframe(mpg)

st.line_chart(mpg["mpg"])

st.bar_chart(mpg["mpg"])

fig, ax = plt.subplots()
sns.barplot(data=mpg, x="origin", y="mpg").set_title("origin 별 자동차 연비")
st.pyplot(fig)
