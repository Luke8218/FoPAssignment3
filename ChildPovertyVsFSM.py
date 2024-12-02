import pandas as pd
import plotly.graph_objects as go

# Load the data (you'll need to adjust the file paths)
poverty = pd.read_csv('ChildPovertyRatesByBorough.csv')
fsm = pd.read_csv('FreeSchoolMealsUptakeByBorough.csv')

# Merge the datasets
merged = pd.merge(poverty, fsm, left_on='Geography code', right_on='Area Code')

fig = go.Figure(data=go.Scatter(
    x=merged['Children in poverty (AHC)'].str.rstrip('%').astype('float'),
    y=merged['MAINTAINED NURSERY AND PRIMARY SCHOOLS - % known to be eligible for and claiming free meals'],
    mode='markers',
    text=merged['Local Authority'],
    hoverinfo='text+x+y'
))

fig.update_layout(
    title='Child Poverty vs. Free School Meal Uptake',
    xaxis_title='Child Poverty Rate (After Housing Costs)',
    yaxis_title='Free School Meal Uptake (%)',
    hovermode='closest'
)

fig.show()
