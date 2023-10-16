import plotly.express as px
import pandas as pd

df=pd.DataFrame(columns=['x','y'])
fig=px.bar(df,x='x',y='y', title="sample line animation")

for i in range(30):
    new_fig={'x':[i], 'y':[i * i]}
    fig.add_trace(px.bar(new_fig,x='x',y='y').data[0])
    
fig.show()





