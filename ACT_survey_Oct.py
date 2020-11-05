# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
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
df = pd.read_csv('ACT_Survey_Oct_2020.csv',names = header_list)
df.drop([0], inplace=True)
df['Division'].head()
df['Division'].value_counts()
df.columns
df.head(5)
csfont = {'fontname':'Times New Roman'}
mpl.rc('font',family='Times New Roman')



df["I am clear on the University of Calgary's key message"].value_counts(normalize=True)
a1 = df["I am clear on the University of Calgary's key message"].value_counts()
a1
Agree = a1.loc['Agree']
Neutral = a1.loc['Neither agree nor disagree']
Disagree = a1.loc['Disagree']
Strongly_agree= a1.loc['Strongly agree']
Strongly_disagree = a1.loc['Strongly disagree']
Strongly_disagree = 0
Agree_percent = (Agree/(Agree+Neutral+Disagree+Strongly_agree+Strongly_disagree))*100

Disagree_percent = (Disagree/(Agree+Neutral+Disagree+Strongly_agree+Strongly_disagree))*100

Neutral_percent = (Neutral/(Agree+Neutral+Disagree+Strongly_agree+Strongly_disagree))*100

Strongly_agree_percent = (Strongly_agree/(Agree+Neutral+Disagree+Strongly_agree+Strongly_disagree))*100

Strongly_disagree_percent = (Strongly_disagree/(Agree+Neutral+Disagree+Strongly_agree+Strongly_disagree))*100

key_message_prcnt = [Strongly_disagree_percent,Disagree_percent,Neutral_percent,Agree_percent,Strongly_agree_percent]
key_message_prcnt
#PLOTTING THE 'KEY MESSAGE' OUTCOME SEPERATELY
colors = ['#d6001c', '#ffcd00', '#ff671f', '#ed0a72', '#ffe57b']
plt.style.use('bmh')
fig = plt.figure()
ax = fig.add_axes([0,0,1,1])
opinion = ['Strongly disagree','Disagree','Neutral','Agree','Strongly agree']
key_message_prcnt = [Strongly_disagree_percent,Disagree_percent,Neutral_percent,Agree_percent,Strongly_agree_percent]
ax.tick_params(axis="x", labelsize=12)
ax.tick_params(axis="y", labelsize=14)
csfont = {'fontname':'Comic Sans MS'}
plt.title("I am clear on the University of Calgary's key message", **csfont)
ax.bar(opinion,key_message_prcnt,color = colors )
plt.tight_layout()
plt.legend()
plt.show()

#PLOTTING THE 'KEY MESSAGE' & 'MISSION'
a_mission = df["I am clear on the mission and objectives of the Advancement Communications team"].value_counts()
a_mission
#calculating the frequency number of each response
mission_Agree = a_mission.loc['Agree']
mission_Neutral = a_mission.loc['Neither agree nor disagree']
mission_Disagree =a_mission.loc['Disagree']
mission_Strongly_agree= a_mission.loc['Strongly agree']
mission_Strongly_disagree = a_mission.loc['Strongly disagree']
mission_Strongly_disagree = 0
#calculating the percentages for each response
mission_Agree_percent = (mission_Agree/(mission_Agree+mission_Neutral+mission_Disagree+mission_Strongly_agree+mission_Strongly_disagree))*100
mission_Disagree_percent = (mission_Disagree/(mission_Agree+mission_Neutral+mission_Disagree+mission_Strongly_agree+mission_Strongly_disagree))*100
mission_Neutral_percent = (mission_Neutral/(mission_Agree+mission_Neutral+mission_Disagree+mission_Strongly_agree+mission_Strongly_disagree))*100
mission_Strongly_agree_percent = (mission_Strongly_agree/(mission_Agree+mission_Neutral+mission_Disagree+mission_Strongly_agree+mission_Strongly_disagree))*100
mission_Strongly_disagree_percent = (mission_Strongly_disagree/(mission_Agree+mission_Neutral+mission_Disagree+mission_Strongly_agree+mission_Strongly_disagree))*100

mission_prcnt = [mission_Strongly_disagree_percent,mission_Disagree_percent,mission_Neutral_percent,mission_Agree_percent , mission_Strongly_agree_percent ] 

#plot "key message" and "mission" next to each other:

x_indexes = np.arange(len(opinion)) #create a var (x_indexes) that is an array of values, which
#are a number version of x values. x_indexes is used instead of ages_x to create bar charts next to each other.
width=0.25 #defining the value that is going to be used as width of bars

plt.figure(figsize=(20,10))
plt.bar(x_indexes - width,key_message_prcnt , width = width, color='#d6001c', label="Clear on U of C's key message")
plt.bar(x_indexes,mission_prcnt, width = width, color='#ffcd00',label ='Clear on Mission and objectives of the Adv Comm team')  
ax.tick_params(axis="x", labelsize=8)
ax.tick_params(axis="y", labelsize=14)
plt.xticks(ticks=x_indexes, labels=opinion, fontsize = 20) #replaces the indexes with the ages on X axis.
plt.yticks(fontsize = 25)

plt.ylabel('Percentage', fontsize=40)
plt.tight_layout()
plt.legend(fontsize = 30)
plt.show() 

#PLOTTING CLEARANCE ON PERFORMANCE IN DIFFERENT AREAS (UNI, ADV, ADV COMM, DIV, ROLE)

##performance university

