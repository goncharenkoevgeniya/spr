__author__ = 'janie'
# -*-coding:utf-8-*-
from spyre import server
import pandas as pd
from numpy import *
import matplotlib.pyplot as plt
import math
import pylab
from matplotlib import mlab
import os


area = ["Cherkasy","Chernihiv","Chernivci","Crimea","Dnipropetrovs'k","Donets'k","Ivano-Frankivs'k","Kharkiv","Kherson",
        "Khmel'nyts'kyy","Kiev","Kiev City","Kirovohrad","Luhans'k"," L'viv","Mykolayiv","Odessa","Poltava"," Rivne",
        "Sevastopol'","Sumy","Ternopil'","Transcarpathia","Vinnytsya","Volyn","Zaporizhzhya","Zhytomyr"]

areaNumber=['01','02','03','04','05','06','07','08','09','10','11','12','13','14','15','16','17','18','19','20','21',
            '22','23','24','25','26','27']
Index = ['VCI','TCI','VHI']

os.chdir('Download/')
path = os.getcwd()

class DataAnalyze(server.App):
    title = "Geodata analysis"

    inputs = [{     "input_type":'dropdown',
                    "label": 'Index',
                    "options" : [ {"label": "vci", "value":Index[0]},
                                  {"label": "tci", "value":Index[1]},
                                  {"label": "vhi", "value":Index[2]}],
                    "variable_name": 'par',
                    "action_id": "plot" },

             {     "input_type":'dropdown',
                    "label": 'Area ',
                    "options" : [ {"label": area[0], "value":areaNumber[0]},
                                  {"label": area[1], "value":areaNumber[1]},
                                  {"label": area[2], "value":areaNumber[2]},
                                  {"label": area[3], "value":areaNumber[3]},
                                  {"label": area[4], "value":areaNumber[4]},
                                  {"label": area[5], "value":areaNumber[5]},
                                  {"label": area[6], "value":areaNumber[6]},
                                  {"label": area[7], "value":areaNumber[7]},
                                  {"label": area[8], "value":areaNumber[8]},
                                  {"label": area[9], "value":areaNumber[9]},
                                  {"label": area[10], "value":areaNumber[10]},
                                  {"label": area[11], "value":areaNumber[11]},
                                  {"label": area[12], "value":areaNumber[12]},
                                  {"label": area[13], "value":areaNumber[13]},
                                  {"label": area[14], "value":areaNumber[14]},
                                  {"label": area[15], "value":areaNumber[15]},
                                  {"label": area[16], "value":areaNumber[16]},
                                  {"label": area[17], "value":areaNumber[17]},
                                  {"label": area[18], "value":areaNumber[18]},
                                  {"label": area[19], "value":areaNumber[19]},
                                  {"label": area[20], "value":areaNumber[20]},
                                  {"label": area[21], "value":areaNumber[21]},
                                  {"label": area[22], "value":areaNumber[22]},
                                  {"label": area[23], "value":areaNumber[23]},
                                  {"label": area[24], "value":areaNumber[24]},
                                  {"label": area[25], "value":areaNumber[25]},
                                  {"label": area[26], "value":areaNumber[26]},
                                 ],
                    "variable_name": 'ticker',
                    "action_id": "update_data",

              },
        { "input_type":"text",
            "variable_name":"min_week",
            "label": "MIN week",
            "value":35,
            "action_id":"update_data"},
        { "input_type":"text",
            "variable_name":"max_week",
            "label": "MAX week",
            "value":44,
            "action_id":"update_data"}
          ,
        { "input_type":"text",
            "variable_name":"year",
            "label": "year",
            "value":1981,
            "action_id":"plot"}

        ]




    tabs = ["Plot", "Table"]
    outputs = [
                {    "output_type" : "plot",
                    "output_id" : "plot",
                    "control_id" : "update_data",
                    "tab" : "Plot",  # must specify which tab each output should live in
                    "on_page_load" : True },
                {   "output_type" : "table",
                    "output_id" : "table_data",
                    "control_id" : "update_data",
                    "tab" : "Table",
                    "on_page_load" : True }]

    def getData(self, params):
        ticker = str(params['ticker'])
        par = str(params['par'])
        max = int(params['max_week'])
        min = int(params['min_week'])
        year = int(params['year'])
        for file in os.listdir(path):
           if file.startswith(ticker):
               df = pd.read_csv(file, index_col=False, header=1)
               a = df[(df["week"]<=max)]
               b=a[df["week"]>=min]
               c = b[df['year']>0]
               d=c[df['year']==year]
               z = d[df[par]>0]
               return z

    def getPlot(self, params):
        par= str(params['par'])
        w = self.getData(params)
        x = w[[par]]
        y = w['week']
        plt = x.plot(y)
        fig = plt.get_figure()
        return fig
app = DataAnalyze()
app.launch(port=9094)