import time
import streamlit as st
from styles import styles
from streamlit_geolocation import streamlit_geolocation
from utils import get_weather_details
from datetime import datetime
from styles import styles


st.set_page_config(
    page_title="Weather App", 
    page_icon="🌦️", 
    layout="centered"
)

location = streamlit_geolocation()
print(location)

if location['latitude']:
    response = get_weather_details(location['latitude'], location['longitude'])
    
    if isinstance(response, str):
        st.error(response)
        time.sleep(5)
        st.rerun()


    #*  Data
    weather = response['weather'][0]['main']
    city = f"{response['name']}, {response['sys']['country']}"
    temperature = f"{response['main']['temp']}°c"
    sunrise = datetime.fromtimestamp(response['sys']['sunrise']).strftime('%I:%M:%S %p')
    sunset = datetime.fromtimestamp(response['sys']['sunset']).strftime('%I:%M:%S %p')
    wind_speed = f"{response['wind']['speed']} m/s"
    humidity = f"{response['main']['humidity']} %"
    icon = f"https://openweathermap.org/img/wn/{response['weather'][0]['icon']}@2x.png"

    print(icon)


    st.image(icon, width=100)

    with st.container(key="container"):
        st.title(city, anchor="city")
        st.subheader(weather + " | " + temperature)
    
        col1, col2 = st.columns(2)
        col3, col4 = st.columns(2)

        with col1:
            icon, text = st.columns(2)
            icon.markdown("<span class='material-symbols-outlined'>waves</span>", True)
            text.markdown(f"{humidity}  \nHumidity")

        with col2:
            icon, text = st.columns(2)
            icon.markdown("<span class='material-symbols-outlined'>air</span>", True)
            text.markdown(f"{wind_speed}  \nWind Speed")
        
        with col3:
            icon, text = st.columns(2)
            icon.markdown("<span class='material-symbols-outlined'>water_lux</span>", True)
            text.markdown(f"{sunrise}  \nSunrise")
        
        with col4:
            icon, text = st.columns(2)
            icon.markdown("<span class='material-symbols-outlined'>wb_twilight</span>", True)
            text.markdown(f"{sunset}  \nSunset")




    st.markdown(styles, unsafe_allow_html=True)

   



