import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns
from pandas.plotting import register_matplotlib_converters
register_matplotlib_converters()
import matplotlib.dates as mdates

# Import data (Make sure to parse dates. Consider setting index column to 'date'.)
df = pd.read_csv('fcc-forum-pageviews.csv', index_col='date')
df.index = pd.to_datetime(df.index, format="%Y/%m/%d")

# Clean data
df = df[(df['value'] >= df['value'].quantile(0.025)) & (df['value'] <= df['value'].quantile(0.975))]
def draw_line_plot():
  # Draw line plot
  fig, ax = plt.subplots(figsize=(20,5))
  ax = sns.lineplot(data=df, x=df.index, y='value')
  ax.xaxis.set_major_locator(mdates.MonthLocator(bymonth=(1, 7)))
  ax.xaxis.set_minor_locator(mdates.MonthLocator())
  #labels
  ax.set_title('Daily freeCodeCamp Forum Page Views 5/2016-12/2019')
  ax.set_xlabel('Date')
  ax.set_ylabel('Page Views')


  # Save image and return fig (don't change this part)
  fig.savefig('line_plot.png')
  return fig

def draw_bar_plot():
  # Copy and modify data for monthly bar plot
  df_bar = df.copy()
  df_bar['year'] = df_bar.index.year
  df_bar['month']= df_bar.index.month_name()
  df_bar = df_bar.groupby(['year','month']).mean()
  df_bar = df_bar.reset_index(level=0)

  #Order by months
  months = ["January", "February", "March", "April", "May", "June", "July", "August", "September", "October", "November", "December"]
  df_bar.index = pd.Categorical(df_bar.index, categories=months, ordered=True)

  # Draw bar plot
  fig, ax = plt.subplots()
  ax = sns.barplot(data=df_bar, x=df_bar['year'], y='value', hue=df_bar.index)
  ax.legend(title='Months')
  ax.set_xlabel('Years')
  ax.set_ylabel('Average Page Views')
  
  # Save image and return fig (don't change this part)
  fig.savefig('bar_plot.png')
  return fig

def draw_box_plot():
  # Prepare data for box plots (this part is done!)
  df_box = df.copy()
  df_box.reset_index(inplace=True)
  df_box['year'] = [d.year for d in df_box.date]
  df_box['month'] = [d.strftime('%b') for d in df_box.date]

  #Order by months
  months = ["Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"]
  df_box['month'] = pd.Categorical(df_box['month'], categories=months, ordered=True)

  print(df_box)
  # Draw box plots (using Seaborn)
  fig, ax = plt.subplots(figsize=(15,5))
  #First plot
  ax1 = plt.subplot(1,2,1)
  #Title
  ax1.set_title('Year-wise Box Plot (Trend)')

  #plot
  sns.boxplot(data=df_box,ax=ax1,x='year', y='value')

  #Labels
  ax1.set_xlabel('Year')
  ax1.set_ylabel('Page Views')

  #Second plot
  ax2 = plt.subplot(1,2,2)
  #Title
  ax2.set_title('Month-wise Box Plot (Seasonality)')
  #Plot
  sns.boxplot(data=df_box,ax=ax2,x='month', y='value')
  #Labels
  ax2.set_xlabel('Month')
  ax2.set_ylabel('Page Views')


  # Save image and return fig (don't change this part)
  fig.savefig('box_plot.png')
  return fig