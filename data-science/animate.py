import plotly.express as px
import pandas as pd

df=pd.DataFrame(columns=['x','y'])
fig=px.scatter(df, x='x', y='y', title="Sample scatter plot animation")

for i in range(30):
    new_fig={'x':[i], 'y': [i * i -1]}
    fig.add_trace(px.scatter(new_fig, x='x', y='y').data[0])  
fig.show()