a_perf_uni = df["I am clear on how performance will be measured... at the university"].value_counts()
a_perf_uni
#calculating the frequency number of each response
perf_uni_Agree = a_perf_uni.loc['Agree']
perf_uni_Neutral = a_perf_uni.loc['Neither agree nor disagree']
perf_uni_Disagree =a_perf_uni.loc['Disagree']
perf_uni_Strongly_agree= a_perf_uni.loc['Strongly agree']
perf_uni_Strongly_disagree = a_perf_uni.loc['Strongly disagree']
perf_uni_PNS = a_perf_uni.loc['Prefer not to say']
perf_uni_PNS = 0
#calculating the percentages for each response
perf_uni_Agree_percent = (perf_uni_Agree/(perf_uni_Agree+perf_uni_Neutral+perf_uni_Disagree+perf_uni_Strongly_agree+perf_uni_Strongly_disagree+perf_uni_PNS))*100
perf_uni_Disagree_percent = (perf_uni_Disagree/(perf_uni_Agree+perf_uni_Neutral+perf_uni_Disagree+perf_uni_Strongly_agree+perf_uni_Strongly_disagree+perf_uni_PNS))*100
perf_uni_Neutral_percent = (perf_uni_Neutral/(perf_uni_Agree+perf_uni_Neutral+perf_uni_Disagree+perf_uni_Strongly_agree+perf_uni_Strongly_disagree+perf_uni_PNS))*100
perf_uni_Strongly_agree_percent = (perf_uni_Strongly_agree/(perf_uni_Agree+perf_uni_Neutral+perf_uni_Disagree+perf_uni_Strongly_agree+perf_uni_Strongly_disagree+perf_uni_PNS))*100
perf_uni_Strongly_disagree_percent = (perf_uni_Strongly_disagree/(perf_uni_Agree+perf_uni_Neutral+perf_uni_Disagree+perf_uni_Strongly_agree+perf_uni_Strongly_disagree+perf_uni_PNS))*100
perf_uni_PNS_percent = (perf_uni_PNS/(perf_uni_Agree+perf_uni_Neutral+perf_uni_Disagree+perf_uni_Strongly_agree+perf_uni_Strongly_disagree+perf_uni_PNS))*100

perf_uni_prcnt = [perf_uni_Strongly_disagree_percent,perf_uni_Disagree_percent,perf_uni_Neutral_percent,perf_uni_Agree_percent , perf_uni_Strongly_agree_percent, perf_uni_PNS_percent ] 

##performance advancement
a_perf_adv = df['I am clear on how performance will be measured... in Advancement'].value_counts()
a_perf_adv
#calculating the frequency number of each response
perf_adv_Agree = a_perf_adv.loc['Agree']
perf_adv_Neutral = a_perf_adv.loc['Neither agree nor disagree']
perf_adv_Disagree =a_perf_adv.loc['Disagree']
perf_adv_Strongly_agree= a_perf_adv.loc['Strongly agree']
perf_adv_Strongly_disagree = a_perf_adv.loc['Strongly disagree']
perf_adv_PNS = a_perf_adv.loc['Prefer not to say']
perf_adv_PNS = 0
#calculating the percentages for each response
perf_adv_Agree_percent = (perf_adv_Agree/(perf_adv_Agree+perf_adv_Neutral+perf_adv_Disagree+perf_adv_Strongly_agree+perf_adv_Strongly_disagree+perf_adv_PNS))*100
perf_adv_Disagree_percent = (perf_adv_Disagree/(perf_adv_Agree+perf_adv_Neutral+perf_adv_Disagree+perf_adv_Strongly_agree+perf_adv_Strongly_disagree+perf_adv_PNS))*100
perf_adv_Neutral_percent = (perf_adv_Neutral/(perf_adv_Agree+perf_adv_Neutral+perf_adv_Disagree+perf_adv_Strongly_agree+perf_adv_Strongly_disagree+perf_adv_PNS))*100
perf_adv_Strongly_agree_percent = (perf_adv_Strongly_agree/(perf_adv_Agree+perf_adv_Neutral+perf_adv_Disagree+perf_adv_Strongly_agree+perf_adv_Strongly_disagree+perf_adv_PNS))*100
perf_adv_Strongly_disagree_percent = (perf_adv_Strongly_disagree/(perf_adv_Agree+perf_adv_Neutral+perf_adv_Disagree+perf_adv_Strongly_agree+perf_adv_Strongly_disagree+perf_adv_PNS))*100
perf_adv_PNS_percent = (perf_adv_PNS/(perf_adv_Agree+perf_adv_Neutral+perf_adv_Disagree+perf_adv_Strongly_agree+perf_adv_Strongly_disagree+perf_adv_PNS))*100


perf_adv_prcnt = [perf_adv_Strongly_disagree_percent,perf_adv_Disagree_percent,perf_adv_Neutral_percent,perf_adv_Agree_percent , perf_adv_Strongly_agree_percent, perf_adv_PNS_percent ] 


##performance advancement communications
a_perf_adv_comm = df['I am clear on how performance will be measured... in Advancement Communications'].value_counts()
a_perf_adv_comm
perf_adv_comm_PNS = 0
#a_perf_adv_comm['Strongly disagree'] = 0
#calculating the frequency number of each response
perf_adv_comm_Agree = a_perf_adv_comm.loc['Agree']
perf_adv_comm_Neutral = a_perf_adv_comm.loc['Neither agree nor disagree']
perf_adv_comm_Disagree =a_perf_adv_comm.loc['Disagree']
perf_adv_comm_Strongly_agree= a_perf_adv_comm.loc['Strongly agree']
perf_adv_comm_Strongly_disagree = a_perf_adv_comm.loc['Strongly disagree']
perf_adv_comm_PNS = a_perf_adv_comm.loc['Prefer not to say']

