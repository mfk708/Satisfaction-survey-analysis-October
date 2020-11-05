# -*- coding: utf-8 -*-
"""
Created on Tue Sep 22 14:23:28 2020

@author: farrokhm
"""


import pandas as pd
from matplotlib import pyplot as plt
import numpy as np
from sklearn.linear_model import LinearRegression
import seaborn as sns
import matplotlib as mpl

header_list = ["Num", "Division",
                "Employee Category",
                "I am clear on the University of Calgary's key message",
                "I am clear on the mission and objectives of the Advancement Communications team",
                "I am clear on how performance will be measured... at the university",
                "I am clear on how performance will be measured... in Advancement Communications",
                "I am clear on how performance will be measured... in my division",
                "I am clear on how performance will be measured... in my role",
                "I understand what is expected of me in my role",
                "I understand what is expected of other people in other communications roles",
                "I feel I have the policies and processes needed to do my job",
                "I believe we have a respectful workplace... at the university",
                "I believe we have a respectful workplace... in Advancement Communications",
                "I believe we have a respectful workplace... in my division",
                "I believe we work as a team... at the university",
                "I believe we work as a team... in Advancement Communications",
                "I believe we work as a team... in my division",
                "I believe we have a workplace that values performance... at the university",
                "I believe we have a workplace that values performance... in Advancement Communications",
                "I believe we have a workplace that values performance... in my division",
                "Performance feedback from my manager is... clear",
                "Performance feedback from my manager is... consistent",
                "Performance feedback from my manager is... regular",
                "The volume of work I'm asked to perform is...",
                "I am provided formal development opportunities like access to courses and seminars",
                "I am provided informal development opportunities like coaching, stretch assignments or acting roles",
                "I have a good understanding of what my career path and/or career opportunities could be at the University of Calgary",
                "I am able to advance my career at the University of Calgary",
                "The work we do here at the University of Calgary matters",
                "The work we do here at Communications matters",
                "Overall, I believe that this is a good place to work",
                ]
df = pd.read_csv('ACT_Survey_Oct_2020_numeric.csv',names = header_list)
df.head(5)
df.drop([0], inplace=True)

df['Division'].value_counts()
round(df['Division'].astype(float).mean(), 1)
mpl.rc('font',family='Times New Roman')
plt.style.use('bmh')


df_division = df.groupby(['Division'])
df_creative = df_division.get_group('1')
df_content = df_division.get_group('2')
df_coordination = df_division.get_group('3')
df_digital = df_division.get_group('4')
df_services = df_division.get_group('6')

clear_msg_total_mean = round(df["I am clear on the University of Calgary's key message"].astype(float).mean(), 1)
clear_msg_creative_mean = round(df_creative["I am clear on the University of Calgary's key message"].astype(float).mean(), 1)
clear_msg_content_mean = round(df_content["I am clear on the University of Calgary's key message"].astype(float).mean(), 1)
clear_msg_digital_mean = round(df_digital["I am clear on the University of Calgary's key message"].astype(float).mean(), 1)
clear_msg_services_mean = round(df_services["I am clear on the University of Calgary's key message"].astype(float).mean(), 1)
clear_msg_coordination_mean = round(df_coordination["I am clear on the University of Calgary's key message"].astype(float).mean(), 1)

clear_msg = [clear_msg_total_mean,clear_msg_creative_mean,clear_msg_content_mean,clear_msg_digital_mean, clear_msg_services_mean, clear_msg_coordination_mean ]

#PLOT
opinion = ['Strongly disagree','Disagree','Neutral','Agree','Strongly agree']
teams = ['Adv. Comm', 'Creative', 'Content', 'Digital', 'Services', 'Coordination']



plt.figure(figsize=(35,17))
plt.bar(teams, clear_msg, color='#d6001c', label="Clear on University's key message")

plt.xticks(ticks=teams, labels=teams, fontsize = 45) #replaces the indexes with the ages on X axis.
plt.ylabel('Strongly disagree ... Strongly agree', fontsize=45)
#plt.title("Clear on University's key message", fontsize=45)
plt.tight_layout()
plt.legend(loc = 'upper left', fontsize=45)
plt.show() 


##CLEAR ON MISSION AND OBJECTIVES
clear_mission_total_mean = round(df["I am clear on the mission and objectives of the Advancement Communications team"].astype(float).mean(), 1)
clear_mission_creative_mean = round(df_creative["I am clear on the mission and objectives of the Advancement Communications team"].astype(float).mean(), 1)
clear_mission_content_mean = round(df_content["I am clear on the mission and objectives of the Advancement Communications team"].astype(float).mean(), 1)
clear_mission_digital_mean = round(df_digital["I am clear on the mission and objectives of the Advancement Communications team"].astype(float).mean(), 1)
clear_mission_services_mean = round(df_services["I am clear on the mission and objectives of the Advancement Communications team"].astype(float).mean(), 1)
clear_mission_coordination_mean = round(df_coordination["I am clear on the mission and objectives of the Advancement Communications team"].astype(float).mean(), 1)

clear_mission = [clear_mission_total_mean,clear_mission_creative_mean,clear_mission_content_mean,clear_mission_digital_mean, clear_mission_services_mean, clear_mission_coordination_mean]
clear_mission


##PLOT clear on message and mission combined
x_indexes = np.arange(len(teams)) #create a var (x_indexes) that is an array of values, which
#are a number version of x values. x_indexes is used instead of ages_x to create bar charts next to each other.
width=0.25 #defining the value that is going to be used as width of bars

plt.figure(figsize=(35,17))
plt.bar(x_indexes - width,clear_mission , width = width, color='#d6001c', label="Clear on U of C's key message")
plt.bar(x_indexes,clear_msg, width = width, color='#ffcd00',label ='Clear on Mission and objectives of the Adv Comm team')  

