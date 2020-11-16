import numpy as np
import sqlalchemy
import datetime as dt
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session
from sqlalchemy import create_engine, func

from flask import Flask, jsonify

#################################################
# Database Setup
#################################################
engine = create_engine("sqlite:///Resources/hawaii.sqlite")

# reflect an existing database into a new model
Base = automap_base()
# reflect the tables
Base.prepare(engine, reflect=True)

# Save reference to the table
Measurement = Base.classes.measurement
Station = Base.classes.station

session = Session(engine)

previous_year = dt.date(2017, 8, 23) - dt.timedelta(days=365)

#################################################
# Flask Setup
#################################################
app = Flask(__name__)

#################################################
# Flask Routes
#################################################

@app.route("/")
def welcome():
    """List all available api routes."""
    return (
        f"Available Routes:<br/>"
        f"Preciptitaiton: /api/v1.0/precipitation<br/>"
        f"List of Stations: /api/v1.0/stations<br/>"
        f"Temperature Observations (TOBS) of the most active station for previous year\
        : /api/v1.0/tobs<br/>"
        f"Temperature Stats for a given Start Date: /api/v1.0/<start><br/>"
        f"Temperature Stats for a given Start date to End Date: /api/v1.0/<start>/<end>"
    )

@app.route("/api/v1.0/precipitation")
def precipitation():

    session = Session(engine)

    """Return precipitation result as JSON"""
    # Query results to retrieve data of date & precipitation
    prcp_data = session.query(Measurement.date, Measurement.prcp).\
            filter(Measurement.date >= previous_year).\
            order_by(Measurement.date).all()

    session.close()

    # Create a dictionary using date as the key and prcp as the value
    precipitation = []
    for date, prcp in prcp_data:
        precipitation_dict = {}
        precipitation_dict["date"] = date
        precipitation_dict["precipitation"] = prcp
        precipitation.append(precipitation_dict)

    return jsonify(precipitation)

@app.route("/api/v1.0/stations")
def station():

    session = Session(engine)

    """Return a JSON list of stations from the dataset"""
    station_data = session.query(Station.station, Station.name).all()

    session.close()

    # Create a dictionary to hold station data
    stations = []
    for station, name in station_data:
        station_dict = {}
        station_dict["station"] = station 
        station_dict["name"] = name
        stations.append(station_dict)

    return jsonify(stations)

@app.route("/api/v1.0/tobs")
def tobs():

    session = Session(engine)

    """Return a JSON list of temperature observations (TOBS) for the previous year"""
    
    highest_tob_station = session.query(Measurement.station, func.count(Measurement.tobs))\
                            .group_by(Measurement.station)\
                            .order_by(func.count(Measurement.tobs).desc()).first()[0]
    tobs_data = session.query(Measurement.date, Measurement.station, Measurement.tobs)\
                        .filter(Measurement.station == highest_tob_station)\
                        .filter(Measurement.date >= previous_year).all()
    
    session.close()

    # Create a dictionary to hold TOPS data
    tobs_active = []
    for date, station, tobs in tobs_data:
        tobs_dict = {}
        tobs_dict["date"] = date
        tobs_dict["station"] = station
        tobs_dict["tobs"] = tobs
        tobs_active.append(tobs_dict)

    return jsonify(tobs_active)

@app.route("/api/v1.0/<start>")
def stat1(start):
    
    session = Session(engine)

    """Return a JSON list of the minimum temperature, the average temperature, 
    and the max temperature for all dates greater than and equal to the start date"""
    stats_data = session.query(func.min(Measurement.tobs), func.avg(Measurement.tobs)\
                                , func.max(Measurement.tobs))\
                                .filter(Measurement.date >= start).all()
    
    session.close()

    # Create a dictionary to hold start data
    stats_start = []
    for min, avg, max in stats_data:
        stats_start_dict = {}
        stats_start_dict["min"] = min
        stats_start_dict["avg"] = avg
        stats_start_dict["max"] = max
        stats_start.append(stats_start_dict)

    return jsonify(stats_start)

@app.route("/api/v1.0/<start>/<end>")
def stat2(start, end):

    session=Session(engine)

    """When given the start and the end date, calculate the TMIN, TAVG, and TMAX 
    for dates between the start and end date inclusive."""
    stats_data_2 = session.query(func.min(Measurement.tobs), func.avg(Measurement.tobs)\
                                , func.max(Measurement.tobs))\
                                .filter(Measurement.date >= start)\
                                .filter(Measurement.date <= end).all()
                
    session.close()
    
    # Create a dictionary to hold start/end data
    stats_start_end = []
    for min, avg, max in stats_data_2:
        stats_start_end_dict = {}
        stats_start_end_dict["min"] = min
        stats_start_end_dict["avg"] = avg
        stats_start_end_dict["max"] = max
        stats_start_end.append(stats_start_end_dict)

    return jsonify(stats_start_end)

if __name__ == '__main__':
    app.run(debug=True)