#calculating the percentages for each response
perf_adv_comm_Agree_percent = (perf_adv_comm_Agree/(perf_adv_comm_Agree+perf_adv_comm_Neutral+perf_adv_comm_Disagree+perf_adv_comm_Strongly_agree+perf_adv_comm_Strongly_disagree+perf_adv_comm_PNS))*100
perf_adv_comm_Disagree_percent = (perf_adv_comm_Disagree/(perf_adv_comm_Agree+perf_adv_comm_Neutral+perf_adv_comm_Disagree+perf_adv_comm_Strongly_agree+perf_adv_comm_Strongly_disagree+perf_adv_comm_PNS))*100
perf_adv_comm_Neutral_percent = (perf_adv_comm_Neutral/(perf_adv_comm_Agree+perf_adv_comm_Neutral+perf_adv_comm_Disagree+perf_adv_comm_Strongly_agree+perf_adv_comm_Strongly_disagree+perf_adv_comm_PNS))*100
perf_adv_comm_Strongly_agree_percent = (perf_adv_comm_Strongly_agree/(perf_adv_comm_Agree+perf_adv_comm_Neutral+perf_adv_comm_Disagree+perf_adv_comm_Strongly_agree+perf_adv_comm_Strongly_disagree+perf_adv_comm_PNS))*100
perf_adv_comm_Strongly_disagree_percent = (perf_adv_comm_Strongly_disagree/(perf_adv_comm_Agree+perf_adv_comm_Neutral+perf_adv_comm_Disagree+perf_adv_comm_Strongly_agree+perf_adv_comm_Strongly_disagree+perf_adv_comm_PNS))*100
perf_adv_comm_PNS_percent = (perf_adv_comm_PNS/(perf_adv_comm_Agree+perf_adv_comm_Neutral+perf_adv_comm_Disagree+perf_adv_comm_Strongly_agree+perf_adv_comm_Strongly_disagree+perf_adv_comm_PNS))*100


perf_adv_comm_prcnt = [perf_adv_comm_Strongly_disagree_percent,perf_adv_comm_Disagree_percent,perf_adv_comm_Neutral_percent,perf_adv_comm_Agree_percent , perf_adv_comm_Strongly_agree_percent, perf_adv_comm_PNS_percent ] 


##performance division
a_perf_div = df['I am clear on how performance will be measured... in my division'].value_counts()
a_perf_div
a_perf_div['Strongly disagree'] = 0
#calculating the frequency number of each response
perf_div_Agree = a_perf_div.loc['Agree']
perf_div_Neutral = a_perf_div.loc['Neither agree nor disagree']
perf_div_Disagree =a_perf_div.loc['Disagree']
perf_div_Strongly_agree= a_perf_div.loc['Strongly agree']
perf_div_Strongly_disagree = a_perf_div.loc['Strongly disagree']
perf_div_PNS = a_perf_div.loc['Prefer not to say']
perf_div_PNS = 0
#calculating the percentages for each response
perf_div_Agree_percent = (perf_div_Agree/(perf_div_Agree+perf_div_Neutral+perf_div_Disagree+perf_div_Strongly_agree+perf_div_Strongly_disagree+perf_div_PNS))*100
perf_div_Disagree_percent = (perf_div_Disagree/(perf_div_Agree+perf_div_Neutral+perf_div_Disagree+perf_div_Strongly_agree+perf_div_Strongly_disagree+perf_div_PNS))*100
perf_div_Neutral_percent = (perf_div_Neutral/(perf_div_Agree+perf_div_Neutral+perf_div_Disagree+perf_div_Strongly_agree+perf_div_Strongly_disagree+perf_div_PNS))*100
perf_div_Strongly_agree_percent = (perf_div_Strongly_agree/(perf_div_Agree+perf_div_Neutral+perf_div_Disagree+perf_div_Strongly_agree+perf_div_Strongly_disagree+perf_div_PNS))*100
perf_div_Strongly_disagree_percent = (perf_div_Strongly_disagree/(perf_div_Agree+perf_div_Neutral+perf_div_Disagree+perf_div_Strongly_agree+perf_div_Strongly_disagree+perf_div_PNS))*100
perf_div_PNS_percent = (perf_div_PNS/(perf_div_Agree+perf_div_Neutral+perf_div_Disagree+perf_div_Strongly_agree+perf_div_Strongly_disagree+perf_div_PNS))*100


perf_div_prcnt = [perf_div_Strongly_disagree_percent,perf_div_Disagree_percent,perf_div_Neutral_percent,perf_div_Agree_percent , perf_div_Strongly_agree_percent, perf_div_PNS_percent ] 



##performance role
a_perf_role = df['I am clear on how performance will be measured... in my role'].value_counts()
a_perf_role
#a_perf_role__ = ((df['I am clear on how performance will be measured... in my role'].value_counts(normalize=True).round(3))*100).round(1)
#a_perf_role__
#calculating the frequency number of each response
perf_role_Agree = a_perf_role.loc['Agree']
perf_role_Neutral = a_perf_role.loc['Neither agree nor disagree']
perf_role_Disagree =a_perf_role.loc['Disagree']
perf_role_Strongly_agree= a_perf_role.loc['Strongly agree']
perf_role_Strongly_disagree = a_perf_role.loc['Strongly disagree']
perf_role_PNS = a_perf_role.loc['Prefer not to say']
perf_role_PNS = 0
#calculating the percentages for each response
perf_role_Agree_percent = (perf_role_Agree/(perf_role_Agree+perf_role_Neutral+perf_role_Disagree+perf_role_Strongly_agree+perf_role_Strongly_disagree+perf_role_PNS))*100
perf_role_Disagree_percent = (perf_role_Disagree/(perf_role_Agree+perf_role_Neutral+perf_role_Disagree+perf_role_Strongly_agree+perf_role_Strongly_disagree+perf_role_PNS))*100
perf_role_Neutral_percent = (perf_role_Neutral/(perf_role_Agree+perf_role_Neutral+perf_role_Disagree+perf_role_Strongly_agree+perf_role_Strongly_disagree+perf_role_PNS))*100
perf_role_Strongly_agree_percent = (perf_role_Strongly_agree/(perf_role_Agree+perf_role_Neutral+perf_role_Disagree+perf_role_Strongly_agree+perf_role_Strongly_disagree+perf_role_PNS))*100
perf_role_Strongly_disagree_percent = (perf_role_Strongly_disagree/(perf_role_Agree+perf_role_Neutral+perf_role_Disagree+perf_role_Strongly_agree+perf_role_Strongly_disagree+perf_role_PNS))*100
perf_role_PNS_percent = (perf_role_PNS/(perf_role_Agree+perf_role_Neutral+perf_role_Disagree+perf_role_Strongly_agree+perf_role_Strongly_disagree+perf_role_PNS))*100


