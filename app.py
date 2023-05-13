
import streamlit as st
import time
from model import RFC, df


st.set_page_config(page_title="Aqua Check", page_icon="media/favicon.png", layout="wide")

st.markdown("""
        <style>
        
        .block-container {
        
                padding-top: 0rem;
                padding-bottom: 0rem;
                padding-left: 5rem;
                padding-right: 5rem;
        }

        #MainMenu {visibility: hidden;}

        footer {visibility: hidden;}

        header {visibility: hidden;}

        button[title="View fullscreen"]{visibility: hidden;}
        
        .css-1q7spjk.e16nr0p34 {
        
                font-size: 1.6rem;
                padding-top: 1rem;
        }

        .css-15zrgzn {display: none;}
        .css-eczf16 {display: none;}
        .css-jn99sy {display: none;}
        
        .css-10trblm.e16nr0p30 {
                
                padding-top: 2rem;
                text-align: left;
        }
        .css-1kyxreq.etr89bj2 {padding-left: 8rem;}
        .css-5rimss.e16nr0p34 {text-align: right;}

        </style>
        """, unsafe_allow_html=True)

title, bg = st.columns(2, gap="large")

with title:

        st.title("Aqua Check — Controlling Pollution through AI")
        st.caption("\"Over the past 100 years, we have lost half of our natural wetlands, and a significant number of freshwater species to climate changes caused by water pollution.\"")
        st.write("— United Nations: World Water Development Report 2020")

with bg:
        st.image("media/water_pollution_vector_art.jpg", width=400, caption="Image by brgfx on Freepik")

st.divider()

col1, col2, col3 = st.columns(3, gap="large")

with col1:

        ph = st.slider('Choose the pH level of water sample.', 0, 14, 0)
        st.divider()

        hardness = st.number_input('Enter the measure of water hardness in mg/L.')
        st.divider()

        solids = st.number_input('What is the Total Dissolved Solids of the water sample in ppm?')
        st.divider()                

with col2:

        sulfates = st.number_input('Enter the amount of Sulfates, in mg/L, present in the  sample.')
        st.divider()
        
        chloramines = st.slider('Choose the amount of Chloramines, in ppm, present in the water sample.', 0, 15, 0)
        st.divider()


        electrical_conductivity = st.number_input('What is the electrical conducitivity of the water sample?')
        st.divider()
        

with col3:

        organic_carbon = st.slider('Choose the amount of Organic Carbon, in ppm, present in the water sample.', 0, 30, 0)
        st.divider()

        
        trihalomethanes = st.number_input('Enter the amount of Trihalomethanes, in NTU, present in the sample.')
        st.divider()

        turbidity = st.number_input('What is the turbidity of the water?')
        st.divider()

quality_parameters = [ph, hardness, solids, chloramines, sulfates, electrical_conductivity, organic_carbon, trihalomethanes, turbidity]

standardized_parameters = []
index =  0

for columns in ['ph', 'Hardness','Solids', 'Chloramines','Sulfate','Conductivity','Organic_carbon','Trihalomethanes','Turbidity']:

        standardized_parameters.append((quality_parameters[index]-df[columns].mean())/ df[columns].std())
        index +=1

if st.button('Check Quality'):

        quality = RFC.predict([standardized_parameters])[0]

        if quality == 1:
                st.success("Yippe!😃 Water is not polluted")
                time.sleep(1)
                st.balloons()

        elif quality == 0:
                st.error("Oh no!😔 Water is pollluted ")

