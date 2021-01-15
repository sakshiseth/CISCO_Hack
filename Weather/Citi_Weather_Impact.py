import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from datetime import date
from datetime import timedelta
import matplotlib.pyplot as plt

class GetCovidCases:
    def getCases(self):
        today = date.today()
        yesterday = today - timedelta(days=1)
        yes = str(yesterday)
        Y = yes.split('-')
        X = Y[1]+'-'+Y[2]+'-'+Y[0]

        path = 'https://raw.githubusercontent.com/CSSEGISandData/COVID-19/master/csse_covid_19_data/csse_covid_19_daily_reports/'
        path = path + X + '.csv'
        df = pd.read_csv(path)
        df = df.nlargest(10, ['Active'])
        x = df[df.columns[3]]
        y = df[df.columns[10]]
        fig, ax = plt.subplots()
        width = 0.75 # the width of the bars
        ind = np.arange(len(y))  # the x locations for the groups
        ax.barh(ind, y, width, color="blue")
        ax.set_yticks(ind+width/2)
        ax.set_yticklabels(x, minor=False)
        plt.title('title')
        plt.xlabel('x')
        plt.ylabel('y')
        #plt.show()
        plt.savefig('./template/test.png', dpi=300, format='png', bbox_inches='tight')

        explode = []
        for i in range(0,len(y)):
            if i%2 == 0:
                explode.append(0.0)
            else:
                explode.append(0.1)


        plt.subplots(figsize =(15, 12))
        plt.pie(y, labels = x,explode=explode)
        plt.savefig('./template/Weather.jpg')