perf_role_prcnt = [perf_role_Strongly_disagree_percent,perf_role_Disagree_percent,perf_role_Neutral_percent,perf_role_Agree_percent , perf_role_Strongly_agree_percent, perf_role_PNS_percent ] 
perf_role_prcnt

##PLOT PERFORMANCE FOR ALL 5 NEXT TO EACH OTHER


opinion_b = ['Strongly disagree','Disagree','Neutral','Agree','Strongly agree', 'PNS']

x_indexes = np.arange(len(opinion_b)) #create a var (x_indexes) that is an array of values, which
#are a number version of x values. x_indexes is used instead of ages_x to create bar charts next to each other.
width=0.15 #defining the value that is going to be used as width of bars

plt.figure(figsize=(35,17))
plt.bar(x_indexes - width*2,perf_uni_prcnt , width = width, color='#d6001c', label="Clear on performance at University")
plt.bar(x_indexes - width,perf_adv_prcnt , width = width, color='#ffcd00', label="Clear on performance in Adv.")
plt.bar(x_indexes,perf_adv_comm_prcnt, width = width, color='#ff671f',label ='Clear on performance in Adv Comm')  
plt.bar(x_indexes + width,perf_div_prcnt , width = width, color='#ed0a72', label="Clear on performance in division")
plt.bar(x_indexes + width*2,perf_role_prcnt , width = width, color='#47a67c', label="Clear on performance in role")


ax.tick_params(axis="x", labelsize=8)
ax.tick_params(axis="y", labelsize=14)
plt.xticks(ticks=x_indexes, labels=opinion_b) #replaces the indexes with the ages on X axis.


plt.ylabel('Percentage', fontsize=60)
plt.tight_layout()
plt.legend(loc = 'upper right',fontsize = 40)
plt.show() 


#ROLE EXPECTATIONS AND POLICIES & PROCESSES in 1 PLOT
expected_my_role_percent = ((df['I understand what is expected of me in my role'].value_counts(normalize=True).round(3))*100).round(1)
#expected_my_role_percent['PNS'] = 0
expected_my_role_percent
expected_my_role_percent_array = [expected_my_role_percent['Strongly disagree'],expected_my_role_percent['Disagree'] ,expected_my_role_percent['Neither agree nor disagree'],expected_my_role_percent['Agree'], expected_my_role_percent['Strongly agree']]
expected_my_role_percent_array

expected_other_role_percent = ((df['I understand what is expected of other people in other communications roles'].value_counts(normalize=True).round(3))*100).round(1)
expected_other_role_percent
#expected_other_role_percent['PNS'] = 0
expected_other_role_percent['Agree']
expected_other_role_percent_array = [expected_other_role_percent['Strongly disagree'],expected_other_role_percent['Disagree'] ,expected_other_role_percent['Neither agree nor disagree'],expected_other_role_percent['Agree'], expected_other_role_percent['Strongly agree']]
expected_other_role_percent_array


policies_processes_percent = ((df['I feel I have the policies and processes needed to do my job'].value_counts(normalize=True).round(3))*100).round(1)
#policies_processes_percent['PNS'] = 0
policies_processes_percent
policies_processes_percent_array = [ policies_processes_percent['Strongly disagree'],policies_processes_percent['Disagree'] ,policies_processes_percent['Neither agree nor disagree'],policies_processes_percent['Agree'], policies_processes_percent['Strongly agree']]
policies_processes_percent_array

#COMBINED PLOT

x_indexes = np.arange(len(opinion)) #create a var (x_indexes) that is an array of values, which
#are a number version of x values. x_indexes is used instead of ages_x to create bar charts next to each other.
width=0.20 #defining the value that is going to be used as width of bars

plt.figure(figsize=(35,17))
plt.bar(x_indexes - width, expected_my_role_percent_array , width = width, color='#d6001c', label="I understand what is expected of me in my role")
plt.bar(x_indexes,expected_other_role_percent_array, width = width, color='#ffcd00',label ='I understand what is expected of other people in other communications roles')  
plt.bar(x_indexes + width,policies_processes_percent_array , width = width, color='#ff671f', label="I have the policies and processes needed to do my job")

#ax.tick_params(axis="x", labelsize=24)
#ax.tick_params(axis="y", labelsize=14)
plt.xticks(ticks=x_indexes, labels=opinion, fontsize = 40) #replaces the indexes with the ages on X axis.
plt.ylabel('Percentage', fontsize = 40)
#plt.tight_layout()
plt.legend(fontsize = 35)
plt.show() 

##WORK ENVIRONMENT
#RESPECTFUL WORKPLACE

##respectful university               
respectful_uni_percent = ((df['I believe we have a respectful workplace... at the university'].value_counts(normalize=True).round(3))*100).round(1)
#respectful_uni_percent['PNS'] = 0
respectful_uni_percent
respectful_uni_percent_array = [respectful_uni_percent['Strongly disagree'],respectful_uni_percent['Disagree'] ,respectful_uni_percent['Neither agree nor disagree'],respectful_uni_percent['Agree'], respectful_uni_percent['Strongly agree']]
respectful_uni_percent_array

##respectful advancement
respectful_adv_percent = ((df['I believe we have a respectful workplace... in Advancement'].value_counts(normalize=True).round(3))*100).round(1)
#respectful_adv_percent['PNS'] = 0
respectful_adv_percent
respectful_adv_percent_array = [respectful_adv_percent['Strongly disagree'],respectful_adv_percent['Disagree'] ,respectful_adv_percent['Neither agree nor disagree'],respectful_adv_percent['Agree'], respectful_adv_percent['Strongly agree']]
respectful_adv_percent_array


##respectful advancement communications
respectful_adv_comm_percent = ((df['I believe we have a respectful workplace... in Advancement Communications'].value_counts(normalize=True).round(3))*100).round(1)
#respectful_adv_comm_percent['PNS'] = 0
respectful_adv_comm_percent
respectful_adv_comm_percent_array = [respectful_adv_comm_percent['Strongly disagree'],respectful_adv_comm_percent['Disagree'] ,respectful_adv_comm_percent['Neither agree nor disagree'],respectful_adv_comm_percent['Agree'], respectful_adv_comm_percent['Strongly agree']]
respectful_adv_comm_percent_array


