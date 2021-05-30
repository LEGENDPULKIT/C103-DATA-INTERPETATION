#import pandas and plotly.express
import pandas as pd
import plotly.express as px

#read the data and print it
df=pd.read_csv("line_chart.csv")
print(df)

#plot the data on line graph
fig=px.line(df,x="Year",y="Per capita income",color="Country",title="Per Capita income")
fig.show()