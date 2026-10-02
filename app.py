import streamlit as st
import pandas as pd
from dbhelper import DB
import plotly.graph_objects as go
import plotly.express as px

db = DB()

st.sidebar.title('Flights Analysis')

user_option = st.sidebar.selectbox('Menu', ['Select One', 'Check Flights', 'Analytics'])

if user_option == 'Check Flights':
    st.title('Check Flights')

    col1, col2 = st.columns(2)
    city = db.fetch_city_name()

    with col1:
        source = st.selectbox('Source', sorted(city))
    with col2:
        destination = st.selectbox('Destination', sorted(city))

    if st.button('Search'):
        results = db.fetch_all_flights(source, destination)
        if results:
            df = pd.DataFrame(
                results,
                columns=['Airline', 'Route', 'Departure', 'Duration', 'Price'],
            )
            st.dataframe(df, use_container_width=True)
        else:
            st.warning('No flights found for this route.')

elif user_option == 'Analytics':
    st.title('Analytics')

    airline, frequency = db.fetch_airline_frequency()
    fig = go.Figure(
        go.Pie(
            labels=airline,
            values=frequency,
            hoverinfo='label+percent',
            textinfo='value',
        )
    )
    st.header('pie chart')
    st.plotly_chart(fig, use_container_width=True)

    city, frequency1 = db.busy_airport()
    fig = go.Figure(
        go.Bar(
            x=city,
            y=frequency1,
            text=frequency1,
            textposition='auto',
        )
    )
    st.header('Busy Airports')
    st.plotly_chart(fig, use_container_width=True)

    date, frequency2 = db.daily_frequency()
    fig = go.Figure(
        px.line(
            x=date,
            y=frequency2,
            text=frequency2,
        )
    )
    st.header('daily flights')
    st.plotly_chart(fig, use_container_width=True)

else:
    st.title('Welcome to Flights Analysis')