##respectful division
respectful_div_percent = ((df['I believe we have a respectful workplace... in my division'].value_counts(normalize=True).round(3))*100).round(1)
respectful_div_percent['Disagree'] = 0
respectful_div_percent
respectful_div_percent_array = [respectful_div_percent['Strongly disagree'],respectful_div_percent['Disagree'] ,respectful_div_percent['Neither agree nor disagree'],respectful_div_percent['Agree'], respectful_div_percent['Strongly agree']]
respectful_div_percent_array


##COMBINED PLOT

x_indexes = np.arange(len(opinion)) #create a var (x_indexes) that is an array of values, which
#are a number version of x values. x_indexes is used instead of ages_x to create bar charts next to each other.
width=0.20 #defining the value that is going to be used as width of bars

plt.figure(figsize=(35,17))
plt.bar(x_indexes - width*2, respectful_uni_percent_array , width = width, color='#d6001c', label="We have a respectful workplace at the university")
plt.bar(x_indexes - width, respectful_adv_percent_array , width = width, color='#ffcd00', label="We have a respectful workplace in Advancement")
plt.bar(x_indexes,respectful_adv_comm_percent_array, width = width, color='#ff671f',label ='We have a respectful workplace in Advancement Communications')  
plt.bar(x_indexes + width,respectful_div_percent_array , width = width, color='#ed0a72', label="We have a respectful workplace in my division")

ax.tick_params(axis="x", labelsize=14)
ax.tick_params(axis="y", labelsize=24)
plt.xticks(ticks=x_indexes, labels=opinion, fontsize = 40) #replaces the indexes with the ages on X axis.

plt.ylabel('Percentage', fontsize = 40)
#plt.tight_layout()
plt.legend(fontsize = 37)
plt.show() 

##WE WORK AS A TEAM

teamwork_uni_percent = ((df['I believe we work as a team... at the university'].value_counts(normalize=True).round(3))*100).round(1)
teamwork_uni_percent
teamwork_uni_percent_array = [teamwork_uni_percent['Strongly disagree'],teamwork_uni_percent['Disagree'] ,teamwork_uni_percent['Neither agree nor disagree'],teamwork_uni_percent['Agree'], teamwork_uni_percent['Strongly agree']]
teamwork_uni_percent_array

##TEAMWORK advancement
teamwork_adv_percent = ((df['I believe we work as a team... in Advancement'].value_counts(normalize=True).round(3))*100).round(1)
teamwork_adv_percent
teamwork_adv_percent_array = [teamwork_adv_percent['Strongly disagree'],teamwork_adv_percent['Disagree'] ,teamwork_adv_percent['Neither agree nor disagree'],teamwork_adv_percent['Agree'], teamwork_adv_percent['Strongly agree']]
teamwork_adv_percent_array


##teamwork advancement communications
teamwork_adv_comm_percent = ((df['I believe we work as a team... in Advancement Communications'].value_counts(normalize=True).round(3))*100).round(1)
teamwork_adv_comm_percent
teamwork_adv_comm_percent_array = [teamwork_adv_comm_percent['Strongly disagree'],teamwork_adv_comm_percent['Disagree'] ,teamwork_adv_comm_percent['Neither agree nor disagree'],teamwork_adv_comm_percent['Agree'], teamwork_adv_comm_percent['Strongly agree']]
teamwork_adv_comm_percent_array


##teamwork division
teamwork_div_percent = ((df['I believe we work as a team... in my division'].value_counts(normalize=True).round(3))*100).round(1)
teamwork_div_percent
teamwork_div_percent_array = [teamwork_div_percent['Strongly disagree'],teamwork_div_percent['Disagree'] ,teamwork_div_percent['Neither agree nor disagree'],teamwork_div_percent['Agree'], teamwork_div_percent['Strongly agree']]
teamwork_div_percent_array


##COMBINED PLOT

x_indexes = np.arange(len(opinion)) #create a var (x_indexes) that is an array of values, which
#are a number version of x values. x_indexes is used instead of ages_x to create bar charts next to each other.
width=0.20 #defining the value that is going to be used as width of bars

plt.figure(figsize=(35,17))
plt.bar(x_indexes - width*2, teamwork_uni_percent_array , width = width, color='#d6001c', label="We work as a team at the university")
plt.bar(x_indexes - width, teamwork_adv_percent_array , width = width, color='#ffcd00', label="We work as a team in Advancement")
plt.bar(x_indexes,teamwork_adv_comm_percent_array, width = width, color='#ff671f',label ='We work as a team in Adv. Comm.')  
plt.bar(x_indexes + width,teamwork_div_percent_array , width = width, color='#ed0a72', label="We work as a team in my division")

ax.tick_params(axis="x", labelsize=14)
ax.tick_params(axis="y", labelsize=24)
plt.xticks(ticks=x_indexes, labels=opinion, fontsize = 40) #replaces the indexes with the ages on X axis.

plt.ylabel('Percentage', fontsize = 40)
#plt.tight_layout()
plt.legend(loc= 'upper left', fontsize = 40)
plt.show() 

##WORKPLACE THAT VALUES PERFORMANCE
#UNIVERSITY               
value_performance_uni_percent = ((df['I believe we have a workplace that values performance... at the university'].value_counts(normalize=True).round(3))*100).round(1)
value_performance_uni_percent
value_performance_uni_percent_array = [value_performance_uni_percent['Strongly disagree'],value_performance_uni_percent['Disagree'] ,value_performance_uni_percent['Neither agree nor disagree'],value_performance_uni_percent['Agree'], value_performance_uni_percent['Strongly agree']]
value_performance_uni_percent_array

