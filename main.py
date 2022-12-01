import pandas as pd
import streamlit as st
import plotly.express as px
from PIL import Image
import openpyxl

st.set_page_config(page_title='Financial Development Plan')
st.header('FDP 2021')
st.subheader('Dashboard')

### ---LOAD DATAFRAME
excel_file = "/Users/sizwekekana/Desktop/FDP_2021.xlsx"
sheet_name = 'Covenants Summary'
sheet_name1 = "Ratio summary"
st.subheader('Covenants Summary')
df = pd.read_excel(excel_file, sheet_name=sheet_name, usecols='A:Q', header=2)

st.subheader('Ratio Summary')
df_ratio = pd.read_excel(excel_file, sheet_name=sheet_name1, usecols='B:U', header=1)
df.fillna("", inplace=True)
df_ratio.fillna("", inplace=True)
st.dataframe(df)
st.dataframe(df_ratio)

# pie_chart = px.pie(df_ratio, title='Ratios', values='Actual', names='Financial ratios')
# st.plotly_chart(pie_chart)
ratio_summary = df_ratio['Financial ratios'].unique().tolist()
ratio_selection = st.multiselect('Financial ratios:', ratio_summary, default=ratio_summary)

mask = (df_ratio['Financial ratios'].isin(ratio_selection))
number_of_result = df_ratio[mask].shape[0]
st.markdown(f'*Available Results:{number_of_result}*')

df_group = df_ratio[mask].groupby(by=['Financial ratios']).count()[['Actual']]
df_group = df_group.rename(columns={'Actual': 'Percentages'})
df_group = df_group.reset_index()

bar_chart = px.bar(df_group, x='Financial ratios', y='Percentages', text='Percentages',
                   color_discrete_sequence=['#F63366'] * len(df_group), template='plotly_white')

st.plotly_chart(bar_chart)
