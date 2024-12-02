import pandas as pd

# Load the data
development = pd.read_csv('FreeSchoolMealsAndChildDevelopmentByBorough.csv')

# Calculate the difference for each borough
development['Disparity'] = (
    development['A good level of development - All other pupils'] - 
    development['A good level of development - Pupils known to be eligible for free school meals']
)

# Calculate the average disparity
average_disparity = development['Disparity'].mean()

print(f"The average disparity in 'good level of development' scores across all boroughs is {average_disparity:.2f} percentage points.")

# Optional: Display the disparity for each borough
for index, row in development.iterrows():
    print(f"{row['Area']}: {row['Disparity']:.2f}")