plt.xticks(ticks=x_indexes, labels=teams, fontsize=40) #replaces the indexes with the ages on X axis.
plt.yticks(fontsize = 25)

#plt.plot(teams,clear_mission_total_mean, color = 'blue', linewidth=10)

plt.ylabel('Strongly disagree ... Strongly agree', fontsize=40)
plt.tight_layout()
plt.legend(fontsize = 40)
plt.show()

##CLEAR ON PERFORMANCE

#UNIVERSITY
clear_perf_uni_total_mean = round(df["I am clear on how performance will be measured... at the university"].astype(float).mean(), 1)
clear_perf_uni_creative_mean = round(df_creative["I am clear on how performance will be measured... at the university"].astype(float).mean(), 1)
clear_perf_uni_content_mean = round(df_content["I am clear on how performance will be measured... at the university"].astype(float).mean(), 1)
clear_perf_uni_digital_mean = round(df_digital["I am clear on how performance will be measured... at the university"].astype(float).mean(), 1)
clear_perf_uni_services_mean = round(df_services["I am clear on how performance will be measured... at the university"].astype(float).mean(), 1)
clear_perf_uni_coordination_mean = round(df_coordination["I am clear on how performance will be measured... at the university"].astype(float).mean(), 1)

clear_per_uni = [clear_perf_uni_total_mean,clear_perf_uni_creative_mean,clear_perf_uni_content_mean,clear_perf_uni_digital_mean,clear_perf_uni_services_mean,clear_perf_uni_coordination_mean]
clear_per_uni


#ADVANCEMENT COMMUNICATIONS
clear_perf_adv_comm_total_mean = round(df["I am clear on how performance will be measured... in Advancement Communications"].astype(float).mean(), 1)
clear_perf_adv_comm_creative_mean = round(df_creative["I am clear on how performance will be measured... in Advancement Communications"].astype(float).mean(), 1)
clear_perf_adv_comm_content_mean = round(df_content["I am clear on how performance will be measured... in Advancement Communications"].astype(float).mean(), 1)
clear_perf_adv_comm_digital_mean = round(df_digital["I am clear on how performance will be measured... in Advancement Communications"].astype(float).mean(), 1)
clear_perf_adv_comm_services_mean = round(df_services["I am clear on how performance will be measured... in Advancement Communications"].astype(float).mean(), 1)
clear_perf_adv_comm_coordination_mean = round(df_coordination["I am clear on how performance will be measured... in Advancement Communications"].astype(float).mean(), 1)

clear_per_adv_comm = [clear_perf_adv_comm_total_mean,clear_perf_adv_comm_creative_mean,clear_perf_adv_comm_content_mean,clear_perf_adv_comm_digital_mean,clear_perf_adv_comm_services_mean,clear_perf_adv_comm_coordination_mean]
clear_per_adv_comm

#DIVISION
clear_perf_div_total_mean = round(df["I am clear on how performance will be measured... in my division"].astype(float).mean(), 1)
clear_perf_div_creative_mean = round(df_creative["I am clear on how performance will be measured... in my division"].astype(float).mean(), 1)
clear_perf_div_content_mean = round(df_content["I am clear on how performance will be measured... in my division"].astype(float).mean(), 1)
clear_perf_div_digital_mean = round(df_digital["I am clear on how performance will be measured... in my division"].astype(float).mean(), 1)
clear_perf_div_services_mean = round(df_services["I am clear on how performance will be measured... in my division"].astype(float).mean(), 1)
clear_perf_div_coordination_mean = round(df_coordination["I am clear on how performance will be measured... in my division"].astype(float).mean(), 1)

clear_per_div = [clear_perf_div_total_mean,clear_perf_div_creative_mean,clear_perf_div_content_mean,clear_perf_div_digital_mean,clear_perf_div_services_mean,clear_perf_div_coordination_mean]
clear_per_div

#Role
clear_perf_role_total_mean = round(df["I am clear on how performance will be measured... in my role"].astype(float).mean(), 1)
clear_perf_role_creative_mean = round(df_creative["I am clear on how performance will be measured... in my role"].astype(float).mean(), 1)
clear_perf_role_content_mean = round(df_content["I am clear on how performance will be measured... in my role"].astype(float).mean(), 1)
clear_perf_role_digital_mean = round(df_digital["I am clear on how performance will be measured... in my role"].astype(float).mean(), 1)
clear_perf_role_services_mean = round(df_services["I am clear on how performance will be measured... in my role"].astype(float).mean(), 1)
clear_perf_role_coordination_mean = round(df_coordination["I am clear on how performance will be measured... in my role"].astype(float).mean(), 1)

clear_per_role = [clear_perf_role_total_mean,clear_perf_role_creative_mean,clear_perf_role_content_mean,clear_perf_role_digital_mean,clear_perf_role_services_mean,clear_perf_role_coordination_mean]
clear_per_role

##COMBINED PLOT
x_indexes = np.arange(len(teams)) #create a var (x_indexes) that is an array of values, which
#are a number version of x values. x_indexes is used instead of ages_x to create bar charts next to each other.
width=0.15 #defining the value that is going to be used as width of bars

plt.figure(figsize=(35,17))
plt.bar(x_indexes - width,clear_per_uni , width = width, color='#d6001c', label="Clear on performance at University")
plt.bar(x_indexes,clear_per_adv_comm, width = width, color='#ffcd00',label ='Clear on performance in Adv Comm')  
plt.bar(x_indexes + width,clear_per_div , width = width, color='#ff671f', label="Clear on performance in division")
plt.bar(x_indexes + width*2,clear_per_role , width = width, color='#ed0a72', label="Clear on performance in role")
  
