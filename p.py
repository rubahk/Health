#To import the libraries:
import pandas as pd 
import streamlit as st
import numpy as np
import matplotlib.pyplot as plt
import plotly.express as px
import requests
from io import StringIO
from PIL import Image
import seaborn as sns
import datetime as dt
from plotly.subplots import make_subplots
import plotly.graph_objs as go
import streamlit.components.v1 as components

#To read the first dataset:  #Cases in Guinea
orig_url='https://drive.google.com/file/d/11tXe-Fm6PPHhyTlHZIfOjIMl1fwbvyla/view?usp=sharing'
file_id = orig_url.split('/')[-2]
dwn_url='https://drive.google.com/uc?export=download&id=' + file_id
url = requests.get(dwn_url).text
csv_raw = StringIO(url)
Guinea = pd.read_csv(csv_raw)

#To calculate the total cases from 2014-2016:
Total_G= Guinea['Confirmed_cases'].sum()

#To seperate the years:
Guinea2014= Guinea[Guinea['Year']==2014]
Guinea2015= Guinea[Guinea['Year']==2015]
Guinea2016= Guinea[Guinea['Year']==2016]

#To calculate the total cases in Guinea per year: 
Guinea['Year'].unique()
G_total= Guinea.groupby('Year')['Confirmed_cases'].sum().round()
Cases_2014= G_total.iloc[0]
Cases_2015= G_total.iloc[1]
Cases_2016= G_total.iloc[2]

#To calculate the total deaths in Guinea per year: 
G_death= Guinea.groupby('Year')['Confirmed_deaths'].sum().round()
G_2014= G_death.iloc[0]
G_2015= G_death.iloc[1]
G_2016= G_death.iloc[2]

#To calculate Confirmed Cases per month in Guinea: 
GC_2014=Guinea2014.groupby('Month')['Confirmed_cases'].sum()
GC_2014=GC_2014.reset_index() 
GC_2015=Guinea2015.groupby('Month')['Confirmed_cases'].sum()
GC_2015=GC_2015.reset_index()
GC_2016=Guinea2016.groupby('Month')['Confirmed_cases'].sum()
GC_2016=GC_2016.reset_index() 


#To calculate total deaths per month in Guinea: 
GD_2014=Guinea2014.groupby('Month')['Confirmed_deaths'].sum()
GD_2014=GD_2014.reset_index() 
GD_2015=Guinea2015.groupby('Month')['Confirmed_deaths'].sum()
GD_2015=GD_2015.reset_index() 
GD_2016=Guinea2016.groupby('Month')['Confirmed_deaths'].sum()
GD_2016=GD_2016.reset_index() 


#---------------------------------------------------------------------------------------------------

#To read the second dataset:  #Cases in Liberia
orig_url1='https://drive.google.com/file/d/1S-LLgd3MEP0DyYQrLKo7BcT9ISc4_Tb4/view?usp=sharing'
file_id1= orig_url1.split('/')[-2]
dwn_url1='https://drive.google.com/uc?export=download&id=' + file_id1
url1 = requests.get(dwn_url1).text
csv_raw1 = StringIO(url1)
Liberia= pd.read_csv(csv_raw1)

#To calculate the total cases from 2014-2016:
Total_L= Liberia['Confirmed Cases'].sum()

#To seperate the years: 
Liberia2014= Liberia[Liberia['Year']==2014]
Liberia2015= Liberia[Liberia['Year']==2015]
Liberia2016= Liberia[Liberia['Year']==2016]

#To calculate the total cases in Liberia per year: 
Liberia['Year'].unique()
L_total= Liberia.groupby('Year')['Confirmed Cases'].sum()
LCase_2014= L_total.iloc[0]
LCase_2015= L_total.iloc[1]
LCase_2016= L_total.iloc[2]
 
#To calculate the total deaths in Liberia per year: 
L_death= Liberia.groupby('Year')['Confirmed Deaths'].sum()
D_2014= L_death.iloc[0]
D_2015= L_death.iloc[1]
D_2016= L_death.iloc[2]

#To calculate Confirmed Cases per month in Liberia: 
LC_2014=Liberia2014.groupby('Month')['Confirmed Cases'].sum()
LC_2014=LC_2014.reset_index() 
LC_2015=Liberia2015.groupby('Month')['Confirmed Cases'].sum()
LC_2015=LC_2015.reset_index() 
LC_2016=Liberia2016.groupby('Month')['Confirmed Cases'].sum()
LC_2016=LC_2016.reset_index() 