##ADVANCEMENT
value_performance_adv_percent = ((df['I believe we have a workplace that values performance... in Advancement'].value_counts(normalize=True).round(3))*100).round(1)
value_performance_adv_percent
value_performance_adv_percent_array = [value_performance_adv_percent['Strongly disagree'],value_performance_adv_percent['Disagree'] ,value_performance_adv_percent['Neither agree nor disagree'],value_performance_adv_percent['Agree'], value_performance_adv_percent['Strongly agree']]
value_performance_adv_percent_array


##ADVANCEMENT COMMUNICATIONS
value_performance_adv_comm_percent = ((df['I believe we have a workplace that values performance... in Advancement Communications'].value_counts(normalize=True).round(3))*100).round(1)
value_performance_adv_comm_percent
value_performance_adv_comm_percent_array = [value_performance_adv_comm_percent['Strongly disagree'],value_performance_adv_comm_percent['Disagree'] ,value_performance_adv_comm_percent['Neither agree nor disagree'],value_performance_adv_comm_percent['Agree'], value_performance_adv_comm_percent['Strongly agree']]
value_performance_adv_comm_percent_array


##DIVISION
value_performance_div_percent = ((df['I believe we have a workplace that values performance... in my division'].value_counts(normalize=True).round(3))*100).round(1)
value_performance_div_percent
value_performance_div_percent_array = [value_performance_div_percent['Strongly disagree'],value_performance_div_percent['Disagree'] ,value_performance_div_percent['Neither agree nor disagree'],value_performance_div_percent['Agree'], value_performance_div_percent['Strongly agree']]
value_performance_div_percent_array


##COMBINED PLOT

x_indexes = np.arange(len(opinion)) #create a var (x_indexes) that is an array of values, which
#are a number version of x values. x_indexes is used instead of ages_x to create bar charts next to each other.
width=0.20 #defining the value that is going to be used as width of bars

plt.figure(figsize=(35,17))
plt.bar(x_indexes - width*2, value_performance_uni_percent_array , width = width, color='#d6001c', label="I believe performance is valued at the university")
plt.bar(x_indexes - width, value_performance_adv_percent_array , width = width, color='#ffcd00', label="I believe performance is valued in Advancement")
plt.bar(x_indexes,value_performance_adv_comm_percent_array, width = width, color='#ff671f',label ='I believe performance is valued in Advancement Comm.')  
plt.bar(x_indexes + width,value_performance_div_percent_array , width = width, color='#ed0a72', label="I believe performance is valued in my division")


ax.tick_params(axis="x", labelsize=14)
ax.tick_params(axis="y")
plt.xticks(ticks=x_indexes, labels=opinion, fontsize = 40, **csfont) #replaces the indexes with the ages on X axis.
plt.ylabel('Percentage', fontsize = 40)
#plt.tight_layout()
plt.legend(fontsize = 40)
plt.show()            
                

##PERFORMANCE FEEDBACK
 
##CLEAR PERFORMANCE FEEDBACK            
clear_perf_fdbck_percent = ((df['Performance feedback from my manager is... clear'].value_counts(normalize=True).round(3))*100).round(1)
clear_perf_fdbck_percent
clear_perf_fdbck_percent_array = [clear_perf_fdbck_percent['Strongly disagree'],clear_perf_fdbck_percent['Disagree'] ,clear_perf_fdbck_percent['Neither agree nor disagree'],clear_perf_fdbck_percent['Agree'], clear_perf_fdbck_percent['Strongly agree']]
clear_perf_fdbck_percent_array

##CONSISTENT PERFORMANCE FEEDBACK
consistent_perf_fdbck_percent = ((df['Performance feedback from my manager is... consistent'].value_counts(normalize=True).round(3))*100).round(1)
consistent_perf_fdbck_percent
consistent_perf_fdbck_percent_array = [consistent_perf_fdbck_percent['Strongly disagree'],consistent_perf_fdbck_percent['Disagree'] ,consistent_perf_fdbck_percent['Neither agree nor disagree'],consistent_perf_fdbck_percent['Agree'], consistent_perf_fdbck_percent['Strongly agree']]
consistent_perf_fdbck_percent_array


##REGULAR PERFORMANCE FEEDBACK
regular_perf_fdbck_percent = ((df['Performance feedback from my manager is... regular'].value_counts(normalize=True).round(3))*100).round(1)
regular_perf_fdbck_percent
regular_perf_fdbck_percent_array = [regular_perf_fdbck_percent['Strongly disagree'],regular_perf_fdbck_percent['Disagree'] ,regular_perf_fdbck_percent['Neither agree nor disagree'],regular_perf_fdbck_percent['Agree'], regular_perf_fdbck_percent['Strongly agree']]
regular_perf_fdbck_percent_array


##COMBINED PLOT

x_indexes = np.arange(len(opinion)) #create a var (x_indexes) that is an array of values, which
#are a number version of x values. x_indexes is used instead of ages_x to create bar charts next to each other.
width=0.20 #defining the value that is going to be used as width of bars

plt.figure(figsize=(35,17))
plt.bar(x_indexes - width, clear_perf_fdbck_percent_array , width = width, color='#d6001c', label="Performance feedback from my manager is clear")
plt.bar(x_indexes,consistent_perf_fdbck_percent_array, width = width, color='#ffcd00',label ='Performance feedback from my manager is consistent')  
plt.bar(x_indexes + width,regular_perf_fdbck_percent_array , width = width, color='#ff671f', label="Performance feedback from my manager is regular")

#ax.set_yticklabels(y_ticks, rotation=0, fontsize=20)
#plt.rc('ytick',labelsize=20)
#plt.rc('xtick', labelsize=20)
ax.tick_params(axis="x", labelsize=20)
ax.tick_params(axis="y")

plt.xticks(ticks=x_indexes, labels=opinion, fontsize = 40, **csfont) #replaces the indexes with the ages on X axis.
plt.ylabel('Percentage', fontsize = 40)
#plt.tight_layout()
plt.legend(fontsize = 40)
plt.show()            
            

