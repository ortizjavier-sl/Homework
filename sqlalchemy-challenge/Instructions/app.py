#Import Dependencies 
import numpy as np
import pandas as pd
import datetime as dt
import sqlalchemy
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session
from sqlalchemy import create_engine, func

from flask import Flask, jsonify

engine = create_engine("sqlite:///Resources/hawaii.sqlite")

#Create Engine
engine = create_engine("sqlite:///Resources/hawaii.sqlite")

# Renaming sqlalchemy import 
base = automap_base()

# reflect the tables
base.prepare(engine, reflect = True)

# See available keys
base.classes.keys()

# Assign variable to each key class 
measurement = base.classes.measurement

stations = base.classes.station

# Create our link to our database 
session = Session(engine)


# Flask Setup 
app = Flask(__name__)


#Home page.
#List all routes that are available

@app.route("/")
def home():
    print("Server received request for 'Home' page")
    return (f"Surfs Up! Climate App API<br/>"
    f"/api/v1.0/precipitation<br>"
    f"/api/v1.0/stations<br>"
    f"/api/v1.0/tobs<br>"
    f"/api/v1.0/start<br>"
    f"/api/v1.0/start/end")


# Convert the query results to a dictionary using date as the key and prcp as the value.
# Return the JSON representation of your dictionary.

@app.route("/api/v1.0/precipitation")
def precipitation():
    last_date = session.query(func.max(measurement.date)).all()[0][0]
    last_date = dt.datetime.strptime(last_date, '%Y-%m-%d')

    last_date_year = int(dt.datetime.strftime(last_date, '%Y'))
    last_date_month = int(dt.datetime.strftime(last_date, '%m'))
    last_date_day = int(dt.datetime.strftime(last_date, '%d'))

    last_date_minus365 = dt.date(last_date_year, last_date_month, last_date_day) - dt.timedelta(days=365)

    climate_data = session.query(measurement.date,measurement.prcp)\
    .filter(measurement.date >= last_date_minus365).all()
    climate = {date:prcp for date, prcp in climate_data}
    return jsonify(climate)

# Return a JSON list of stations from the dataset

@app.route("/api/v1.0/stations")
def Stations(): 
    station_count_test = session.query(stations.station).all()
    all_names = list(np.ravel(station_count_test))
    return jsonify(all_names)

#Query the dates and temperature observations of the most active station for the last year of data.
#Return a JSON list of temperature observations (TOBS) for the previous year.

@app.route("/api/v1.0/tobs")
def tobs():
    last_date = session.query(func.max(measurement.date)).all()[0][0]
    last_date = dt.datetime.strptime(last_date, '%Y-%m-%d')

    last_date_year = int(dt.datetime.strftime(last_date, '%Y'))
    last_date_month = int(dt.datetime.strftime(last_date, '%m'))
    last_date_day = int(dt.datetime.strftime(last_date, '%d'))
    last_date_minus365 = dt.date(last_date_year, last_date_month, last_date_day) - dt.timedelta(days=365)
    most_active_stations = (session.query(measurement.station,func.count(measurement.station))\
                       .group_by(measurement.station)\
                       .order_by(func.count(measurement.station).desc())\
                       .all())
    top_active_station = most_active_stations[0][0]
    temperature_observations = session.query(measurement.date,measurement.tobs)\
        .filter(measurement.station == top_active_station)\
            .filter(measurement.date >= last_date_minus365)\
                .order_by(measurement.date.desc())\
                    .all()

    observations_list = []
    for observations in temperature_observations:
        observations_dict = {}
        observations_dict["date"] = observations.date
        observations_dict["tobs"] = observations.tobs
        observations_list.append(observations_dict)

    return jsonify (observations_list)


#Return a JSON list of the minimum temperature, the average temperature, and the max temperature
#  for a given start or start-end range.
#When given the start only, calculate TMIN, TAVG, and TMAX for all dates greater than and equal
#  to the start date.
#When given the start and the end date, calculate the TMIN, TAVG, and TMAX for dates between the
#  start and end date inclusive.

@app.route("/api/v1.0/<start>")
def date(start):
    start_date = dt.datetime.strptime(start,"%Y-%m-%d")

    start_date_stats = session.query(func.max(measurement.tobs), func.min(measurement.tobs),func.avg(measurement.tobs))\
    .filter(measurement.date >= start_date).all()
    session.close()
    start_date_result = list(np.ravel(start_date_stats))
    return jsonify(start_date_result)

@app.route("/api/v1.0/<start>/<end>")
def dates(start,end):
    start_date = dt.datetime.strptime(start,"%Y-%m-%d")
    end_date = dt.datetime.strptime(end,"%Y-%m-%d")

    start_end_date_stats = session.query(func.max(measurement.tobs), func.min(measurement.tobs),func.avg(measurement.tobs))\
    .filter(measurement.date.between(start_date,end_date)).all()
    session.close()

    start_end_date_result = list(np.ravel(start_end_date_stats))
    return jsonify(start_end_date_result)

if __name__ == "__main__":
    app.run(debug=True)