#To calculate total deaths per month in Liberia: 
LD_2014=Liberia2014.groupby('Month')['Confirmed Deaths'].sum()
LD_2014=LD_2014.reset_index() 
LD_2015=Liberia2015.groupby('Month')['Confirmed Deaths'].sum()
LD_2015=LD_2015.reset_index() 
LD_2016=Liberia2016.groupby('Month')['Confirmed Deaths'].sum()
LD_2016=LD_2016.reset_index() 
#---------------------------------------------------------------------------------------------------

#To read the third dataset:  #Cases in Sierra Leone
orig_url2='https://drive.google.com/file/d/10FCrNzkIaNIexKSJcBAaOg-EKU3wUbrM/view?usp=sharing'
file_id2= orig_url2.split('/')[-2]
dwn_url2='https://drive.google.com/uc?export=download&id=' + file_id2
url2 = requests.get(dwn_url2).text
csv_raw2 = StringIO(url2)
Sierra= pd.read_csv(csv_raw2)

#To calculate the total cases from 2014-2016:
Total_S= Sierra['Confirmed Cases'].sum()

#To seperate the years:  
Sierra2014= Sierra[Sierra['Year']==2014]
Sierra2015= Sierra[Sierra['Year']==2015]
Sierra2016= Sierra[Sierra['Year']==2016]

#To calculate the total cases in Sierra Leone per year: 
Sierra['Year'].unique()
S_total= Sierra.groupby('Year')['Confirmed Cases'].sum()
SCase_2014= S_total.iloc[0]
SCase_2015= S_total.iloc[1]
SCase_2016= S_total.iloc[2]

#To calculate the total deaths in Sierra Leone per year: 
S_death= Sierra.groupby('Year')['Confirmed Deaths'].sum().round()
S_2014= S_death.iloc[0]
S_2015= S_death.iloc[1]
S_2016= S_death.iloc[2]

#To calculate Confirmed Cases per month in Sierra Leone: 
SC_2014=Sierra2014.groupby('Month')['Confirmed Cases'].sum()
SC_2014=SC_2014.reset_index() 
SC_2015=Sierra2015.groupby('Month')['Confirmed Cases'].sum()
SC_2015=SC_2015.reset_index() 
SC_2016=Sierra2016.groupby('Month')['Confirmed Cases'].sum()
SC_2016=SC_2016.reset_index() 

#To calculate total deaths per month in Sierra Leone: 
SD_2014=Sierra2014.groupby('Month')['Confirmed Deaths'].sum()
SD_2014=SD_2014.reset_index() 
SD_2015=Sierra2015.groupby('Month')['Confirmed Deaths'].sum()
SD_2015=SD_2015.reset_index() 
SD_2016=Sierra2016.groupby('Month')['Confirmed Deaths'].sum()
SD_2016=SD_2016.reset_index() 
#---------------------------------------------------------------------------------------------------
#To read the forth dataset: #Gender in Guinea
orig_url3='https://drive.google.com/file/d/1jzfZM1-qL0jN17ukCy2QkOA8vBQqNVRM/view?usp=sharing'
file_id3 = orig_url3.split('/')[-2]
dwn_url3='https://drive.google.com/uc?export=download&id=' + file_id3
url3 = requests.get(dwn_url3).text
csv_raw3 = StringIO(url3)
gender_G = pd.read_csv(csv_raw3)

#Total Cases per Gender in Guinea
GM= gender_G.iloc[0]['Male Cases']
GF= gender_G.iloc[0]['Female Cases']

#---------------------------------------------------------------------------------------------------
#To read the fifth dataset: #Gender in Liberia
orig_url4='https://drive.google.com/file/d/1b92gs1QNar0QdUQit-VRsqaGRX0eZ1GY/view?usp=sharing'
file_id4 = orig_url4.split('/')[-2]
dwn_url4='https://drive.google.com/uc?export=download&id=' + file_id4
url4 = requests.get(dwn_url4).text
csv_raw4 = StringIO(url4)
gender_L = pd.read_csv(csv_raw4)

#Total Cases per Gender in Liberia
LM= gender_L.iloc[0]['Male Cases']
LF= gender_L.iloc[0]['Female Cases']
#---------------------------------------------------------------------------------------------------
#To read the sixth dataset: #Gender in Sierra
orig_url5='https://drive.google.com/file/d/1_OzVgCw4DPmtG1Z-baWkPgJ6TGxOxBRE/view?usp=sharing'
file_id5 = orig_url5.split('/')[-2]
dwn_url5='https://drive.google.com/uc?export=download&id=' + file_id5
url5 = requests.get(dwn_url5).text
csv_raw5 = StringIO(url5)
gender_S = pd.read_csv(csv_raw5)

