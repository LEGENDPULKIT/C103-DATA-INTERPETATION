#import pandas and plotly.express
import pandas as pd
import plotly.express as px

#read the data and print it
df=pd.read_csv("data.csv")
print(df)

#plot the data on bar graph
fig=px.bar(df,x="Country",y="InternetUsers",title="Internet Users")
fig.show()