#ax.tick_params(axis="x", labelsize=8)
#ax.tick_params(axis="y", labelsize=16)
plt.xticks(ticks=x_indexes, labels=teams, fontsize = 40) #replaces the indexes with the ages on X axis.
plt.yticks(fontsize = 30)

#plt.plot(teams,clear_mission_total_mean, color = 'blue', linewidth=10)

plt.ylabel('1: Strongly disagree ........... 5: Strongly agree', fontsize=40)
plt.tight_layout()
plt.legend(fontsize = 40)
plt.show()


##EXPECTATIONS AND POLICIES AND PROCESSES

##EXPECTED OF ME IN MY ROLE
expected_my_role_total_mean = round(df["I understand what is expected of me in my role"].astype(float).mean(), 1)
expected_my_role_creative_mean = round(df_creative["I understand what is expected of me in my role"].astype(float).mean(), 1)
expected_my_role_content_mean = round(df_content["I understand what is expected of me in my role"].astype(float).mean(), 1)
expected_my_role_digital_mean = round(df_digital["I understand what is expected of me in my role"].astype(float).mean(), 1)
expected_my_role_services_mean = round(df_services["I understand what is expected of me in my role"].astype(float).mean(), 1)
expected_my_role_coordination_mean = round(df_coordination["I understand what is expected of me in my role"].astype(float).mean(), 1)

expected_my_role = [expected_my_role_total_mean,expected_my_role_creative_mean,expected_my_role_content_mean,expected_my_role_digital_mean,expected_my_role_services_mean,expected_my_role_coordination_mean ]
expected_my_role

##EXPECTED OF OTHER PEOPLE IN OTHER ROLES
expected_other_role_total_mean = round(df["I understand what is expected of other people in other communications roles"].astype(float).mean(), 1)
expected_other_role_creative_mean = round(df_creative["I understand what is expected of other people in other communications roles"].astype(float).mean(), 1)
expected_other_role_content_mean = round(df_content["I understand what is expected of other people in other communications roles"].astype(float).mean(), 1)
expected_other_role_digital_mean = round(df_digital["I understand what is expected of other people in other communications roles"].astype(float).mean(), 1)
expected_other_role_services_mean = round(df_services["I understand what is expected of other people in other communications roles"].astype(float).mean(), 1)
expected_other_role_coordination_mean = round(df_coordination["I understand what is expected of other people in other communications roles"].astype(float).mean(), 1)

expected_other_role = [expected_other_role_total_mean,expected_other_role_creative_mean,expected_other_role_content_mean,expected_other_role_digital_mean,expected_other_role_services_mean,expected_other_role_coordination_mean]
expected_other_role

##POLICIES AND PROCESSES
policies_total_mean = round(df["I feel I have the policies and processes needed to do my job"].astype(float).mean(), 1)
policies_creative_mean = round(df_creative["I feel I have the policies and processes needed to do my job"].astype(float).mean(), 1)
policies_content_mean = round(df_content["I feel I have the policies and processes needed to do my job"].astype(float).mean(), 1)
policies_digital_mean = round(df_digital["I feel I have the policies and processes needed to do my job"].astype(float).mean(), 1)
policies_services_mean = round(df_services["I feel I have the policies and processes needed to do my job"].astype(float).mean(), 1)
policies_coordination_mean = round(df_coordination["I feel I have the policies and processes needed to do my job"].astype(float).mean(), 1)

policies = [policies_total_mean,policies_creative_mean,policies_content_mean,policies_digital_mean,policies_services_mean,policies_coordination_mean]
policies

##COMBINED PLOT
x_indexes = np.arange(len(teams)) #create a var (x_indexes) that is an array of values, which
#are a number version of x values. x_indexes is used instead of ages_x to create bar charts next to each other.
width=0.20 #defining the value that is going to be used as width of bars

plt.figure(figsize=(35,17))
plt.bar(x_indexes - width,expected_my_role , width = width, color='#d6001c', label="I understand what is expected of me in my role")
plt.bar(x_indexes , expected_other_role , width = width, color='#ffcd00', label="I understand what is expected of other people in other comm. roles")
plt.bar(x_indexes + width,policies, width = width, color='#ff671f',label ='I feel I have the policies and processes needed to do my job')  

  
plt.xticks(ticks=x_indexes, labels=teams, fontsize=40) #replaces the indexes with the ages on X axis.
plt.yticks(fontsize = 30)


#plt.plot(teams,clear_mission_total_mean, color = 'blue', linewidth=10)

plt.ylabel('1: Strongly disagree ........... 5: Strongly agree', fontsize=40)
plt.tight_layout()
plt.legend(fontsize = 35)
plt.show()


##WORK ENVIRONMENT

#RESPECTFUL WORKPLACE
#UNI
respectful_uni_total_mean = round(df["I believe we have a respectful workplace... at the university"].astype(float).mean(), 1)
respectful_uni_creative_mean = round(df_creative["I believe we have a respectful workplace... at the university"].astype(float).mean(), 1)
respectful_uni_content_mean = round(df_content["I believe we have a respectful workplace... at the university"].astype(float).mean(), 1)
respectful_uni_digital_mean = round(df_digital["I believe we have a respectful workplace... at the university"].astype(float).mean(), 1)
respectful_uni_services_mean = round(df_services["I believe we have a respectful workplace... at the university"].astype(float).mean(), 1)
respectful_uni_coordination_mean = round(df_coordination["I believe we have a respectful workplace... at the university"].astype(float).mean(), 1)