#Total Cases per Gender in Sierra
SM= gender_S.iloc[0]['Male Cases']
SF= gender_S.iloc[0]['Female Cases']
#---------------------------------------------------------------------------------------------------
#To read the seventh dataset: #Age groups in Guinea
orig_url6='https://drive.google.com/file/d/19HnNBa1wpa2xaR95ALDMhMM25D-RkTuk/view?usp=sharing'
file_id6 = orig_url6.split('/')[-2]
dwn_url6='https://drive.google.com/uc?export=download&id=' + file_id6
url6 = requests.get(dwn_url6).text
csv_raw6 = StringIO(url6)
Gage = pd.read_csv(csv_raw6)
#---------------------------------------------------------------------------------------------------
#To read the eighth dataset: #Age groups in Liberia
orig_url7='https://drive.google.com/file/d/1kBM1l7-Sxb6mnbBTEkpuNE0PKMipy-Nm/view?usp=sharing'
file_id7 = orig_url7.split('/')[-2]
dwn_url7='https://drive.google.com/uc?export=download&id=' + file_id7
url7 = requests.get(dwn_url7).text
csv_raw7 = StringIO(url7)
Lage = pd.read_csv(csv_raw7)
#---------------------------------------------------------------------------------------------------
#To read the ninth dataset: #Age groups in Sierra
orig_url8='https://drive.google.com/file/d/1nHbfeWp4K2u_iGco8e7Cew2bHnjqEobL/view?usp=sharing'
file_id8 = orig_url8.split('/')[-2]
dwn_url8='https://drive.google.com/uc?export=download&id=' + file_id8
url8 = requests.get(dwn_url8).text
csv_raw8 = StringIO(url8)
Sage = pd.read_csv(csv_raw8)
#---------------------------------------------------------------------------------------------------
#To read the tenth dataset: #Global Cases
orig_url9='https://drive.google.com/file/d/1sMTsIt5bpUVZyS2L6hrNZMX_kAX0aTFh/view?usp=sharing'
file_id9 = orig_url9.split('/')[-2]
dwn_url9='https://drive.google.com/uc?export=download&id=' + file_id9
url9 = requests.get(dwn_url9).text
csv_raw9 = StringIO(url9)
global_C= pd.read_csv(csv_raw9)
#---------------------------------------------------------------------------------------------------
#To read the Eleventh dataset: #Global Deaths
orig_url10='https://drive.google.com/file/d/1EEaaQAQMY--Dn3WBGPQ2JKg3xr5Xed1Y/view?usp=sharing'
file_id10 = orig_url10.split('/')[-2]
dwn_url10='https://drive.google.com/uc?export=download&id=' + file_id10
url10 = requests.get(dwn_url10).text
csv_raw10 = StringIO(url10)
global_D= pd.read_csv(csv_raw10)
#---------------------------------------------------------------------------------------------------
#To insert the image:
url= 'https://drive.google.com/file/d/19QEG0gY2FZIo0CpaLgSFTCVWP0uqbifL/view?usp=sharing'
image='https://drive.google.com/uc?export=download&id='+url.split('/')[-2]

#To add a title:
st.title("Ebola Virus Disease Outbreak in West Africa 2014-2016")
st.write("by Ruba Al Hakeem | June 2021")
st.set_option('deprecation.showPyplotGlobalUse', False)
#---------------------------------------------------------------------------------------------------
#To create the filter: 
choice= st.sidebar.radio("Menu",["Homepage","Ebola Situation Room"])

if "Homepage"in choice:       
        st.write("")
        st.info("This dashboard shows the official CDC data on the Ebola Virus Disease (EVD) outbreak in West Africa in 2014-2016.")
        st.subheader("Ebola Virus Disease Overview:")
        middle_col=st.image(image,width=710)
        st.markdown("On March 23, 2014, the World Health Organization reported cases of Ebola Virus Disease (EVD) in the rural area of southeastern Guinea. The cases marked the beginning of the **West Africa Ebola epidemic** which the **largest in history**.")
        st.write("Ebola virus disease (EVD) is a fatal disease with occasional outbreaks that happen mainly on the African continent. It most commonly affects people and nonhuman primates such as monkeys, gorillas, and chimpanzees. It is caused by an infection with a group of viruses within the genus Ebolavirus.")
        st.markdown("This Streamlit dashboard is a valuable tool that allows users to have an overview about the trends and patterns, distribution across gender and age, geographic mapping of the Ebola Virus Disease outbreak in 2014-2016 in three African countries, **Guinea**, **Liberia**, and **Sierra Leone**.")
