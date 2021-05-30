#import pandas and plotly.express
import pandas as pd
import plotly.express as px

#read the data and print it
df=pd.read_csv("data.csv")
print(df)

#plot the data on scatter
fig=px.scatter(df,x="Population",y="Per capita",color="Country",size="Percentage",size_max=50)
fig.show()
