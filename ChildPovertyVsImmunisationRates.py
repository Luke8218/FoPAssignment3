import pandas as pd
import plotly.graph_objects as go

# Load the data (you'll need to adjust the file paths)
poverty = pd.read_csv('ChildPovertyRatesByBorough.csv')
immunization = pd.read_csv('ChildImmunisationRatesBy5thBirthdayByBorough.csv')

# Merge the datasets
merged = pd.merge(poverty, immunization, left_on='Geography code', right_on='Code')

# Create the scatter plot
fig = go.Figure(data=go.Scatter(
    x=merged['Children in poverty (AHC)'].str.rstrip('%').astype('float'),
    y=merged['Diphtheria, Tetanus, Polio, Pertussis, Hib (DTaP/IPV/HiB)'],
    mode='markers',
    text=merged['Local Authority'],
    hoverinfo='text+x+y'
))

fig.update_layout(
    title='Child Poverty vs. Immunization Rates',
    xaxis_title='Child Poverty Rate (After Housing Costs)',
    yaxis_title='DTaP/IPV/HiB Immunization Rate (%)',
    hovermode='closest'
)

fig.show()
