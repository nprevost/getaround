import streamlit as st
import requests
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
import plotly.io as pio
import numpy as np
import math

@st.cache_data 
def load_data(nrows: int = None):
    data = pd.read_excel("data/get_around_delay_analysis.xlsx", nrows=nrows)
    return data


if __name__ == '__main__':
    st.set_page_config(
        page_title="GetAround Late Checkouts Analysis",
        page_icon="🚘⏱",
        layout="wide"
    )

    st.logo(
        "https://getaround-assets.gumlet.io/images/shared/icons/app-icon-production.svg",
        link="https://nprevost-getaround-streamlit.hf.space/",
        icon_image=None,
    )

    st.image("https://lever-client-logos.s3.amazonaws.com/2bd4cdf9-37f2-497f-9096-c2793296a75f-1568844229943.png", caption="GetAround")

    df = load_data()

    st.write(df)