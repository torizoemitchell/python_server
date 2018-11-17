
import matplotlib.pyplot as plt, mpld3
import jinja2
import requests
import json

def make_graph():
    url = "https://shark-week-server.herokuapp.com/entries/1"
    r = requests.get(url).json()
    entry_list = r


    #base cycle line----------------------------------------------------------------
    entry_nums = []
    temps = []
    # r is a list (an array) of dictionaries (objects)
    # iterate through the list and for each dictionary, get the day and temp
    # push the day into days and the temp into temp for each dictionary
    for i in range(len(entry_list)):
        entry_nums.append(entry_list[i].get('id'))
        temps.append(entry_list[i].get('temp'))
    #plot the
    entry_nums.pop()
    temps.pop()


    #danger days line---------------------------------------------------------------
    danger_days = []
    danger_temps = []

    #iterate through the entires to find a difference in temperature more than 2 tenths of a degree
    checkTemp = entry_list[0].get('temp')
    for i, entry in enumerate(entry_list):
        difference = entry_list[i].get('temp') - checkTemp
        if difference > 0.20:
            #subtract 3 days from the day the difference was observed. Start the ovul. period on that day,with a length of 5.
            danger_period_start = i-4
            danger_period_end = i+3
            #push the days and temps to be charged for the ovul. period to ovulDays and ovulTemps.
            for i in range(danger_period_start, danger_period_end):
                danger_days.append(entry_list[i].get('id'))
                danger_temps.append(entry_list[i].get('temp'))
            break

    #menstration line---------------------------------------------------------------
    mens_days = [1]
    mens_temps = []

    for i, entry in enumerate(entry_list):
        if entry_list[i].get('flow'):
            mens_days.append(entry_list[i].get('id'))
    #get the temps of those days that mens is occurring
    for i in range (len(entry_list)):
        for j in range(len(mens_days)):
            if entry_list[i].get('id') == mens_days[j]:
                mens_temps.append(entry_list[i].get('temp'))
    #get rid of extra numbers (?)
    mens_temps.pop()
    mens_days.pop()

    # print(mens_temps)
    # print(mens_days)

    #hack in a 2nd mens line to simulate start of next period
    next_mens = [29, 30, 31]
    next_temps = [98.6, 98.6, 98.6]

    fig = plt.figure()
    plt.xlabel('entry number')
    plt.ylabel('basal body temp in F')
    plt.title('BBT Over Time')
    #plot base cycle line
    plt.plot(entry_nums, temps, '#bbdefb', label='Normal Days')
    #plot danger line
    plt.plot(danger_days, danger_temps, '#ff6f00', label='Danger Days')
    #plot menstration line
    plt.plot(mens_days, mens_temps, '#42a5f5', label='Period Days')
    plt.legend()
    plt.plot(next_mens, next_temps, '#42a5f5')
    #plt.show()
    #mpld3.show()
    return mpld3.fig_to_html(fig)
