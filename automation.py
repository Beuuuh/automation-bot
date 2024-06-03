#Import libraries
import pyautogui as auto
import time
import pandas as pd

#pausing automation
auto.PAUSE = 1

#start automation
link = ''

def getInTheSite():
    auto.press('win')
    auto.write('brave')
    auto.press('enter')
    auto.write(link)
    auto.press('enter')
    time.sleep(4)
    auto.click(x=1273, y=305)
    auto.click(x=815, y=259)
    auto.press('down')

#Data analysis
chart = pd.read_csv('C:\\Users\\USER\\Repositories\\data_folder\\Receitas.csv')

def dataAnalysis():
    for l in chart.index:
        if('Consultoria em Gestão' in chart.loc[l, 'DESCRIÇÃO']):
            auto.press('enter')
            auto.press('enter')
        elif('Gestão Estratégica' in chart.loc[l,'DESCRIÇÃO']):
            auto.press('enter')
            auto.press('down')
            auto.press('enter')
        elif('Elaboração de Dashboards' in chart.loc[l,'DESCRIÇÃO']):
            auto.press('enter')
            auto.press('down')
            auto.press('down')
            auto.press('enter')
        elif('Planejamento Estratégico' in chart.loc[l,'DESCRIÇÃO']):
            auto.press('enter')
            auto.press('down')
            auto.press('down')
            auto.press('down')
            auto.press('enter')
        auto.scroll(-30)