##WORK LOAD
workload_range = ['Too heavy', 'Heavy', 'Moderate', 'Light', 'Too light','Hard to tell', 'PNS']
workload_percent = ((df["The volume of work I'm asked to perform is..."].value_counts(normalize=True).round(3))*100).round(1)
for word in workload_range:
    if word not in workload_percent.index:
        workload_percent[word] = 0
workload_percent
workload_percent_array = [workload_percent['Too heavy'],workload_percent['Heavy'],workload_percent['Moderate'] ,workload_percent['Light'], workload_percent['Too light'],workload_percent['Hard to tell'], workload_percent['Prefer not to say']]
workload_percent_array
#PLOT WORKLOAD
x_indexes = np.arange(len(workload_range)) #create a var (x_indexes) that is an array of values, which
#are a number version of x values. x_indexes is used instead of ages_x to create bar charts next to each other.
width=0.35 #defining the value that is going to be used as width of bars

plt.figure(figsize=(25,10))
plt.bar(x_indexes,workload_percent_array, width = width, color='#d6001c',label ="The volume of work I'm asked to perform is:")  

#ax.set_yticklabels(y_ticks, rotation=0, fontsize=20)
#plt.rc('ytick',labelsize=20)
#plt.rc('xtick', labelsize=20)
ax.tick_params(axis="x", labelsize=20)
ax.tick_params(axis="y")

plt.xticks(ticks=x_indexes, labels=workload_range, fontsize = 25) #replaces the indexes with the ages on X axis.
plt.ylabel('Percentage', fontsize = 30)
#plt.tight_layout()
plt.legend(fontsize = 35)
plt.show()            
            
##PROFESSIONAL DEVELOPMENT

#FORMAL DEVELOPMENT OPPORTUNITIES
formal_dev_percent = ((df['I am provided formal development opportunities like access to courses and seminars'].value_counts(normalize=True).round(3))*100).round(1)

for word in response:
    if word not in formal_dev_percent.index:
        formal_dev_percent[word] = 0

formal_dev_percent

formal_dev_percent_array = [formal_dev_percent['Strongly disagree'],formal_dev_percent['Disagree'] ,formal_dev_percent['Neither agree nor disagree'],formal_dev_percent['Agree'], formal_dev_percent['Strongly Agree']]
formal_dev_percent_array


#INFORMAL DEVELOPMENT OPPORTUNITIES
informal_dev_percent = ((df['I am provided informal development opportunities like coaching, stretch assignments or acting roles'].value_counts(normalize=True).round(3))*100).round(1)
informal_dev_percent.index

response = ['Strongly disagree','Disagree','Neither agree nor disagree','Agree','Strongly Agree']
for word in response:
    if word not in informal_dev_percent.index:
        informal_dev_percent[word] = 0
        
informal_dev_percent

informal_dev_percent_array = [informal_dev_percent['Strongly disagree'],informal_dev_percent['Disagree'] ,informal_dev_percent['Neither agree nor disagree'],informal_dev_percent['Agree'], informal_dev_percent['Strongly Agree']]
informal_dev_percent_array

##COMBINED PLOT

x_indexes = np.arange(len(opinion)) #create a var (x_indexes) that is an array of values, which
#are a number version of x values. x_indexes is used instead of ages_x to create bar charts next to each other.
width=0.25 #defining the value that is going to be used as width of bars

plt.figure(figsize=(35,17))
plt.bar(x_indexes - width, formal_dev_percent_array , width = width, color='#d6001c', label="I am provided formal development opportunities like access to courses and seminars")
plt.bar(x_indexes,informal_dev_percent_array, width = width, color='#ffcd00',label ='I am provided informal development opportunities like coaching, stretch assignments or acting roles')  

#ax.set_yticklabels(y_ticks, rotation=0, fontsize=20)
#plt.rc('ytick',labelsize=20)
#plt.rc('xtick', labelsize=20)
ax.tick_params(axis="x", labelsize=20)
ax.tick_params(axis="y")

plt.xticks(ticks=x_indexes, labels=opinion, fontsize = 40) #replaces the indexes with the ages on X axis.
plt.ylabel('Percentage', fontsize = 40)
#plt.tight_layout()
plt.legend(loc = 'upper left', fontsize = 35)
plt.show()     


## CAREER PATH
opinion_c = ['Strongly disagree','Disagree','Neutral','Agree','Strongly agree', "Don't know"]
career_path_percent = ((df['I have a good understanding of what my career path and/or career opportunities could be at the University of Calgary'].value_counts(normalize=True).round(3))*100).round(1)

response = ['Strongly disagree','Disagree','Neither agree nor disagree','Agree','Strongly agree']
for word in response:
    if word not in career_path_percent.index:
        career_path_percent[word] = 0

career_path_percent


career_path_percent_array = [career_path_percent['Strongly disagree'],career_path_percent['Disagree'] ,career_path_percent['Neither agree nor disagree'],career_path_percent['Agree'], career_path_percent['Strongly Agree'], career_path_percent["Don't know"]]
career_path_percent_array

##ADVANCE CAREER
career_advance_percent = ((df["I am able to advance my career at the University of Calgary"].value_counts(normalize=True).round(3))*100).round(1)

response = ['Strongly disagree','Disagree','Neither agree nor disagree','Agree','Strongly agree']
for word in response:
    if word not in career_advance_percent.index:
        career_advance_percent[word] = 0

career_advance_percent


career_advance_percent_array = [career_advance_percent['Strongly disagree'],career_advance_percent['Disagree'] ,career_advance_percent['Neither agree nor disagree'],career_advance_percent['Agree'], career_advance_percent['Strongly Agree'], career_advance_percent["Don't know"]]
career_advance_percent_array

##COMBINED PLOT

x_indexes = np.arange(len(opinion_c)) #create a var (x_indexes) that is an array of values, which
#are a number version of x values. x_indexes is used instead of ages_x to create bar charts next to each other.
width=0.25 #defining the value that is going to be used as width of bars

plt.figure(figsize=(35,17))
plt.bar(x_indexes - width, career_path_percent_array , width = width, color='#d6001c', label="Good understanding of what my career path could be at UCalgary")
plt.bar(x_indexes,career_advance_percent_array, width = width, color='#ffcd00',label ='Able to advance my career at UCalgary')  