respectful_uni = [respectful_uni_total_mean,respectful_uni_creative_mean,respectful_uni_content_mean,respectful_uni_digital_mean,respectful_uni_services_mean,respectful_uni_coordination_mean]
respectful_uni

#ADVANCEMENT COMMUNICATIONS
respectful_adv_comm_total_mean = round(df["I believe we have a respectful workplace... in Advancement Communications"].astype(float).mean(), 1)
respectful_adv_comm_creative_mean = round(df_creative["I believe we have a respectful workplace... in Advancement Communications"].astype(float).mean(), 1)
respectful_adv_comm_content_mean = round(df_content["I believe we have a respectful workplace... in Advancement Communications"].astype(float).mean(), 1)
respectful_adv_comm_digital_mean = round(df_digital["I believe we have a respectful workplace... in Advancement Communications"].astype(float).mean(), 1)
respectful_adv_comm_services_mean = round(df_services["I believe we have a respectful workplace... in Advancement Communications"].astype(float).mean(), 1)
respectful_adv_comm_coordination_mean = round(df_coordination["I believe we have a respectful workplace... in Advancement Communications"].astype(float).mean(), 1)

respectful_adv_comm = [respectful_adv_comm_total_mean,respectful_adv_comm_creative_mean,respectful_adv_comm_content_mean,respectful_adv_comm_digital_mean,respectful_adv_comm_services_mean,respectful_adv_comm_coordination_mean]
respectful_adv_comm

#MY DIVISION
respectful_div_total_mean = round(df["I believe we have a respectful workplace... in my division"].astype(float).mean(), 1)
respectful_div_creative_mean = round(df_creative["I believe we have a respectful workplace... in my division"].astype(float).mean(), 1)
respectful_div_content_mean = round(df_content["I believe we have a respectful workplace... in my division"].astype(float).mean(), 1)
respectful_div_digital_mean = round(df_digital["I believe we have a respectful workplace... in my division"].astype(float).mean(), 1)
respectful_div_services_mean = round(df_services["I believe we have a respectful workplace... in my division"].astype(float).mean(), 1)
respectful_div_coordination_mean = round(df_coordination["I believe we have a respectful workplace... in my division"].astype(float).mean(), 1)

respectful_div = [respectful_div_total_mean,respectful_div_creative_mean,respectful_div_content_mean,respectful_div_digital_mean,respectful_div_services_mean,respectful_div_coordination_mean]
respectful_div


##COMBINED PLOT
x_indexes = np.arange(len(teams)) #create a var (x_indexes) that is an array of values, which
#are a number version of x values. x_indexes is used instead of ages_x to create bar charts next to each other.
width=0.15 #defining the value that is going to be used as width of bars

plt.figure(figsize=(35,17))
plt.bar(x_indexes - width,respectful_uni , width = width, color='#d6001c', label="Respectful workplace at the university")
plt.bar(x_indexes,respectful_adv_comm, width = width, color='#ffcd00',label ='Respectful workplace in Adv. Comm.')  
plt.bar(x_indexes + width,respectful_div , width = width, color='#ff671f', label="Respectful workplace in my division")
  

plt.xticks(ticks=x_indexes, labels=teams, fontsize=40) #replaces the indexes with the ages on X axis.
plt.yticks(fontsize = 30)


#plt.plot(teams,clear_mission_total_mean, color = 'blue', linewidth=10)

plt.ylabel('1: Strongly disagree ........... 5: Strongly agree', fontsize=40)
plt.tight_layout()
plt.legend(fontsize = 40)
plt.show()


##TEAMWORK

#UNI
teamwork_uni_total_mean = round(df["I believe we work as a team... at the university"].astype(float).mean(), 1)
teamwork_uni_creative_mean = round(df_creative["I believe we work as a team... at the university"].astype(float).mean(), 1)
teamwork_uni_content_mean = round(df_content["I believe we work as a team... at the university"].astype(float).mean(), 1)
teamwork_uni_digital_mean = round(df_digital["I believe we work as a team... at the university"].astype(float).mean(), 1)
teamwork_uni_services_mean = round(df_services["I believe we work as a team... at the university"].astype(float).mean(), 1)
teamwork_uni_coordination_mean = round(df_coordination["I believe we work as a team... at the university"].astype(float).mean(), 1)

teamwork_uni = [teamwork_uni_total_mean,teamwork_uni_creative_mean,teamwork_uni_content_mean,teamwork_uni_digital_mean,teamwork_uni_services_mean,teamwork_uni_coordination_mean]
teamwork_uni


#ADVANCEMENT COMMUNICATIONS
teamwork_adv_comm_total_mean = round(df["I believe we work as a team... in Advancement Communications"].astype(float).mean(), 1)
teamwork_adv_comm_creative_mean = round(df_creative["I believe we work as a team... in Advancement Communications"].astype(float).mean(), 1)
teamwork_adv_comm_content_mean = round(df_content["I believe we work as a team... in Advancement Communications"].astype(float).mean(), 1)
teamwork_adv_comm_digital_mean = round(df_digital["I believe we work as a team... in Advancement Communications"].astype(float).mean(), 1)
teamwork_adv_comm_services_mean = round(df_services["I believe we work as a team... in Advancement Communications"].astype(float).mean(), 1)
teamwork_adv_comm_coordination_mean = round(df_coordination["I believe we work as a team... in Advancement Communications"].astype(float).mean(), 1)

teamwork_adv_comm = [teamwork_adv_comm_total_mean,teamwork_adv_comm_creative_mean,teamwork_adv_comm_content_mean,teamwork_adv_comm_digital_mean,teamwork_adv_comm_services_mean,teamwork_adv_comm_coordination_mean]
teamwork_adv_comm