#---------------------------------------------------------------------------------------------------
#To create another filter: 
col1, col2, col3 = st.beta_columns(3)


if "Ebola Situation Room" in choice:
    task= st.sidebar.radio("Navigate",["Guinea", "Liberia","Sierra Leone", "Worldwide"])
    
    
   
    if ((task == "Guinea")):
        frame= st.sidebar.radio("Filter by year",["2014", "2015","2016"])
                        
        with col1:   
            st.markdown('#')
            st.markdown(f"<h2 style='text-align:center; font-family:arial;' >{'<b>Guinea</b>'} </h2>", unsafe_allow_html=True)
            st.markdown(f"<h2 style='text-align:center; font-family:arial;' >{Total_G} </h2>", unsafe_allow_html=True)
            st.markdown(f"<h3 style='text-align:center; font-family:arial;' > total cases </h3>", unsafe_allow_html=True)
            
        with col2:
            st.markdown('#')
            st.markdown(f"<h2 style='text-align:center; font-family:arial;' >{'<b>Male</b>'} </h2>", unsafe_allow_html=True)
            st.markdown(f"<h2 style='text-align:center; font-family:arial;' >{GM} </h2>", unsafe_allow_html=True)
            st.markdown(f"<h3 style='text-align:center; font-family:arial;' > total cases </h3>", unsafe_allow_html=True)    
            
        with col3:
            st.markdown('#')
            st.markdown(f"<h2 style='text-align:center; font-family:arial;' >{'<b>Female</b>'} </h2>", unsafe_allow_html=True)
            st.markdown(f"<h2 style='text-align:center; font-family:arial;' >{GF}  </h2>", unsafe_allow_html=True)
            st.markdown(f"<h3 style='text-align:center; font-family:arial;' > total cases </h3>", unsafe_allow_html=True)
       
    
        st.markdown('#')
        st.subheader("Total confirmed cases per age groups")
        fig=px.bar(Gage,x="Age Group",y="Total Cases",color="Age Group")
        fig.update_layout({
            'plot_bgcolor':'rgba(0, 0, 0, 0)',
            'paper_bgcolor':'rgba(0, 0, 0, 0)',
            })
        st.plotly_chart(fig)
            
   
        st.markdown('#')        
        selected_status= st.selectbox('Filter by Cases/Deaths:', options=['Monthly Confirmed Cases','Monthly Confirmed Deaths'])     
           
        
        if ((frame =='2014')) and ((selected_status == 'Monthly Confirmed Cases')):
            st.subheader("Monthly confirmed cases in 2014")
            fig1= px.line(GC_2014, x=GC_2014["Month"],y=GC_2014["Confirmed_cases"],width=600,height=600,labels={"Confirmed_cases":" Total Cases","Month":"Month"})
            fig1.update_traces(line_color='#636EFA')
            fig1.update_layout({
                "plot_bgcolor":"rgba(0, 0, 0, 0)",
                "paper_bgcolor":"rgba(0, 0, 0, 0)",
                })
            fig1.update_xaxes(title_text='Month',range=[1,12])
            fig1.update_yaxes(title_text='Confirmed Cases')
            st.plotly_chart(fig1)
            
        if ((frame =='2015')) and ((selected_status == 'Monthly Confirmed Cases')):
            st.subheader("Monthly confirmed cases in 2015")
            fig2= px.line(GC_2015, x=GC_2015["Month"],y=GC_2015["Confirmed_cases"],width=600,height=600,labels={"Confirmed_cases":" Total Cases","Month":"Month"})
            fig2.update_traces(line_color='#636EFA')
            fig2.update_layout({
                "plot_bgcolor":"rgba(0, 0, 0, 0)",
                "paper_bgcolor":"rgba(0, 0, 0, 0)",
                })
            fig2.update_xaxes(title_text='Month',range=[1,12])
            fig2.update_yaxes(title_text='Confirmed Cases')
            st.plotly_chart(fig2)                 
  
        if ((frame =='2016')) and ((selected_status == 'Monthly Confirmed Cases')):
            st.subheader("Monthly confirmed cases in 2016")
            fig3= px.line(GC_2016, x=GC_2016["Month"],y=GC_2016["Confirmed_cases"],width=600,height=600,labels={"Confirmed_cases":" Total Cases","Month":"Month"})
            fig3.update_traces(line_color='#636EFA')
            fig3.update_layout({
                "plot_bgcolor":"rgba(0, 0, 0, 0)",
                "paper_bgcolor":"rgba(0, 0, 0, 0)",
                })
            fig3.update_xaxes(title_text='Month',range=[1,12])
            fig3.update_yaxes(title_text='Confirmed Cases')
            st.plotly_chart(fig3)
  
                
        if ((frame =='2014')) and ((selected_status == 'Monthly Confirmed Deaths')):
            st.subheader("Monthly confirmed deaths in 2014")
            fig4= px.line(GD_2014, x=GD_2014["Month"],y=GD_2014["Confirmed_deaths"],width=600,height=600,labels={"Confirmed_deaths":" Total Deaths","Month":"Month"})
            fig4.update_traces(line_color='#EF553B')
            fig4.update_layout({
                "plot_bgcolor":"rgba(0, 0, 0, 0)",
                "paper_bgcolor":"rgba(0, 0, 0, 0)",
                })
            fig4.update_xaxes(title_text='Month',range=[1,12])
            fig4.update_yaxes(title_text='Confirmed Deaths')
            st.plotly_chart(fig4)
            
        if ((frame =='2015')) and ((selected_status == 'Monthly Confirmed Deaths')):
            st.subheader("Monthly confirmed deaths in 2015")
            fig5= px.line(GD_2015, x=GD_2015["Month"],y=GD_2015["Confirmed_deaths"],width=600,height=600,labels={"Confirmed_deaths":" Total Deaths","Month":"Month"})
            fig5.update_traces(line_color='#EF553B')
            fig5.update_layout({
                "plot_bgcolor":"rgba(0, 0, 0, 0)",
                "paper_bgcolor":"rgba(0, 0, 0, 0)",
                })
            fig5.update_xaxes(title_text='Month',range=[1,12])
            fig5.update_yaxes(title_text='Confirmed Deaths')
            st.plotly_chart(fig5)
            
        if ((frame =='2016')) and ((selected_status == 'Monthly Confirmed Deaths')):
            st.subheader("Monthly confirmed deaths in 2016")
            fig6= px.line(GD_2016, x=GD_2016["Month"],y=GD_2016["Confirmed_deaths"],width=600,height=600,labels={"Confirmed_deaths":" Total Deaths","Month":"Month"})
            fig6.update_traces(line_color='#EF553B')
            fig6.update_layout({
                "plot_bgcolor":"rgba(0, 0, 0, 0)",
                "paper_bgcolor":"rgba(0, 0, 0, 0)",
                })
            fig6.update_xaxes(title_text='Month',range=[1,12])
            fig6.update_yaxes(title_text='Confirmed Deaths')
            st.plotly_chart(fig6)
