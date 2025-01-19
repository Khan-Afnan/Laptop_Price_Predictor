import streamlit as st
import pickle
import numpy as np
from PIL import Image

# Load the model and data
pipe = pickle.load(open('pipe.pkl', 'rb'))
df = pickle.load(open('df.pkl', 'rb'))

# Set the page configuration
st.set_page_config(page_title="Laptop Price Predictor", page_icon="\U0001F4BB", layout="centered")

# Add a banner image
st.image("laptop_banner.jpg", use_column_width=True)

# Title and subtitle
st.title("Laptop Price Predictor")
st.subheader("Predict the price of a laptop based on its specifications")

# Input fields with better organization
with st.form("predict_form"):
    st.markdown("### Select Laptop Specifications")

    # Brand
    company = st.selectbox('Brand', df['Company'].unique(), help="Select the brand of the laptop.")

    # Type of laptop
    type = st.selectbox('Type', df['TypeName'].unique(), help="Select the type of laptop.")

    # RAM
    ram = st.selectbox('RAM (in GB)', [2, 4, 6, 8, 12, 16, 24, 32, 64], help="Choose the RAM size.")

    # Weight
    weight = st.number_input('Weight of the Laptop (in kg)', min_value=0.5, max_value=5.0, step=0.1, help="Enter the weight in kilograms.")

    # Touchscreen
    touchscreen = st.radio('Touchscreen', ['No', 'Yes'], help="Does the laptop have a touchscreen?")

    # IPS
    ips = st.radio('IPS Display', ['No', 'Yes'], help="Does the laptop have an IPS display?")

    # Screen size
    screen_size = st.slider('Screen size (in inches)', 10.0, 18.0, 13.0, step=0.1, help="Select the screen size.")

    # Resolution
    resolution = st.selectbox('Screen Resolution', ['1920x1080', '1366x768', '1600x900', '3840x2160', '3200x1800',
                                                     '2880x1800', '2560x1600', '2560x1440', '2304x1440'],
                               help="Choose the screen resolution.")

    # CPU
    cpu = st.selectbox('CPU', df['Cpu brand'].unique(), help="Select the CPU brand.")

    # HDD
    hdd = st.selectbox('HDD (in GB)', [0, 128, 256, 512, 1024, 2048], help="Specify the HDD capacity.")

    # SSD
    ssd = st.selectbox('SSD (in GB)', [0, 8, 128, 256, 512, 1024], help="Specify the SSD capacity.")

    # GPU
    gpu = st.selectbox('GPU', df['Gpu brand'].unique(), help="Choose the GPU brand.")

    # Operating System
    os = st.selectbox('Operating System', df['os'].unique(), help="Select the operating system.")

    # Submit button
    submitted = st.form_submit_button("Predict Price")

if submitted:
    # Process input
    ppi = None
    if touchscreen == 'Yes':
        touchscreen = 1
    else:
        touchscreen = 0

    if ips == 'Yes':
        ips = 1
    else:
        ips = 0

    X_res = int(resolution.split('x')[0])
    Y_res = int(resolution.split('x')[1])
    ppi = ((X_res**2) + (Y_res**2))**0.5 / screen_size

    query = np.array([company, type, ram, weight, touchscreen, ips, ppi, cpu, hdd, ssd, gpu, os])
    query = query.reshape(1, 12)

    # Prediction
    predicted_price = np.exp(pipe.predict(query)[0])

    # Display the result
    st.success(f"The predicted price of this configuration is: **₹{int(predicted_price):,}**")

# Footer
st.markdown("---")
st.markdown("**Developed by Afnan Ulla**")
st.markdown("For any issues, contact: [afnanulla149@gmail.com](mailto:afnanulla149@gmail.com)")