#MY DIVISION
teamwork_div_total_mean = round(df["I believe we work as a team... in my division"].astype(float).mean(), 1)
teamwork_div_creative_mean = round(df_creative["I believe we work as a team... in my division"].astype(float).mean(), 1)
teamwork_div_content_mean = round(df_content["I believe we work as a team... in my division"].astype(float).mean(), 1)
teamwork_div_digital_mean = round(df_digital["I believe we work as a team... in my division"].astype(float).mean(), 1)
teamwork_div_services_mean = round(df_services["I believe we work as a team... in my division"].astype(float).mean(), 1)
teamwork_div_coordination_mean = round(df_coordination["I believe we work as a team... in my division"].astype(float).mean(), 1)

teamwork_div = [teamwork_div_total_mean,teamwork_div_creative_mean,teamwork_div_content_mean,teamwork_div_digital_mean,teamwork_div_services_mean,teamwork_div_coordination_mean]
teamwork_div


##COMBINED PLOT
x_indexes = np.arange(len(teams)) #create a var (x_indexes) that is an array of values, which
#are a number version of x values. x_indexes is used instead of ages_x to create bar charts next to each other.
width=0.15 #defining the value that is going to be used as width of bars

plt.figure(figsize=(35,17))
plt.bar(x_indexes - width,teamwork_uni , width = width, color='#d6001c', label="We work as a team at the University")
plt.bar(x_indexes,teamwork_adv_comm, width = width, color='#ffcd00',label ='We work as a team in Adv. Comm.')  
plt.bar(x_indexes + width,teamwork_div , width = width, color='#ff671f', label="We work as a team in my division")
  
plt.xticks(ticks=x_indexes, labels=teams, fontsize=40) #replaces the indexes with the ages on X axis.
plt.yticks(fontsize = 30)


#plt.plot(teams,clear_mission_total_mean, color = 'blue', linewidth=10)

plt.ylabel('1: Strongly disagree ........... 5: Strongly agree', fontsize=40)
plt.tight_layout()
plt.legend(loc ='upper left', fontsize = 40)
plt.show()


##VALUE PERFORMANCE
#UNI
perf_uni_total_mean = round(df["I believe we have a workplace that values performance... at the university"].astype(float).mean(), 1)
perf_uni_creative_mean = round(df_creative["I believe we have a workplace that values performance... at the university"].astype(float).mean(), 1)
perf_uni_content_mean = round(df_content["I believe we have a workplace that values performance... at the university"].astype(float).mean(), 1)
perf_uni_digital_mean = round(df_digital["I believe we have a workplace that values performance... at the university"].astype(float).mean(), 1)
perf_uni_services_mean = round(df_services["I believe we have a workplace that values performance... at the university"].astype(float).mean(), 1)
perf_uni_coordination_mean = round(df_coordination["I believe we have a workplace that values performance... at the university"].astype(float).mean(), 1)

perf_uni = [perf_uni_total_mean,perf_uni_creative_mean,perf_uni_content_mean,perf_uni_digital_mean,perf_uni_services_mean,perf_uni_coordination_mean]
perf_uni


#ADVANCEMENT COMMUNICATIONS
perf_adv_comm_total_mean = round(df["I believe we have a workplace that values performance... in Advancement Communications"].astype(float).mean(), 1)
perf_adv_comm_creative_mean = round(df_creative["I believe we have a workplace that values performance... in Advancement Communications"].astype(float).mean(), 1)
perf_adv_comm_content_mean = round(df_content["I believe we have a workplace that values performance... in Advancement Communications"].astype(float).mean(), 1)
perf_adv_comm_digital_mean = round(df_digital["I believe we have a workplace that values performance... in Advancement Communications"].astype(float).mean(), 1)
perf_adv_comm_services_mean = round(df_services["I believe we have a workplace that values performance... in Advancement Communications"].astype(float).mean(), 1)
perf_adv_comm_coordination_mean = round(df_coordination["I believe we have a workplace that values performance... in Advancement Communications"].astype(float).mean(), 1)

perf_adv_comm = [perf_adv_comm_total_mean,perf_adv_comm_creative_mean,perf_adv_comm_content_mean,perf_adv_comm_digital_mean,perf_adv_comm_services_mean,perf_adv_comm_coordination_mean]
perf_adv_comm

#MY DIVISION
perf_div_total_mean = round(df["I believe we have a workplace that values performance... in my division"].astype(float).mean(), 1)
perf_div_creative_mean = round(df_creative["I believe we have a workplace that values performance... in my division"].astype(float).mean(), 1)
perf_div_content_mean = round(df_content["I believe we have a workplace that values performance... in my division"].astype(float).mean(), 1)
perf_div_digital_mean = round(df_digital["I believe we have a workplace that values performance... in my division"].astype(float).mean(), 1)
perf_div_services_mean = round(df_services["I believe we have a workplace that values performance... in my division"].astype(float).mean(), 1)
perf_div_coordination_mean = round(df_coordination["I believe we have a workplace that values performance... in my division"].astype(float).mean(), 1)

perf_div = [perf_div_total_mean,perf_div_creative_mean,perf_div_content_mean,perf_div_digital_mean,perf_div_services_mean,perf_div_coordination_mean]
perf_div


##COMBINED PLOT
x_indexes = np.arange(len(teams)) #create a var (x_indexes) that is an array of values, which
#are a number version of x values. x_indexes is used instead of ages_x to create bar charts next to each other.
width=0.15 #defining the value that is going to be used as width of bars

plt.figure(figsize=(35,17))
plt.bar(x_indexes - width,perf_uni , width = width, color='#d6001c', label="University values performance")
plt.bar(x_indexes,perf_adv_comm, width = width, color='#ffcd00',label ='Adv. Comm.values performance')  
plt.bar(x_indexes + width,perf_div , width = width, color='#ff671f', label="My division values performance")
  

