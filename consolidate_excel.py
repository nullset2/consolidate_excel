#reads all excel files in directory, assuming same row-format, and join in a single consolidated CSV volume
#Alfredo Gallegos, Xerox, 2015

import os
import glob
import pandas as pd
import numpy as np
import xlrd

excelfiles = glob.glob("*.xlsx")
globalxl = pd.DataFrame()

for excel in excelfiles:
    print "Processing: %s" % excel

    dataframe = pd.read_excel(excel)

    globalxl = globalxl.append(dataframe, ignore_index = True)

globalxl.to_csv("global_info.csv", encoding = 'utf-8')