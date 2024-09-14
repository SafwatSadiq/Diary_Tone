import streamlit as st
import plotly.express as px
from backend import get_data

dates, pos, neg= get_data()

st.title("Diary Tone")

st.subheader("Positivity")
figure_pos = px.line(x=dates, y=pos, labels={'x':"Date", 'y':"Positivity"})
st.plotly_chart(figure_pos)

st.subheader("Negativity")
figure_neg = px.line(x=dates, y=neg, labels={'x':"Date", 'y':"Negativity"})
st.plotly_chart(figure_neg)