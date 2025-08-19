import deutsche_bahn_api.api_authentication as dba
import deutsche_bahn_api.timetable_helper as dbt
import deutsche_bahn_api.station_helper as dbc_s

api = dba.ApiAuthentication("1ac3d18ab81777747efe5f41b6b78ca5", "076006a97b68f3fd1c914ede788c443f")
station_helper = dbc_s.StationHelper()
print(station_helper.find_stations_by_lat_long(48.209166953908536, 11.34949095056929, 2))