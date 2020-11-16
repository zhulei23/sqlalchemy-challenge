SQLAlchemy Challenge:

Challenge/Task:

Step 1 - Climate Analysis and Exploration
To begin, use Python and SQLAlchemy to do basic climate analysis and data exploration of your climate database. All of the following analysis should be completed using SQLAlchemy ORM queries, Pandas, and Matplotlib.
- Use the provided starter notebook and hawaii.sqlite files to complete your climate analysis and data exploration.
- Choose a start date and end date for your trip. Make sure that your vacation range is approximately 3-15 days total.
- Use SQLAlchemy create_engine to connect to your sqlite database.
- Use SQLAlchemy automap_base() to reflect your tables into classes and save a reference to those classes called Station and Measurement.
- Processes:
    - Python SQL toolkit and Object Relational Mapper
    - Use the Inspector to explore the database and print the table names
    - Use Inspector to print the column names & types for table 'measurement'
    - Use Inspector to print the column names & types for table 'measurement'
    - Use 'engine.execute to select and display first 10 rows of table of measurement'
    - Use 'engine.execute to select and display first 10 rows of table of station'
    - Reflect an existing database into a new model
    - View all of the classes that automap found
    - Save references to each table
    - Map measurement & station class
    - Create our session (link) from Python to the DB

(1) Precipitation Analysis
- Design a query to retrieve the last 12 months of precipitation data.
- Select only the date and prcp values.
- Load the query results into a Pandas DataFrame and set the index to the date column.
- Sort the DataFrame values by date.
- Plot the results using the DataFrame plot method.
- Use Pandas to print the summary statistics for the precipitation data.
- Processes:
    - Select last data point in the database
    - Calculate the date 1 year ago from the last data point in the database
    - Perform a query to retrieve the date and precipitation scores
    - Save the query results as a Pandas DataFrame and set the index to the date column
    - Drop Null value in the DataFrame
    - Sort the dataframe by date
    - Use Pandas Plotting with Matplotlib to plot the date (see fig1)

(2) Station Analysis
- Design a query to calculate the total number of stations.
- Design a query to find the most active stations.
- List the stations and observation counts in descending order.
- Which station has the highest number of observations?
    Hint: You will need to use a function such as func.min, func.max, func.avg, and func.count in your queries.
- Design a query to retrieve the last 12 months of temperature observation data (TOBS).
- Filter by the station with the highest number of observations.
- Plot the results as a histogram with bins=12.
- Processes:
    - Use Pandas to calcualte the summary statistics for the precipitation data
    - Design a query to show how many stations are available in this dataset?
    - List the stations and the counts in descending order.
    - Identify most active station
    - Calculate lowest temperature record for most active station
    - Calculate highest temperature record for most active station
    - Calculate averange temperature record for most active station
    - Choose the station with the highest number of temperature observations.
    - Query the last 12 months of temperature observation data for this station 
    - Create a dataframe with last_year_tob_data
    - Plot the last_year_tob_df as a histogram (see fig2)

Step 2 - Climate App
Now that you have completed your initial analysis, design a Flask API based on the queries that you have just developed.

Use Flask to create your routes.
Routes
- /
- /api/v1.0/precipitation
- /api/v1.0/stations
- /api/v1.0/tobs
- /api/v1.0/<start> and /api/v1.0/<start>/<end>

Bonus: Other Recommended Analyses
The following are optional challenge queries. These are highly recommended to attempt, but not required for the homework.
(1) Temperature Analysis I
- Hawaii is reputed to enjoy mild weather all year. Is there a meaningful difference between the temperature in, for example, June and December?
You may either use SQLAlchemy or pandas's read_csv() to perform this portion.
- Identify the average temperature in June at all stations across all available years in the dataset. Do the same for December temperature.
- Use the t-test to determine whether the difference in the means, if any, is statistically significant. Will you use a paired t-test, or an unpaired t-test? Why?
- Processes:
    - Calculate average temperature for June at all stations for all years
    - Calculate average temperature for December at all stations for all years
    - Create DataFrames for Avg Temperature of June
    - Create DataFrames for Avg Temperature of December
    - Calcuate T-test stats for average temperation between June & December

(2) Temperature Analysis II
- The starter notebook contains a function called calc_temps that will accept a start date and end date in the format %Y-%m-%d. The function will return the minimum, average, and maximum temperatures for that range of dates.
- Use the calc_temps function to calculate the min, avg, and max temperatures for your trip using the matching dates from the previous year (i.e., use "2017-01-01" if your trip start date was "2018-01-01").
- Plot the min, avg, and max temperature from your previous query as a bar chart.
- Use the average temperature as the bar height.
- Use the peak-to-peak (TMAX-TMIN) value as the y error bar (YERR).
- Processes: 
    - Select trip start date (2015-03-26) & end date (2015-04-08)
    - Create a DataFrame for chosen dates data
    - Plot the results from your previous query as a bar chart (see fig3)
    - Use "Trip Avg Temp" as your Title
    - Use the average temperature for the y value
    - Use the peak-to-peak (tmax-tmin) value as the y error bar (yerr)

(3) Daily Rainfall Average
- Calculate the rainfall per weather station using the previous year's matching dates.
- Calculate the daily normals. Normals are the averages for the min, avg, and max temperatures.
- You are provided with a function called daily_normals that will calculate the daily normals for a specific date. This date string will be in the format %m-%d. Be sure to use all historic TOBS that match that date string.
- Create a list of dates for your trip in the format %m-%d. Use the daily_normals function to calculate the normals for each date string and append the results to a list.
- Load the list of daily normals into a Pandas DataFrame and set the index equal to the date.
- Use Pandas to plot an area plot (stacked=False) for the daily normals.
- Processes:
    - Collect all station data with total amount of rainfall
    - Set the start and end date of the trip
    - Use the start and end date to create a range of dates
    - Stip off the year and save a list of %m-%d strings
    - Loop through the list of %m-%d strings and calculate the normals for each date
    - Load the previous query results into a Pandas DataFrame and add the `trip_dates` range as the `date` index
    - Plot the daily normals as an area plot with `stacked=False` (see fig4)