ax.tick_params(axis="x", labelsize=20)
ax.tick_params(axis="y")

plt.xticks(ticks=x_indexes, labels=opinion_c, fontsize = 40) #replaces the indexes with the ages on X axis.
plt.ylabel('Percentage', fontsize = 40)
#plt.tight_layout()
plt.legend(fontsize = 35)
plt.show()     


##BOTTOM LINE
              
#uni work matters               
work_matters_percent = ((df['The work we do here at the University of Calgary matters'].value_counts(normalize=True).round(3))*100).round(1)

for word in response:
    if word not in work_matters_percent.index:
        work_matters_percent[word] = 0

work_matters_percent

work_matters_percent_array = [work_matters_percent['Strongly disagree'],work_matters_percent['Disagree'] ,work_matters_percent['Neither agree nor disagree'],work_matters_percent['Agree'], work_matters_percent['Strongly agree']]
work_matters_percent_array
                
#comm work matters
work_comm_matters_percent = ((df[ "The work we do here at Communications matters"].value_counts(normalize=True).round(3))*100).round(1)

for word in response:
    if word not in work_comm_matters_percent.index:
        work_comm_matters_percent[word] = 0

work_comm_matters_percent

work_comm_matters_percent_array = [work_comm_matters_percent['Strongly disagree'],work_comm_matters_percent['Disagree'] ,work_comm_matters_percent['Neither agree nor disagree'],work_comm_matters_percent['Agree'], work_comm_matters_percent['Strongly agree']]
work_comm_matters_percent_array      

#GOOD PLACE TO WORK
good_place_percent = ((df[ "Overall, I believe that this is a good place to work"].value_counts(normalize=True).round(3))*100).round(1)

for word in response:
    if word not in good_place_percent.index:
        good_place_percent[word] = 0

good_place_percent

good_place_percent_array = [good_place_percent['Strongly disagree'],good_place_percent['Disagree'] ,good_place_percent['Neither agree nor disagree'],good_place_percent['Agree'], good_place_percent['Strongly agree']]
good_place_percent_array  

##COMBINED PLOT

x_indexes = np.arange(len(opinion)) #create a var (x_indexes) that is an array of values, which
#are a number version of x values. x_indexes is used instead of ages_x to create bar charts next to each other.
width=0.20 #defining the value that is going to be used as width of bars

plt.figure(figsize=(35,17))
plt.bar(x_indexes - width, work_matters_percent_array , width = width, color='#d6001c', label="The work we do here at the University of Calgary matters")
plt.bar(x_indexes,work_comm_matters_percent_array, width = width, color='#ffcd00',label ='The work we do here at Communications matters')  
plt.bar(x_indexes + width,good_place_percent_array , width = width, color='#ff671f', label="Overall, I believe that this is a good place to work")

#ax.set_yticklabels(y_ticks, rotation=0, fontsize=20)
#plt.rc('ytick',labelsize=20)
#plt.rc('xtick', labelsize=20)
ax.tick_params(axis="x", labelsize=20)
ax.tick_params(axis="y")

plt.xticks(ticks=x_indexes, labels=opinion, fontsize = 40) #replaces the indexes with the ages on X axis.
plt.ylabel('Percentage', fontsize = 40)
#plt.tight_layout()
plt.legend(fontsize = 40)
plt.show()     


##Seasonal - Feedback
##AUDIENCE
how_good = ['Extremely good', 'Somewhat good', 'Neither good nor bad','Somewhat bad', 'Extremely bad']
audience_prcnt = ((df[ "I know my target audience"].value_counts(normalize=True).round(3))*100).round(1) 
audience_prcnt    
audience_prcnt_array = [audience_prcnt['Extremely good'],audience_prcnt['Somewhat good'],audience_prcnt['Neither good nor bad'],audience_prcnt['Somewhat bad'],audience_prcnt['Extremely bad'] ]           

x_indexes = np.arange(len(how_good)) #create a var (x_indexes) that is an array of values, which
#are a number version of x values. x_indexes is used instead of ages_x to create bar charts next to each other.
width=0.35 #defining the value that is going to be used as width of bars

plt.figure(figsize=(25,10))
plt.bar(x_indexes,audience_prcnt_array, width = width, color='#d6001c',label ="I know my target audience...")  

ax.tick_params(axis="x", labelsize=20)
ax.tick_params(axis="y")

plt.xticks(ticks=x_indexes, labels=how_good, fontsize = 25) #replaces the indexes with the ages on X axis.
plt.ylabel('Percentage', fontsize = 30)
#plt.tight_layout()
plt.legend(fontsize = 35)
plt.show()


##FEEDBACK
freq = ['Always','Most of the time', 'About half the time', 'Sometimes', 'Never']
feedback_freq_prcnt = ((df[ "I receive feedback from my target audience"].value_counts(normalize=True).round(3))*100).round(1) 
feedback_freq_prcnt
feedback_freq_prcnt_array = [feedback_freq_prcnt['Always'], feedback_freq_prcnt['Most of the time'],feedback_freq_prcnt['About half the time'],feedback_freq_prcnt['Sometimes'],feedback_freq_prcnt['Never']]
x_indexes = np.arange(len(freq)) #create a var (x_indexes) that is an array of values, which
#are a number version of x values. x_indexes is used instead of ages_x to create bar charts next to each other.
width=0.35 #defining the value that is going to be used as width of bars

plt.figure(figsize=(25,10))
plt.bar(x_indexes,feedback_freq_prcnt_array, width = width, color='#d6001c',label ="I receive feedback from my target audience...")  

ax.tick_params(axis="x", labelsize=20)
ax.tick_params(axis="y")

plt.xticks(ticks=x_indexes, labels=freq, fontsize = 25) #replaces the indexes with the ages on X axis.
plt.ylabel('Percentage', fontsize = 30)
#plt.tight_layout()
plt.legend(fontsize = 35)
plt.show()





