import streamlit as st
import base64
import plotly.express as px

def app():
    df = px.data.iris()

    # @st.experimental_memo
    @st.cache_data 
    def get_img_as_base64(file):
        with open(file, "rb") as f:
            data = f.read()
        return base64.b64encode(data).decode()


    img = get_img_as_base64("image.jpg")
    img2 = get_img_as_base64("image2.jpg")
    img4 = get_img_as_base64("image4.jpg")


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

        st.title("About Project")
        st.markdown(
            "Our Stock Market Prediction and Forecast Project combines the power of cutting-edge Recurrent Neural Network (RNN) technology with comprehensive historical data analysis to offer users accurate and insightful predictions for various stocks. By harnessing the capabilities of the RNN model, we enable investors and traders to make informed decisions based on reliable forecasts generated from the intricate analysis of past market trends. With our user-friendly interface built on the Streamlit framework, accessing and interpreting the predictions becomes seamless and intuitive for users of all levels of expertise. Our mission is to provide a valuable tool that empowers individuals in the financial world, equipping them with the necessary foresight to navigate the complexities of the stock market with confidence and precision."
        )
