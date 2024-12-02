import pandas as pd
import plotly.graph_objects as go

# Load the data (you'll need to adjust the file path)
development = pd.read_csv('FreeSchoolMealsAndChildDevelopmentByBorough.csv')

fig = go.Figure()

fig.add_trace(go.Scatter(
    x=development['Area'],
    y=development['A good level of development - Pupils known to be eligible for free school meals'],
    mode='markers',
    name='FSM Eligible'
))

fig.add_trace(go.Scatter(
    x=development['Area'],
    y=development['A good level of development - All other pupils'],
    mode='markers',
    name='Not FSM Eligible'
))

fig.update_layout(
    title='Child Development by Free School Meal Eligibility',
    xaxis_title='Borough',
    yaxis_title='% Achieving Good Level of Development',
    hovermode='closest'
)

# Improve readability of x-axis labels
fig.update_xaxes(tickangle=45)

fig.show()
