import streamlit as st
import base64
import plotly.express as px

def app():

    # @st.experimental_memo
    @st.cache_data 
    def get_img_as_base64(file):
        with open(file, "rb") as f:
            data = f.read()
        return base64.b64encode(data).decode()


    img = get_img_as_base64("./image.jpg")
    # img2 = get_img_as_base64("image2.jpg")
    img4 = get_img_as_base64("./image4.jpg")


    page_bg_img = f"""
    <style>
    [data-testid="stAppViewContainer"] > .main {{
    # background-image: url("https://images.unsplash.com/photo-1501426026826-31c667bdf23d");
    background-image: url("data:image/png;base64,{img4}");
    # filter: blur(5px); 
    background-size: 180%;
    background-position: top left;
    background-repeat: no-repeat;
    background-attachment: local;
    }}

    [data-testid="stSidebar"] > div:first-child {{
    # background-image: url("data:image/png;base64,{img}");
    background-position: center; 
    background-repeat: no-repeat;
    background-attachment: fixed;
    }}

    [data-testid="stHeader"] {{
    background: rgba(0,0,0,0);
    }}

    [data-testid="stToolbar"] {{
    right: 2rem;
    }}
    </style>
    """
    st.markdown(page_bg_img, unsafe_allow_html=True)

    with st.container():

        st.title("Welcome to Stock Price Prediction - Your Ultimate Stock Market Companion")
        st.markdown(
            "Are you looking to stay ahead in the dynamic world of stock trading? Look no further! [Your Website Name] is here to empower you with cutting-edge tools and insights for intelligent stock market decisions."
        )
