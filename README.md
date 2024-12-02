# Fundamentals of Programming - Assignment 3

## Data Sources
These four CSVs (located in this repo) were used for the production of the interactive `plotly` graphs. There data was originally taken from the [London Datastore](https://data.london.gov.uk/) and subsequently modified to remove unnecessary data (identified as outside of the data range scope for this task)
- ChildPovertyRatesByBorough.csv
- ChildImmunisationRatesBy5thBirthdayByBorough.csv
- FreeSchoolMealsAndChildDevelopmentByBorough.csv
- FreeSchoolMealsUptakeByBorough.csv

## Data Analysis
The following graphs were created using a combination of the `pandas` and `plotly` modules in Python. The data used compares all boroughs within London.
### Child Poverty vs. Free School Meal Uptake
- Data shows there is a strong positive correlation
- Areas with higher child poverty rates tend to have increased uptake in Free School Meals

#### Example
- Tower Hamlets: 48% child poverty (AHC), 31.3% free school meal uptake in primary schools
- Richmond upon Thames: 12% child poverty (AHC), 7.7% free school meal uptake in primary schools
![Child Poverty vs. Free School Meal Uptake](https://github.com/Luke8218/FoPAssignment3/blob/main/Child%20Poverty%20vs%20Free%20School%20Meals%20Uptake.png)

### Child Poverty vs. Immunization Rates
- Data shows there is a negative correlation
- Areas with higher child poverty rates tend to have lower immunisation rates
- While the correlation is not super strong, the trend is generally consistent across boroughs
![Child Poverty vs. Immunization Rates](https://github.com/Luke8218/FoPAssignment3/blob/main/Child%20Poverty%20vs%20Child%20Immunisation%20Rates.png)

### Child Development by Free School Meal Eligibility
- Data shows there is a strong correlation
- For all boroughs, children who are on Free School Meals have a lower Child Development score compared to children who are not on Free School Meals.
- Across all boroughs, the average percentage difference (disparity) between those on FSM and those not, is 12.09%

#### Example (for Bromley)
- Pupils eligible for free school meals: 59% achieve a good level of development
- All other pupils: 80% achieve a good level of development

#### Additional Findings
Following the creation of the `Child Development by Free School Meal Eligibility` graph, I created a Python script to display the average disparity in 'good level of development' scores across all borough (see [FSMVsChildDevelopmentDisparityCalc](https://github.com/Luke8218/FoPAssignment3/blob/main/FSMVsChildDevelopmentDisparityCalc.py))

This result of this was `12.09` percentage points
![Child Development by Free School Meal Eligibility](https://github.com/Luke8218/FoPAssignment3/blob/main/Free%20School%20Meals%20vs%20Child%20Development.png)
