import streamlit as st
#install options_menu - pip install streamlit option_menu
from streamlit_option_menu import option_menu

import application, about, homepage

st.set_page_config(
        page_title="Forecasting and Prediction",
)



class MultiApp:

    def __init__(self):
        self.apps = []

    def add_app(self, title, func):

        self.apps.append({
            "title": title,
            "function": func
        })

    def run():
        # app = st.sidebar(
        with st.sidebar:        
            app = option_menu(
                menu_title='Navigation Menu',
                options=['Homepage','App','About Us'],
                icons=['house-fill','info-circle-fill','info-circle-fill'],
                menu_icon='chat-text-fill',
                default_index=0,
                styles={
                    "container": {"padding": "5!important","background-color":'white'},
                    "icon": {"color": "black", "font-size": "23px"}, 
                    "nav-link": {"color":"black","font-size": "20px", "text-align": "left", "margin":"0px", "--hover-color": "blue"},
                    "nav-link-selected": {"background-color": "#02ab21"},
                    "menu-title": {"color": "black"}}
                )

    
        if app == "App":
            application.app()
        if app == 'About Us':
            about.app()    
        if app == 'Homepage':
            homepage.app()  

    run()            