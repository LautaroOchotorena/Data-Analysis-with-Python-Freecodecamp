import pandas as pd
import matplotlib.pyplot as plt
from scipy.stats import linregress

def draw_plot():
  # Read data from file
  df = pd.read_csv('epa-sea-level.csv')
  # Create scatter plot
  fig, ax = plt.subplots()
  plt.scatter(data=df, x='Year', y='CSIRO Adjusted Sea Level')

  # Create first line of best fit
  x=df['Year']
  y=df['CSIRO Adjusted Sea Level']
  res = linregress(x, y)
  x = range(1880, 2051, 1)
  plt.plot(x, res.intercept + res.slope*x, 'r', label='fitted line')

  # Create second line of best fit
  x=df[df['Year'] >= 2000]['Year']
  y=df[df['Year'] >= 2000]['CSIRO Adjusted Sea Level']
  res = linregress(x, y)
  x = range(2000, 2051, 1)
  plt.plot(x, res.intercept + res.slope*x, 'g', label='fitted lin2e')


  # Add labels and title
  ax.set_xlabel('Year')
  ax.set_ylabel('Sea Level (inches)')
  ax.set_title('Rise in Sea Level')

  ax.set_xticks(range(1850,2076,25)) #It has to include 2075
  
  # Save plot and return data for testing (DO NOT MODIFY)
  plt.savefig('sea_level_plot.png')
  return plt.gca()