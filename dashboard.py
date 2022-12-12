import pandas as pd
import streamlit as st
import matplotlib.pyplot as plt
import plotly.express as px
import plotly.graph_objects as go
from urllib.request import urlopen
import json
from copy import deepcopy
from plotly.subplots import make_subplots


st.title("Towards AI for humanitarian actions: exploring data on populations displacement")


###############Line Map############################


st.header("Monthwise distribution of refugees arriving in Ireland")
df_refugees1 = pd.read_csv('Downloads/chart33.csv')

left_column1, right_column1 = st.columns([1, 1])

options = ['All', 'Ukrainians', 'All other refugees'] 
select1 = left_column1.selectbox("Choose the month", options)

df_refugees = df_refugees1.groupby('Month', as_index=False).sum()

if select1 == 'All':
    trace1 = px.line(x = df_refugees['Month'], y = df_refugees['All'], labels={'x':'Months', 'y':'All refugees'})
    st.plotly_chart(trace1)
elif select1 == 'Ukrainians':
    trace2 = px.line(x = df_refugees['Month'], y = df_refugees['Ukraine'], labels={'x':'Months', 'y':'Ukrainian'})
    st.plotly_chart(trace2)
elif select1 == 'All other refugees':
    trace2 = px.line(x = df_refugees['Month'], y = df_refugees['Other'], labels={'x':'Months', 'y':'All Other nationalities with protected status'})
    st.plotly_chart(trace2)


###############Choropleth Map############################


with open("Downloads/ireland.geojson") as response:
    geo = json.load(response)

df_counties = pd.read_csv('Downloads/counties.csv')

# Add title and header
st.header("Division of Refugees across counties in Ireland")

# Geographic Map
fig = go.Figure(
    go.Choroplethmapbox(
        geojson=geo,
        locations=df_counties.Counties,
        featureidkey="properties.name",
        z=df_counties.Count,
        colorscale="sunsetdark",
        # zmin=0,
        # zmax=500000,
        marker_opacity=0.5,
        marker_line_width=0,
    )
)


fig.update_layout(
    mapbox_style="carto-positron",
    mapbox_zoom=6,
    mapbox_center={"lat": 53.15, "lon": -7.69},
    width=800,
    height=600,
)
fig.update_layout(margin={"r": 0, "t": 0, "l": 0, "b": 0})
st.plotly_chart(fig)



###############Stack Bar Graph Map############################

df_months = pd.read_csv('Downloads/chart2.csv')

st.header("Division across age group and gender")
left_column, right_column = st.columns([1, 1])

# Widgets: selectbox
months = ['March', 'April', 'May', 'April', 'May', 'June', 'July', 'September', 'October', 'November', 'All']
select = left_column.selectbox("Choose the month", months)

if select == 'March':
    fig1 = px.bar(df_months,x='Age Group', y='March', color='Sex',height=400, width=700)
    st.plotly_chart(fig1)
elif select =='April':
    fig2 = px.bar(df_months,x='Age Group', y='April', color='Sex',height=400, width=700)
    st.plotly_chart(fig2)
elif select =='May':
    fig3 = px.bar(df_months,x='Age Group', y='May', color='Sex',height=400, width=700)
    st.plotly_chart(fig3)
elif select =='June':
    fig4 = px.bar(df_months,x='Age Group', y='June', color='Sex',height=400, width=700)
    st.plotly_chart(fig4)
elif select =='July':
    fig5 = px.bar(df_months,x='Age Group', y='July', color='Sex',height=400, width=700)
    st.plotly_chart(fig5)
elif select =='August':
    fig6 = px.bar(df_months,x='Age Group', y='August', color='Sex',height=400, width=700)
    st.plotly_chart(fig6)
elif select =='September':
    fig7 = px.bar(df_months,x='Age Group', y='September', color='Sex',height=400, width=700)
    st.plotly_chart(fig7)
elif select =='October':
    fig8 = px.bar(df_months,x='Age Group', y='October', color='Sex',height=400, width=700)
    st.plotly_chart(fig8)
elif select =='November':
    fig9 = px.bar(df_months,x='Age Group', y='November', color='Sex',height=400, width=700)
    st.plotly_chart(fig9)
else:
    fig10 = px.bar(df_months,x='Age Group', y='All', color='Sex',height=400, width=700)
    st.plotly_chart(fig10)



###############Pie Chart Map############################


st.header("Relationship status of refugees in Ireland")

df_pie = pd.read_csv('Downloads/chart4.csv')

left_column2, right_column2 = st.columns([1, 1])

relationships_months = ['May', 'June', 'July', 'August', 'September', 'Total'] 
select2 = left_column2.selectbox("Choose the month", relationships_months)

if select2 == 'May':
    fig11 = px.pie(df_pie, values='May', names='Relationship', title='Population of European continent')
    st.plotly_chart(fig11)
elif select2 == 'June':
    fig12 = px.pie(df_pie, values='June', names='Relationship', title='Population of European continent')
    st.plotly_chart(fig12)
elif select2 == 'July':
    fig13 = px.pie(df_pie, values='July', names='Relationship', title='Population of European continent')
    st.plotly_chart(fig13)
elif select2 == 'August':
    fig13 = px.pie(df_pie, values='August', names='Relationship', title='Population of European continent')
    st.plotly_chart(fig13)
elif select2 == 'September':
    fig13 = px.pie(df_pie, values='September', names='Relationship', title='Population of European continent')
    st.plotly_chart(fig13)
elif select2 == 'Total':
    fig13 = px.pie(df_pie, values='Total', names='Relationship', title='Population of European continent')
    st.plotly_chart(fig13)