plt.xticks(ticks=x_indexes, labels=teams,fontsize = 40 ) #replaces the indexes with the ages on X axis.
plt.yticks(fontsize = 30)


#plt.plot(teams,clear_mission_total_mean, color = 'blue', linewidth=10)

plt.ylabel('1: Strongly disagree ........... 5: Strongly agree', fontsize=40)
plt.tight_layout()
plt.legend(fontsize = 40)
plt.show()

##PERFORMANCE FEEDBACK FROM MANAGER

 ##PERFORMANCE FEEDBACK: CLEAR
fdbck_clear_total_mean = round(df["Performance feedback from my manager is... clear"].astype(float).mean(), 1)
fdbck_clear_creative_mean = round(df_creative["Performance feedback from my manager is... clear"].astype(float).mean(), 1)
fdbck_clear_content_mean = round(df_content["Performance feedback from my manager is... clear"].astype(float).mean(), 1)
fdbck_clear_digital_mean = round(df_digital["Performance feedback from my manager is... clear"].astype(float).mean(), 1)
fdbck_clear_services_mean = round(df_services["Performance feedback from my manager is... clear"].astype(float).mean(), 1)
fdbck_clear_coordination_mean = round(df_coordination["Performance feedback from my manager is... clear"].astype(float).mean(), 1)

fdbck_clear = [fdbck_clear_total_mean,fdbck_clear_creative_mean,fdbck_clear_content_mean,fdbck_clear_digital_mean,fdbck_clear_services_mean,fdbck_clear_coordination_mean]
fdbck_clear

##PERFORMANCE FEEDBACK: CONSISTENT
fdbck_consistent_total_mean = round(df["Performance feedback from my manager is... consistent"].astype(float).mean(), 1)
fdbck_consistent_creative_mean = round(df_creative["Performance feedback from my manager is... consistent"].astype(float).mean(), 1)
fdbck_consistent_content_mean = round(df_content["Performance feedback from my manager is... consistent"].astype(float).mean(), 1)
fdbck_consistent_digital_mean = round(df_digital["Performance feedback from my manager is... consistent"].astype(float).mean(), 1)
fdbck_consistent_services_mean = round(df_services["Performance feedback from my manager is... consistent"].astype(float).mean(), 1)
fdbck_consistent_coordination_mean = round(df_coordination["Performance feedback from my manager is... consistent"].astype(float).mean(), 1)

fdbck_consistent = [fdbck_consistent_total_mean,fdbck_consistent_creative_mean,fdbck_consistent_content_mean,fdbck_consistent_digital_mean,fdbck_consistent_services_mean,fdbck_consistent_coordination_mean]
fdbck_consistent

##PERFORMANCE FEEDBACK: REGULAR
fdbck_regular_total_mean = round(df["Performance feedback from my manager is... regular"].astype(float).mean(), 1)
fdbck_regular_creative_mean = round(df_creative["Performance feedback from my manager is... regular"].astype(float).mean(), 1)
fdbck_regular_content_mean = round(df_content["Performance feedback from my manager is... regular"].astype(float).mean(), 1)
fdbck_regular_digital_mean = round(df_digital["Performance feedback from my manager is... regular"].astype(float).mean(), 1)
fdbck_regular_services_mean = round(df_services["Performance feedback from my manager is... regular"].astype(float).mean(), 1)
fdbck_regular_coordination_mean = round(df_coordination["Performance feedback from my manager is... regular"].astype(float).mean(), 1)

fdbck_regular = [fdbck_regular_total_mean,fdbck_regular_creative_mean,fdbck_regular_content_mean,fdbck_regular_digital_mean,fdbck_regular_services_mean,fdbck_regular_coordination_mean]
fdbck_regular


##COMBINED PLOT
x_indexes = np.arange(len(teams)) #create a var (x_indexes) that is an array of values, which
#are a number version of x values. x_indexes is used instead of ages_x to create bar charts next to each other.
width=0.15 #defining the value that is going to be used as width of bars

plt.figure(figsize=(35,17))
plt.bar(x_indexes - width,fdbck_clear , width = width, color='#d6001c', label="CLEAR performance feedback")
plt.bar(x_indexes,fdbck_consistent , width = width, color='#ffcd00', label="CONSISTENT performance feedback")
plt.bar(x_indexes + width,fdbck_regular, width = width, color='#ff671f',label ='REGULAR performance feedback')  
  

plt.xticks(ticks=x_indexes, labels=teams, fontsize = 40) #replaces the indexes with the ages on X axis.
plt.yticks(fontsize = 30)


#plt.plot(teams,clear_mission_total_mean, color = 'blue', linewidth=10)

plt.ylabel('1: Strongly disagree ........... 5: Strongly agree', fontsize=40)
plt.tight_layout()
plt.legend(loc = 'upper left', fontsize = 40)
plt.show()

##WORK VOLUME
workload_total_mean = round(df["The volume of work I'm asked to perform is..."].astype(float).mean(), 1)
workload_creative_mean = round(df_creative["The volume of work I'm asked to perform is..."].astype(float).mean(), 1)
workload_content_mean = round(df_content["The volume of work I'm asked to perform is..."].astype(float).mean(), 1)
workload_digital_mean = round(df_digital["The volume of work I'm asked to perform is..."].astype(float).mean(), 1)
workload_services_mean = round(df_services["The volume of work I'm asked to perform is..."].astype(float).mean(), 1)
workload_coordination_mean = round(df_coordination["The volume of work I'm asked to perform is..."].astype(float).mean(), 1)

