# -*- coding: utf-8 -*-
"""
Created on Fri May 13 18:32:35 2022

@author: omart
"""

import streamlit as st
import pandas as pd
import numpy as np
import os
import glob
import json
import matplotlib.pyplot as plt

#JSON parsing
def get_files(filepath):
    all_files=[]
    for root,dirs,files in os.walk(filepath):
        files=glob.glob(os.path.join(root,"json"))
        for f in files:
            all_files.append(os.path.abspath(f))
        
        return all_files


def main():
    st.title('Grad Dashboard')
    menu = ["User","Aggergate"]
    choice = st.sidebar.selectbox("Menu",menu)
    """    
    json_folder_path = os.path.join("Dashboard")
# In order to get the list of all files that ends with ".json"
# we will get list of all files, and take only the ones that ends with "json"
    json_files = [ x for x in os.listdir(json_folder_path) if x.endswith("json") ]
    json_data = list()
    for json_file in json_files:
        json_file_path = os.path.join(json_folder_path, json_file)
        with open (json_file_path, "r") as f:
            json_data.append(json.load(f))
    user=pd.DataFrame()
    charachters=[]
    real=[]
    virtual=[]
    play=[]
    achieve=[]
    failed=[]
    idle=[]
    for i in range(len(json_data)):
        charachters.append(json_data[i]['user']['Passive']['Looking at']['Charachter'])
        real.append(json_data[i]['user']['Passive']['Looking at']['Enviornment']['Real'])
        virtual.append(json_data[i]['user']['Passive']['Looking at']['Enviornment']['Virtual'])
        play.append(json_data[i]['user']['Active']['Play'])
        achieve.append(json_data[i]['user']['Active']['Solve']['Achieve'])
        failed.append(json_data[i]['user']['Active']['Solve']['Failed'])
        idle.append(json_data[i]['user']['Passive']['Idle'])
    user['Charachters']=charachters
    user['Real']=real
    user['Virtual']=virtual
    user['Play']=play
    user['Achieve']=achieve
    user['Failed']=failed
    user['Idle']=idle
    
    if choice=='User':
        st.dataframe(user)
        st.bar_chart(user['Play'])
        st.bar_chart(user['Idle'])
        user_leaderboard=user[['Achieve']]
        user_leaderboard=user_leaderboard.sort_values('Achieve',ascending=False)
        st.dataframe(user_leaderboard)
    elif choice=='Aggergate':
        percent_success=(user.Achieve.sum()/len(user.Achieve)*5)*100
        percent_failure=(user.Failed.sum()/len(user.Achieve)*5)*100
        pieplot=[percent_success,percent_failure]
        fig1, ax1 = plt.subplots()
        ax1.pie(pieplot,labels=['Success','Failure'], autopct='%1.1f%%',startangle=90)
# Equal aspect ratio ensures that pie is drawn as a circle.
        centre_circle = plt.Circle((0, 0), 0.70, fc='white')
# Adding Circle in Pie chart
        fig1.gca().add_artist(centre_circle)
        st.pyplot(fig1)
        fig2, ax2 = plt.subplots()

        real_value=user['Real'].apply(lambda row :len(row))
        virutal_value=user['Virtual'].apply(lambda row :len(row))
        itemplot=[real_value.sum(),virutal_value.sum()]
        ax2.pie(itemplot,labels=['Real','Virutal'], autopct='%1.1f%%',startangle=90)
        centre_circle = plt.Circle((0, 0), 0.70, fc='white')
        fig2 = plt.gcf()
# Adding Circle in Pie chart
        fig2.gca().add_artist(centre_circle)
        Charile=[]
        Adam=[]
        ccount=0
        acount=0
        for index, row in user.iterrows():
            for r in row['Charachters']:
                if r=='Adam':
                    acount+=1
                else:
                    ccount+=1
            Adam.append(acount)
            Charile.append(ccount)
            acount=0
            ccount=0
            D={'Charile':sum(Charile),
         'Adam':sum(Adam)}
            st.bar(range(len(D)), list(D.values()), align='center')
            


"""