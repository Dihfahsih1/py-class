import plotly.graph_objs as go
import time

fig = go.Figure()

x_data = []
y_data = []

for i in range(30):
    x_data.append(i)
    y_data.append(i)
    fig.add_trace(go.Scatter(x=x_data, y=y_data, mode='lines', name=f'line{i}'))

    x_data.append(i)
    y_data.append(i * 2)
    fig.add_trace(go.Scatter(x=x_data, y=y_data, mode='lines', name=f'line 2x {i}'))

fig.update_layout(title="Multiple line plots")
fig.show()
time.sleep(2)