#---------------------------------------------------------------------------------------------------            
    col4, col5, col6 = st.beta_columns(3)
    
    
    if ((task == "Liberia")):
        frame= st.sidebar.radio("Filter by year",["2014", "2015","2016"])
        with col4:
            st.markdown('#')
            st.markdown(f"<h2 style='text-align:center; font-family:arial;' >{'<b>Liberia</b>'} </h2>", unsafe_allow_html=True)
            st.markdown(f"<h2 style='text-align:center; font-family:arial;' >{Total_L} </h2>", unsafe_allow_html=True)
            st.markdown(f"<h3 style='text-align:center; font-family:arial;' > total cases </h3>", unsafe_allow_html=True)
        with col5:
            st.markdown('#')
            st.markdown(f"<h2 style='text-align:center; font-family:arial;' >{'<b>Male</b>'} </h2>", unsafe_allow_html=True)
            st.markdown(f"<h2 style='text-align:center; font-family:arial;' >{LM} </h2>", unsafe_allow_html=True)
            st.markdown(f"<h3 style='text-align:center; font-family:arial;' > total cases </h3>", unsafe_allow_html=True)
        with col6:
            st.markdown('#')
            st.markdown(f"<h2 style='text-align:center; font-family:arial;' >{'<b>Female</b>'} </h2>", unsafe_allow_html=True)
            st.markdown(f"<h2 style='text-align:center; font-family:arial;' >{LF} </h2>", unsafe_allow_html=True)
            st.markdown(f"<h3 style='text-align:center; font-family:arial;' > total cases </h3>", unsafe_allow_html=True)
            
        st.markdown('#')
        st.subheader("Total confirmed cases per age groups")
        fig7=px.bar(Lage,x="Age Group",y="Total Cases",color="Age Group")
        fig7.update_layout({
            'plot_bgcolor':'rgba(0, 0, 0, 0)',
            'paper_bgcolor':'rgba(0, 0, 0, 0)',
            })
        st.plotly_chart(fig7)
        
        st.markdown('#')
        selected_status= st.selectbox('Filter by Cases/Deaths:', options=['Monthly Confirmed Cases','Monthly Confirmed Deaths'])
        
        if ((frame =='2014')) and ((selected_status == 'Monthly Confirmed Cases')):
            st.subheader("Monthly confirmed cases in 2014")
            fig8= px.line(LC_2014, x=LC_2014["Month"],y=LC_2014["Confirmed Cases"],width=600,height=600,labels={"Confirmed Cases":" Total Cases","Month":"Month"})
            fig8.update_traces(line_color='#636EFA')
            fig8.update_layout({
                "plot_bgcolor":"rgba(0, 0, 0, 0)",
                "paper_bgcolor":"rgba(0, 0, 0, 0)",
                })
            fig8.update_xaxes(title_text='Month',range=[1,12])
            fig8.update_yaxes(title_text='Confirmed Cases')
            st.plotly_chart(fig8)
            
        if ((frame =='2015')) and ((selected_status == 'Monthly Confirmed Cases')):
            st.subheader("Monthly confirmed cases in 2015")
            fig9= px.line(LC_2015, x=LC_2015["Month"],y=LC_2015["Confirmed Cases"],width=600,height=600,labels={"Confirmed Cases":" Total Cases","Month":"Month"})
            fig9.update_traces(line_color='#636EFA')
            fig9.update_layout({
                "plot_bgcolor":"rgba(0, 0, 0, 0)",
                "paper_bgcolor":"rgba(0, 0, 0, 0)",
                })
            fig9.update_xaxes(title_text='Month',range=[1,12])
            fig9.update_yaxes(title_text='Confirmed Cases')
            st.plotly_chart(fig9)
            
        if ((frame =='2016')) and ((selected_status == 'Monthly Confirmed Cases')):
            st.subheader("Monthly confirmed cases in 2016")
            fig10= px.line(LC_2016, x=LC_2016["Month"],y=LC_2016["Confirmed Cases"],width=600,height=600,labels={"Confirmed Cases":" Total Cases","Month":"Month"})
            fig10.update_traces(line_color='#636EFA')
            fig10.update_layout({
                "plot_bgcolor":"rgba(0, 0, 0, 0)",
                "paper_bgcolor":"rgba(0, 0, 0, 0)",
                })
            fig10.update_xaxes(title_text='Month',range=[1,12])
            fig10.update_yaxes(title_text='Confirmed Cases')
            st.plotly_chart(fig10)
            
        if ((frame =='2014')) and ((selected_status == 'Monthly Confirmed Deaths')):
            st.subheader("Monthly confirmed deaths in 2014")
            fig11= px.line(LD_2014, x=LD_2014["Month"],y=LD_2014["Confirmed Deaths"],width=600,height=600,labels={"Confirmed Deaths":" Total Deaths","Month":"Month"})
            fig11.update_traces(line_color='#EF553B')
            fig11.update_layout({
                "plot_bgcolor":"rgba(0, 0, 0, 0)",
                "paper_bgcolor":"rgba(0, 0, 0, 0)",
                })
            fig11.update_xaxes(title_text='Month',range=[1,12])
            fig11.update_yaxes(title_text='Confirmed Deaths')
            st.plotly_chart(fig11)
            
        if ((frame =='2015')) and ((selected_status == 'Monthly Confirmed Deaths')):
            st.subheader("Monthly confirmed deaths in 2015")
            fig12= px.line(LD_2015, x=LD_2015["Month"],y=LD_2015["Confirmed Deaths"],width=600,height=600,labels={"Confirmed Deaths":" Total Deaths","Month":"Month"})
            fig12.update_traces(line_color='#EF553B')
            fig12.update_layout({
                "plot_bgcolor":"rgba(0, 0, 0, 0)",
                "paper_bgcolor":"rgba(0, 0, 0, 0)",
                })
            fig12.update_xaxes(title_text='Month',range=[1,12])
            fig12.update_yaxes(title_text='Confirmed Deaths')
            st.plotly_chart(fig12)
            
        if ((frame =='2016')) and ((selected_status == 'Monthly Confirmed Deaths')):
            st.subheader("Monthly confirmed deaths in 2016")
            fig13= px.line(LD_2016, x=LD_2016["Month"],y=LD_2016["Confirmed Deaths"],width=600,height=600,labels={"Confirmed Deaths":" Total Deaths","Month":"Month"})
            fig13.update_traces(line_color='#EF553B')
            fig13.update_layout({
                "plot_bgcolor":"rgba(0, 0, 0, 0)",
                "paper_bgcolor":"rgba(0, 0, 0, 0)",
                })
            fig13.update_xaxes(title_text='Month',range=[1,12])
            fig13.update_yaxes(title_text='Confirmed Deaths')
            st.plotly_chart(fig13)
            