workload = [workload_total_mean,workload_creative_mean,workload_content_mean,workload_digital_mean,workload_services_mean,workload_coordination_mean ]
workload


##COMBINED PLOT
x_indexes = np.arange(len(teams)) #create a var (x_indexes) that is an array of values, which
#are a number version of x values. x_indexes is used instead of ages_x to create bar charts next to each other.
width=0.45 #defining the value that is going to be used as width of bars

plt.figure(figsize=(25,12.5))
plt.bar(x_indexes,workload, width = width, color='#d6001c', label="My workload is ...")
  
  

plt.xticks(ticks=x_indexes, labels=teams, fontsize = 40) #replaces the indexes with the ages on X axis.
plt.yticks(fontsize = 25)
plt.ylabel('1: Too heavy ........ 3: Moderate..........5: Too light', fontsize=30)
plt.tight_layout()
plt.legend(fontsize = 40)
plt.show()

##PROFESSIONAL DEVELOPMENT

##FORMAL DEVELOPMENT OPPORTUNITIES
formal_dev_total_mean = round(df["I am provided formal development opportunities like access to courses and seminars"].astype(float).mean(), 1)
formal_dev_creative_mean = round(df_creative["I am provided formal development opportunities like access to courses and seminars"].astype(float).mean(), 1)
formal_dev_content_mean = round(df_content["I am provided formal development opportunities like access to courses and seminars"].astype(float).mean(), 1)
formal_dev_digital_mean = round(df_digital["I am provided formal development opportunities like access to courses and seminars"].astype(float).mean(), 1)
formal_dev_services_mean = round(df_services["I am provided formal development opportunities like access to courses and seminars"].astype(float).mean(), 1)
formal_dev_coordination_mean = round(df_coordination["I am provided formal development opportunities like access to courses and seminars"].astype(float).mean(), 1)

formal_dev = [formal_dev_total_mean,formal_dev_creative_mean,formal_dev_content_mean,formal_dev_digital_mean,formal_dev_services_mean,formal_dev_coordination_mean]
formal_dev

##INFORMAL DEVELOPMENT OPPORTUNITIES
informal_dev_total_mean = round(df["I am provided informal development opportunities like coaching, stretch assignments or acting roles"].astype(float).mean(), 1)
informal_dev_creative_mean = round(df_creative["I am provided informal development opportunities like coaching, stretch assignments or acting roles"].astype(float).mean(), 1)
informal_dev_content_mean = round(df_content["I am provided informal development opportunities like coaching, stretch assignments or acting roles"].astype(float).mean(), 1)
informal_dev_digital_mean = round(df_digital["I am provided informal development opportunities like coaching, stretch assignments or acting roles"].astype(float).mean(), 1)
informal_dev_services_mean = round(df_services["I am provided informal development opportunities like coaching, stretch assignments or acting roles"].astype(float).mean(), 1)
informal_dev_coordination_mean = round(df_coordination["I am provided informal development opportunities like coaching, stretch assignments or acting roles"].astype(float).mean(), 1)

informal_dev = [informal_dev_total_mean,informal_dev_creative_mean,informal_dev_content_mean,informal_dev_digital_mean,informal_dev_services_mean,informal_dev_coordination_mean]
informal_dev



##COMBINED PLOT
x_indexes = np.arange(len(teams)) #create a var (x_indexes) that is an array of values, which
#are a number version of x values. x_indexes is used instead of ages_x to create bar charts next to each other.
width=0.20 #defining the value that is going to be used as width of bars

plt.figure(figsize=(30,15))
plt.bar(x_indexes - width,formal_dev , width = width, color='#d6001c', label="Provided formal development opportunities")
plt.bar(x_indexes,informal_dev , width = width, color='#ffcd00', label="Provided INformal development opportunities")
  
plt.xticks(ticks=x_indexes, labels=teams, fontsize = 40) #replaces the indexes with the ages on X axis.
plt.yticks(fontsize = 25)

#plt.plot(teams,clear_mission_total_mean, color = 'blue', linewidth=10)

plt.ylabel('1: Strongly disagree ........... 5: Strongly agree', fontsize=40)
plt.tight_layout()
plt.legend(fontsize = 40)
plt.show()
 
##CAREER PATH AND ADVANCEMENT
##CAREER PATH
career_path_total_mean = round(df["I have a good understanding of what my career path and/or career opportunities could be at the University of Calgary"].astype(float).mean(), 1)
career_path_creative_mean = round(df_creative["I have a good understanding of what my career path and/or career opportunities could be at the University of Calgary"].astype(float).mean(), 1)
career_path_content_mean = round(df_content["I have a good understanding of what my career path and/or career opportunities could be at the University of Calgary"].astype(float).mean(), 1)
career_path_digital_mean = round(df_digital["I have a good understanding of what my career path and/or career opportunities could be at the University of Calgary"].astype(float).mean(), 1)
career_path_services_mean = round(df_services["I have a good understanding of what my career path and/or career opportunities could be at the University of Calgary"].astype(float).mean(), 1)
career_path_coordination_mean = round(df_coordination["I have a good understanding of what my career path and/or career opportunities could be at the University of Calgary"].astype(float).mean(), 1)

career_path = [career_path_total_mean,career_path_creative_mean,career_path_content_mean,career_path_digital_mean,career_path_services_mean,career_path_coordination_mean]
career_path

