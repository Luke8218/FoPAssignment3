import pandas as pd
import plotly.graph_objects as go
from plotly.subplots import make_subplots

# Load the data
poverty = pd.read_csv('ChildPovertyRatesByBorough.csv')
immunization = pd.read_csv('ChildImmunisationRatesBy5thBirthdayByBorough.csv')
development = pd.read_csv('FreeSchoolMealsAndChildDevelopmentByBorough.csv')
fsm = pd.read_csv('FreeSchoolMealsUptakeByBorough.csv')

# Merge datasets
merged = pd.merge(poverty, immunization, left_on='Geography code', right_on='Code')
merged = pd.merge(merged, development, left_on='Geography code', right_on='Code')
merged = pd.merge(merged, fsm, left_on='Geography code', right_on='Area Code')

# Create subplots with increased spacing
fig = make_subplots(
    rows=2, cols=2,
    subplot_titles=("Child Poverty vs. Immunization Rates", 
                    "Child Development by Free School Meal Eligibility",
                    "Child Poverty vs. Free School Meal Uptake",
                    "Disparity in Child Development Scores"),
    vertical_spacing=0.2,
    horizontal_spacing=0.1
)

# 1. Child Poverty vs. Immunization Rates
fig.add_trace(
    go.Scatter(
        x=merged['Children in poverty (AHC)'].str.rstrip('%').astype('float'),
        y=merged['Diphtheria, Tetanus, Polio, Pertussis, Hib (DTaP/IPV/HiB)'],
        mode='markers',
        text=merged['Local Authority'],
        name='Boroughs'
    ),
    row=1, col=1
)

# 2. Child Development by Free School Meal Eligibility (reverted to scatter plot)
fig.add_trace(
    go.Scatter(
        x=development['Area'],
        y=development['A good level of development - Pupils known to be eligible for free school meals'],
        mode='markers',
        name='FSM Eligible'
    ),
    row=1, col=2
)
fig.add_trace(
    go.Scatter(
        x=development['Area'],
        y=development['A good level of development - All other pupils'],
        mode='markers',
        name='Not FSM Eligible'
    ),
    row=1, col=2
)

# 3. Child Poverty vs. Free School Meal Uptake
fig.add_trace(
    go.Scatter(
        x=merged['Children in poverty (AHC)'].str.rstrip('%').astype('float'),
        y=merged['MAINTAINED NURSERY AND PRIMARY SCHOOLS - % known to be eligible for and claiming free meals'],
        mode='markers',
        text=merged['Local Authority'],
        name='Boroughs'
    ),
    row=2, col=1
)

# 4. Disparity in Child Development Scores
development['Disparity'] = (
    development['A good level of development - All other pupils'] - 
    development['A good level of development - Pupils known to be eligible for free school meals']
)
fig.add_trace(
    go.Bar(
        x=development['Area'],
        y=development['Disparity'],
        name='Disparity'
    ),
    row=2, col=2
)

# Update layout with increased height and adjusted margins
fig.update_layout(
    height=1200,
    width=1500,
    title_text="Health and Education Inequalities in London Boroughs",
    showlegend=True,
    margin=dict(l=50, r=50, t=100, b=50)
)

# Update axes labels and improve readability
fig.update_xaxes(title_text="Child Poverty Rate (%)", row=1, col=1)
fig.update_yaxes(title_text="DTaP/IPV/HiB Immunization Rate (%)", row=1, col=1)

fig.update_xaxes(title_text="Borough", row=1, col=2, tickangle=45)
fig.update_yaxes(title_text="% Achieving Good Level of Development", row=1, col=2)

fig.update_xaxes(title_text="Child Poverty Rate (%)", row=2, col=1)
fig.update_yaxes(title_text="Free School Meal Uptake (%)", row=2, col=1)

fig.update_xaxes(title_text="Borough", row=2, col=2, tickangle=45)
fig.update_yaxes(title_text="Disparity in Development Scores", row=2, col=2)

# Show the figure
fig.show()