#---------------------------------------------------------------------------------------------------
    col7, col8, col9 = st.beta_columns(3)
    
    
    if ((task == "Sierra Leone")):
        frame= st.sidebar.radio("Filter by year",["2014", "2015","2016"])
        with col7:
            st.markdown('#')
            st.markdown(f"<h2 style='text-align:center; font-family:arial;' >{'<b>Sierra Leone</b>'} </h2>", unsafe_allow_html=True)
            st.markdown(f"<h2 style='text-align:center; font-family:arial;' >{Total_S} </h2>", unsafe_allow_html=True)
            st.markdown(f"<h3 style='text-align:center; font-family:arial;' > total cases </h3>", unsafe_allow_html=True)
        with col8:
            st.markdown('#')
            st.markdown(f"<h2 style='text-align:center; font-family:arial;' >{'<b>Male</b>'} </h2>", unsafe_allow_html=True)
            st.markdown(f"<h2 style='text-align:center; font-family:arial;' >{SM} </h2>", unsafe_allow_html=True)
            st.markdown(f"<h3 style='text-align:center; font-family:arial;' > total cases </h3>", unsafe_allow_html=True)
        with col9:
            st.markdown('#')
            st.markdown(f"<h2 style='text-align:center; font-family:arial;' >{'<b>Female</b>'} </h2>", unsafe_allow_html=True)
            st.markdown(f"<h2 style='text-align:center; font-family:arial;' >{SF}  </h2>", unsafe_allow_html=True)
            st.markdown(f"<h3 style='text-align:center; font-family:arial;' > total cases </h3>", unsafe_allow_html=True)
            st.markdown('#')
            
        st.subheader("Total confirmed cases per age groups")
        fig14=px.bar(Sage,x="Age Group",y="Total Cases",color="Age Group")
        fig14.update_layout({
            'plot_bgcolor':'rgba(0, 0, 0, 0)',
            'paper_bgcolor':'rgba(0, 0, 0, 0)',
            })
        st.plotly_chart(fig14)
        
        st.markdown('#')
        selected_status= st.selectbox('Filter by Cases/Deaths:', options=['Monthly Confirmed Cases','Monthly Confirmed Deaths'])
        
        if ((frame =='2014')) and ((selected_status == 'Monthly Confirmed Cases')):
            st.subheader("Monthly confirmed cases in 2014")
            fig15= px.line(SC_2014, x=SC_2014["Month"],y=SC_2014["Confirmed Cases"],width=600,height=600,labels={"Confirmed Cases":" Total Cases","Month":"Month"})
            fig15.update_traces(line_color='#636EFA')
            fig15.update_layout({
                "plot_bgcolor":"rgba(0, 0, 0, 0)",
                "paper_bgcolor":"rgba(0, 0, 0, 0)",
                })
            fig15.update_xaxes(title_text='Month',range=[1,12])
            fig15.update_yaxes(title_text='Confirmed Cases')
            st.plotly_chart(fig15)
            
        if ((frame =='2015')) and ((selected_status == 'Monthly Confirmed Cases')):
            st.subheader("Monthly confirmed cases in 2015")
            fig16= px.line(SC_2015, x=SC_2015["Month"],y=SC_2015["Confirmed Cases"],width=600,height=600,labels={"Confirmed Cases":" Total Cases","Month":"Month"})
            fig16.update_traces(line_color='#636EFA')
            fig16.update_layout({
                "plot_bgcolor":"rgba(0, 0, 0, 0)",
                "paper_bgcolor":"rgba(0, 0, 0, 0)",
                })
            fig16.update_xaxes(title_text='Month',range=[1,12])
            fig16.update_yaxes(title_text='Confirmed Cases')
            st.plotly_chart(fig16)
            
        if ((frame =='2016')) and ((selected_status == 'Monthly Confirmed Cases')):
            st.subheader("Monthly confirmed cases in 2016")
            fig17= px.line(SC_2016, x=SC_2016["Month"],y=SC_2016["Confirmed Cases"],width=600,height=600,labels={"Confirmed Cases":" Total Cases","Month":"Month"})
            fig17.update_traces(line_color='#636EFA')
            fig17.update_layout({
                "plot_bgcolor":"rgba(0, 0, 0, 0)",
                "paper_bgcolor":"rgba(0, 0, 0, 0)",
                })
            fig17.update_xaxes(title_text='Month',range=[1,12])
            fig17.update_yaxes(title_text='Confirmed Cases')
            st.plotly_chart(fig17)
            
        if ((frame =='2014')) and ((selected_status == 'Monthly Confirmed Deaths')):
            st.subheader("Monthly confirmed deaths in 2014")
            fig18= px.line(SD_2014, x=SD_2014["Month"],y=SD_2014["Confirmed Deaths"],width=600,height=600,labels={"Confirmed Deaths":" Total Deaths","Month":"Month"})
            fig18.update_traces(line_color='#EF553B')
            fig18.update_layout({
                "plot_bgcolor":"rgba(0, 0, 0, 0)",
                "paper_bgcolor":"rgba(0, 0, 0, 0)",
                })
            fig18.update_xaxes(title_text='Month',range=[1,12])
            fig18.update_yaxes(title_text='Confirmed Deaths')
            st.plotly_chart(fig18)
            
        if ((frame =='2015')) and ((selected_status == 'Monthly Confirmed Deaths')):
            st.subheader("Monthly confirmed deaths in 2015")
            fig19= px.line(SD_2015, x=SD_2015["Month"],y=SD_2015["Confirmed Deaths"],width=600,height=600,labels={"Confirmed Deaths":" Total Deaths","Month":"Month"})
            fig19.update_traces(line_color='#EF553B')
            fig19.update_layout({
                "plot_bgcolor":"rgba(0, 0, 0, 0)",
                "paper_bgcolor":"rgba(0, 0, 0, 0)",
                })
            fig19.update_xaxes(title_text='Month',range=[1,12])
            fig19.update_yaxes(title_text='Confirmed Deaths')
            st.plotly_chart(fig19)
            
        if ((frame =='2016')) and ((selected_status == 'Monthly Confirmed Deaths')):
            st.subheader("Monthly confirmed deaths in 2016")
            fig20= px.line(SD_2016, x=SD_2016["Month"],y=SD_2016["Confirmed Deaths"],width=600,height=600,labels={"Confirmed Deaths":" Total Deaths","Month":"Month"})
            fig20.update_traces(line_color='#EF553B')
            fig20.update_layout({
                "plot_bgcolor":"rgba(0, 0, 0, 0)",
                "paper_bgcolor":"rgba(0, 0, 0, 0)",
                })
            fig20.update_xaxes(title_text='Month',range=[1,12])
            fig20.update_yaxes(title_text='Confirmed Deaths')
            st.plotly_chart(fig20)
                