##ADVANCE CAREER
career_adv_total_mean = round(df["I am able to advance my career at the University of Calgary"].astype(float).mean(), 1)
career_adv_creative_mean = round(df_creative["I am able to advance my career at the University of Calgary"].astype(float).mean(), 1)
career_adv_content_mean = round(df_content["I am able to advance my career at the University of Calgary"].astype(float).mean(), 1)
career_adv_digital_mean = round(df_digital["I am able to advance my career at the University of Calgary"].astype(float).mean(), 1)
career_adv_services_mean = round(df_services["I am able to advance my career at the University of Calgary"].astype(float).mean(), 1)
career_adv_coordination_mean = round(df_coordination["I am able to advance my career at the University of Calgary"].astype(float).mean(), 1)

career_adv = [career_adv_total_mean,career_adv_creative_mean,career_adv_content_mean,career_adv_digital_mean,career_adv_services_mean,career_adv_coordination_mean]
career_adv



##COMBINED PLOT
x_indexes = np.arange(len(teams)) #create a var (x_indexes) that is an array of values, which
#are a number version of x values. x_indexes is used instead of ages_x to create bar charts next to each other.
width=0.20 #defining the value that is going to be used as width of bars

plt.figure(figsize=(35,17))
plt.bar(x_indexes - width,career_path , width = width, color='#d6001c', label="I have a good understanding of my career path")
plt.bar(x_indexes,career_adv , width = width, color='#ffcd00', label="I'm able to advance my career at UCalgary")
  
plt.xticks(ticks=x_indexes, labels=teams, fontsize = 40) #replaces the indexes with the ages on X axis.
plt.yticks(fontsize = 25)


#plt.plot(teams,clear_mission_total_mean, color = 'blue', linewidth=10)

plt.ylabel('1: Strongly disagree ........... 5: Strongly agree', fontsize=40)
plt.tight_layout()
plt.legend(fontsize = 40)
plt.show()

 
##BOTTOM LINE
 ##WORK MATTERS: UNI
work_matters_total_mean = round(df["The work we do here at the University of Calgary matters"].astype(float).mean(), 1)
work_matters_creative_mean = round(df_creative["The work we do here at the University of Calgary matters"].astype(float).mean(), 1)
work_matters_content_mean = round(df_content["The work we do here at the University of Calgary matters"].astype(float).mean(), 1)
work_matters_digital_mean = round(df_digital["The work we do here at the University of Calgary matters"].astype(float).mean(), 1)
work_matters_services_mean = round(df_services["The work we do here at the University of Calgary matters"].astype(float).mean(), 1)
work_matters_coordination_mean = round(df_coordination["The work we do here at the University of Calgary matters"].astype(float).mean(), 1)

work_matters = [work_matters_total_mean,work_matters_creative_mean,work_matters_content_mean,work_matters_digital_mean,work_matters_services_mean,work_matters_coordination_mean]
work_matters

##WORK MATTERS:COMMUNICATIONS
work_matters_comm_total_mean = round(df["The work we do here at Communications matters"].astype(float).mean(), 1)
work_matters_comm_creative_mean = round(df_creative["The work we do here at Communications matters"].astype(float).mean(), 1)
work_matters_comm_content_mean = round(df_content["The work we do here at Communications matters"].astype(float).mean(), 1)
work_matters_comm_digital_mean = round(df_digital["The work we do here at Communications matters"].astype(float).mean(), 1)
work_matters_comm_services_mean = round(df_services["The work we do here at Communications matters"].astype(float).mean(), 1)
work_matters_comm_coordination_mean = round(df_coordination["The work we do here at Communications matters"].astype(float).mean(), 1)

work_matters_comm = [work_matters_comm_total_mean,work_matters_comm_creative_mean,work_matters_comm_content_mean,work_matters_comm_digital_mean,work_matters_comm_services_mean,work_matters_comm_coordination_mean]
work_matters_comm

##GOOD PLACE TO WORK
work_good_total_mean = round(df["Overall, I believe that this is a good place to work"].astype(float).mean(), 1)
work_good_creative_mean = round(df_creative["Overall, I believe that this is a good place to work"].astype(float).mean(), 1)
work_good_content_mean = round(df_content["Overall, I believe that this is a good place to work"].astype(float).mean(), 1)
work_good_digital_mean = round(df_digital["Overall, I believe that this is a good place to work"].astype(float).mean(), 1)
work_good_services_mean = round(df_services["Overall, I believe that this is a good place to work"].astype(float).mean(), 1)
work_good_coordination_mean = round(df_coordination["Overall, I believe that this is a good place to work"].astype(float).mean(), 1)

work_good = [work_good_total_mean,work_good_creative_mean,work_good_content_mean,work_good_digital_mean,work_good_services_mean,work_good_coordination_mean]
work_good


##COMBINED PLOT
x_indexes = np.arange(len(teams)) #create a var (x_indexes) that is an array of values, which
#are a number version of x values. x_indexes is used instead of ages_x to create bar charts next to each other.
width=0.15 #defining the value that is going to be used as width of bars

plt.figure(figsize=(40,20))
plt.bar(x_indexes - width,work_matters , width = width, color='#d6001c', label="The work we do here at the University of Calgary matters")
plt.bar(x_indexes,work_matters_comm , width = width, color='#ffcd00', label="The work we do here at Communications matters")
plt.bar(x_indexes + width,work_good, width = width, color='#ff671f',label ='Overall, I believe that this is a good place to work')  
  

plt.xticks(ticks=x_indexes, labels=teams, fontsize = 40) #replaces the indexes with the ages on X axis.
plt.yticks(fontsize = 25)

#plt.plot(teams,clear_mission_total_mean, color = 'blue', linewidth=10)

plt.ylabel('1: Strongly disagree ........... 5: Strongly agree', fontsize=40)
plt.tight_layout()
plt.legend(loc = 'upper left',fontsize = 40)
plt.show()
                
##SEASONAL QUESTIONS
"I know my target audience",
"I receive feedback from my target audience


                
 