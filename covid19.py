import requests
from pandas import DataFrame
import matplotlib.pyplot as plt
import numpy as np
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import tkinter as tk
from tkinter import ttk


r = requests.get('https://pomber.github.io/covid19/timeseries.json')
data = r.json()

def getChart():

    country = name.get()
    if country == '':
        return
    df = DataFrame(data[country])

    figure = plt.figure()
    subplot = figure.add_subplot(111)
    subplot.plot(df['date'], df['confirmed'], label='confirmed', color='blue')
    subplot.plot(df['date'], df['deaths'], label='deaths', color='red')
    subplot.plot(df['date'], df['recovered'], label='recovered', color='green')
    subplot.legend(loc='upper left')

    start, end = subplot.get_xlim()
    subplot.xaxis.set_ticks(np.arange(start, end, 10))

    for tick in subplot.get_xticklabels():
        tick.set_rotation(45)

    canvas = FigureCanvasTkAgg(figure)
    canvas.get_tk_widget().grid(row=1, column=4, columnspan=3, rowspan=20)
    plt.show()

window = tk.Tk()

name = tk.StringVar()
nameEntered = ttk.Entry(window, width=15, textvariable = name)
nameEntered.grid(column=0, row=1)

button = ttk.Button(window, text = "Show trend for country", command = getChart)
button.grid(column=0, row = 2)

window.mainloop()