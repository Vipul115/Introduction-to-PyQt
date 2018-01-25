
# coding: utf-8

# In[1]:


import sys
from PyQt5 import QtWidgets,QtGui
from PyQt5 import QtCore
import pandas as pd
import numpy as np


# In[2]:


df = pd.read_csv('info1.csv', encoding = 'ISO-8859-1')
df.drop('Unnamed: 0', axis = 1, inplace = True)
df
#len(df['period'])
# type(df['period'])


# In[ ]:






# In[3]:


class Windows(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()
        self.setGeometry(100,100,200,200)
        
        b1 = QtWidgets.QPushButton('Quit',self)
        self.setWindowTitle('Weather Forecast')
        
        periods1 = QtWidgets.QLabel(df['period'][0],self)
        periods1.move(90,90)
        periods2 = QtWidgets.QLabel(df['period'][1],self)
        periods3 = QtWidgets.QLabel(df['period'][2],self)
        periods4 = QtWidgets.QLabel(df['period'][3],self)
        periods5 = QtWidgets.QLabel(df['period'][4],self)
        periods6 = QtWidgets.QLabel(df['period'][5],self)
        periods7 = QtWidgets.QLabel(df['period'][6],self)
        periods8 = QtWidgets.QLabel(df['period'][7],self)
        
        
        temp1 = QtWidgets.QLabel(df['temperature'][0],self)
        temp2 = QtWidgets.QLabel(df['temperature'][1],self)
        temp3 = QtWidgets.QLabel(df['temperature'][2],self)
        temp4 = QtWidgets.QLabel(df['temperature'][3],self)
        temp5 = QtWidgets.QLabel(df['temperature'][4],self)
        temp6 = QtWidgets.QLabel(df['temperature'][5],self)
        temp7 = QtWidgets.QLabel(df['temperature'][6],self)
        temp8 = QtWidgets.QLabel(df['temperature'][7],self)
        
        sd1 = QtWidgets.QLabel(df['short_desc'][0],self)
        sd2 = QtWidgets.QLabel(df['short_desc'][1],self)
        sd3 = QtWidgets.QLabel(df['short_desc'][2],self)
        sd4 = QtWidgets.QLabel(df['short_desc'][3],self)
        sd5 = QtWidgets.QLabel(df['short_desc'][4],self)
        sd6 = QtWidgets.QLabel(df['short_desc'][5],self)
        sd7 = QtWidgets.QLabel(df['short_desc'][6],self)
        sd8 = QtWidgets.QLabel(df['short_desc'][7],self)
        
        self.showMaximized()
        
        
if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv) 
    win_obj = Windows()
    sys.exit(app.exec_())