#---------------------------------------------------------------------------------------------------                
                
    if ((task == "Worldwide")):
        
        st.info("This map shows the total confirmed cases/ total confirmed deaths of Ebola Virus Disease (EVD) outbreak in all affected countries.")
        selected= st.selectbox('Filter by Cases/Deaths:', options=['Total Confirmed Cases','Total Confirmed Deaths'])
           
        if ((selected == 'Total Confirmed Cases')):
            st.subheader("Total confirmed cases across countries")
            fig21 = go.Figure(data = go.Scattergeo(
            lon = global_C["lon"],
            lat = global_C["lat"],
            text = global_C["text"],
            mode = "markers",
            marker = dict(
                size = 12,
                opacity = 0.8,
                reversescale = False,
                autocolorscale = True,
                symbol = 'circle',
                line = dict(
                    width = 1,
                    color = 'rgba(102, 102, 102)'
                    ),
                cmin = 0,
                cmax = 14124,
                color= "#636EFA"
                )
                ))
            fig21.update_layout(
                geo = dict(
                    scope = "world",
                    showland = True,
                    showframe=False
                    )
                )
            st.plotly_chart(fig21)
                
            
        if ((selected == 'Total Confirmed Deaths')):
            st.subheader("Total confirmed deaths across countries")
            fig22 = go.Figure(data = go.Scattergeo(
            lon = global_D["lon"],
            lat = global_D["lat"],
            text = global_D["text"],
            mode = "markers",
            marker = dict(
                size = 12,
                opacity = 0.8,
                reversescale = False,
                autocolorscale = True,
                symbol = 'circle',
                line = dict(
                    width = 1,
                    color = 'rgba(102, 102, 102)'
                    ),
                cmin = 0,
                cmax = 4810,
                color= "#EF553B"
                )
                ))
            fig22.update_layout(
                geo = dict(
                    scope = "world",
                    showland = True,
                    showframe=False
                    )
                )
            st.plotly_chart(fig22)
                    

                           