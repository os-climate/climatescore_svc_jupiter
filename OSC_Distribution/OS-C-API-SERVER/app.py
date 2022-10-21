from fireproc import procFireRecord
from combinedfloodproc import procCombinedFloodRecord
from droughtproc import procDroughtRecord
from hailproc import procHailRecord
from heatproc import procHeatRecord
from precipproc import procPrecipRecord
from windproc import procWindRecord
from flask import Flask
from flask import request, jsonify
from flask import abort
import psycopg2
from psycopg2.extras import DictCursor
from constants import fireNames, combinedFloodNames, droughtNames, hailNames, heatNames, precipNames, windNames
from constants import list_of_perils
import os

# export db_host=os-c-db.cfxe5jyx7l0h.us-east-2.rds.amazonaws.com
# export db_port=5432
# export db_database=os-c-db
# export db_user=postgres

db_host = os.environ.get("db_host")
db_port = os.environ.get("db_port")
db_database = os.environ.get("db_database")
db_user = os.environ.get("db_user")
db_password = os.environ.get("db_password")
api_key = os.environ.get("api_key")

print("host:", db_host)
print("port:", db_port)
print("database:", db_database)
print("user:", db_user)
print("pasword:", db_password)

app = Flask(__name__)

try:
    print("Connecting to :", db_host)
    connection = psycopg2.connect(
        host=db_host, port=db_port, database=db_database, user=db_user, password=db_password)
    cursor = connection.cursor()
    print("Connection successul")
except Exception as e:
    print("Connection unsuccessful due to "+str(e))

cursor = connection.cursor(cursor_factory=DictCursor)


def round25(x):
    return (round(x*4)/4)


def dict_from_cursor(fieldNames, cursorList):
    newDict = {}
    for i in range(len(fieldNames)):
        newDict[fieldNames[i]] = str(cursorList[i])
    return newDict


def dict_from_cursor_params(fieldNames, cursorList, year, scenario):
    newDict = {}

    for i in range(len(fieldNames)):
        if (((year != None) and (scenario != None) and (year in fieldNames[i]) and (scenario in fieldNames[i]))
            or ((year != None) and (scenario == None) and (year in fieldNames[i]))
            or ((year == None) and (scenario != None) and (scenario in fieldNames[i]))
                or ((year == None) and (scenario == None))):
            newDict[fieldNames[i]] = str(cursorList[i])

    return newDict


@app.route('/healthz')
def index():
    return 'OK'


def get_fire(key):
    #print("get_fire:", key)
    sql = """ SELECT * FROM osdbfire WHERE key = %s"""
    try:
        cursor.execute(sql, (key,))
        #updated_rows = cursor.rowcount
        connection.commit()
        #print("Number of Rows:", updated_rows)
        row = cursor.fetchone()
        return row
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
    return {}
    # finally:
    #     if conn is not None:
    #         conn.close()


def procFire(lat, lon, key, year, scenario):
    row = get_fire(key)
    if (row != None):
        ret_Val = {
            "peril": "fire",
            "key": key,
            "latitude": lat,
            "longitude": lon,
            "data": []
        }
        if ((year == None) and (scenario == None)):
            newDict = dict_from_cursor(fireNames, row)
        else:
            newDict = dict_from_cursor_params(fireNames, row, year, scenario)
        ret_Val["data"] = newDict
        return ret_Val
    else:
        return {"message:": "Error"}


@app.route('/fire')
def fire():
    headers = request.headers
    auth = headers.get("X-Api-Key")
    if auth != api_key:
        return jsonify({"message": "ERROR; Unauthorized"}), 404
    lat = round25(float(request.args.get('lat')))
    lon = round25(float(request.args.get('lon')))
    key = "{:.2f}".format(lat)+"{:.2f}".format(lon)
    year = request.args.get('year')
    scenario = request.args.get('scenario')
    return procFire(lat, lon, key, year, scenario)


def get_combinedflood(key):
    #print("get_combinedflood:", key)
    sql = """ SELECT * FROM osdbcombinedflood WHERE key = %s"""
    try:
        cursor.execute(sql, (key,))
        #updated_rows = cursor.rowcount
        connection.commit()
        #print("Number of Rows:", updated_rows)
        row = cursor.fetchone()
        return row
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
    return {}
    # finally:
    #     if conn is not None:
    #         conn.close()


def procCombinedFlood(lat, lon, key, year, scenario):
    row = get_combinedflood(key)
    if (row != None):
        ret_Val = {
            "peril": "combinedflood",
            "key": key,
            "latitude": lat,
            "longitude": lon,
            "data": []
        }
        if ((year == None) and (scenario == None)):
            newDict = dict_from_cursor(combinedFloodNames, row)
        else:
            newDict = dict_from_cursor_params(
                combinedFloodNames, row, year, scenario)
        ret_Val["data"] = newDict
        return ret_Val
    else:
        return {"message:": "Error"}


@app.route('/combinedflood')
def combinedflood():
    headers = request.headers
    auth = headers.get("X-Api-Key")
    if auth != api_key:
        return jsonify({"message": "ERROR; Unauthorized"}), 404
    lat = round25(float(request.args.get('lat')))
    lon = round25(float(request.args.get('lon')))
    key = "{:.2f}".format(lat)+"{:.2f}".format(lon)
    year = request.args.get('year')
    scenario = request.args.get('scenario')
    return procCombinedFlood(lat, lon, key, year, scenario)


def get_drought(key):
    print("get_drought:", key)
    sql = """ SELECT * FROM osdbdrought WHERE key = %s"""
    try:
        cursor.execute(sql, (key,))
        #updated_rows = cursor.rowcount
        connection.commit()
        #print("Number of Rows:", updated_rows)
        row = cursor.fetchone()
        return row
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
    return {}
    # finally:
    #     if conn is not None:
    #         conn.close()


def procDrought(lat, lon, key, year, scenario):
    row = get_drought(key)
    if (row != None):
        ret_Val = {
            "peril": "drought",
            "key": key,
            "latitude": lat,
            "longitude": lon,
            "data": []
        }
        if ((year == None) and (scenario == None)):
            newDict = dict_from_cursor(droughtNames, row)
        else:
            newDict = dict_from_cursor_params(
                droughtNames, row, year, scenario)
        ret_Val["data"] = newDict
        return ret_Val
    else:
        return {"message:": "Error"}


@app.route('/drought')
def drought():
    headers = request.headers
    auth = headers.get("X-Api-Key")
    if auth != api_key:
        return jsonify({"message": "ERROR; Unauthorized"}), 404
    lat = round25(float(request.args.get('lat')))
    lon = round25(float(request.args.get('lon')))
    key = "{:.2f}".format(lat)+"{:.2f}".format(lon)
    year = request.args.get('year')
    scenario = request.args.get('scenario')
    return procDrought(lat, lon, key, year, scenario)


def get_hail(key):
    sql = """ SELECT * FROM osdbhail WHERE key = %s"""
    try:
        cursor.execute(sql, (key,))
        #updated_rows = cursor.rowcount
        connection.commit()
        #print("Number of Rows:", updated_rows)
        row = cursor.fetchone()
        return row
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
    return {}
    # finally:
    #     if conn is not None:
    #         conn.close()


def procHail(lat, lon, key, year, scenario):
    row = get_hail(key)
    if (row != None):
        ret_Val = {
            "peril": "hail",
            "key": key,
            "latitude": lat,
            "longitude": lon,
            "data": []
        }
        if ((year == None) and (scenario == None)):
            newDict = dict_from_cursor(hailNames, row)
        else:
            newDict = dict_from_cursor_params(hailNames, row, year, scenario)
        ret_Val["data"] = newDict
        return ret_Val
    else:
        return {"message:": "Error"}


@app.route('/hail')
def hail():
    headers = request.headers
    auth = headers.get("X-Api-Key")
    if auth != api_key:
        return jsonify({"message": "ERROR; Unauthorized"}), 404
    lat = round25(float(request.args.get('lat')))
    lon = round25(float(request.args.get('lon')))
    key = "{:.2f}".format(lat)+"{:.2f}".format(lon)
    year = request.args.get('year')
    scenario = request.args.get('scenario')
    return procHail(lat, lon, key, year, scenario)


def get_heat(key):
    sql = """ SELECT * FROM osdbheat WHERE key = %s"""
    try:
        cursor.execute(sql, (key,))
        #updated_rows = cursor.rowcount
        connection.commit()
        #print("Number of Rows:", updated_rows)
        row = cursor.fetchone()
        return row
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
    return {}
    # finally:
    #     if conn is not None:
    #         conn.close()


def procHeat(lat, lon, key, year, scenario):
    row = get_heat(key)
    if (row != None):
        ret_Val = {
            "peril": "heat",
            "key": key,
            "latitude": lat,
            "longitude": lon,
            "data": []
        }
        if ((year == None) and (scenario == None)):
            newDict = dict_from_cursor(heatNames, row)
        else:
            newDict = dict_from_cursor_params(heatNames, row, year, scenario)
        ret_Val["data"] = newDict
        return ret_Val
    else:
        return {"message:": "Error"}


@app.route('/heat')
def heat():
    headers = request.headers
    auth = headers.get("X-Api-Key")
    if auth != api_key:
        return jsonify({"message": "ERROR; Unauthorized"}), 404
    lat = round25(float(request.args.get('lat')))
    lon = round25(float(request.args.get('lon')))
    key = "{:.2f}".format(lat)+"{:.2f}".format(lon)
    year = request.args.get('year')
    scenario = request.args.get('scenario')
    return procHeat(lat, lon, key, year, scenario)


def get_precip(key):
    sql = """ SELECT * FROM osdbprecip WHERE key = %s"""
    try:
        cursor.execute(sql, (key,))
        #updated_rows = cursor.rowcount
        connection.commit()
        #print("Number of Rows:", updated_rows)
        row = cursor.fetchone()
        return row
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
    return {}
    # finally:
    #     if conn is not None:
    #         conn.close()


def procPrecip(lat, lon, key, year, scenario):
    row = get_precip(key)
    if (row != None):
        ret_Val = {
            "peril": "precip",
            "key": key,
            "latitude": lat,
            "longitude": lon,
            "data": []
        }
        if ((year == None) and (scenario == None)):
            newDict = dict_from_cursor(precipNames, row)
        else:
            newDict = dict_from_cursor_params(precipNames, row, year, scenario)
        ret_Val["data"] = newDict
        return ret_Val
    else:
        return {"message:": "Error"}


@app.route('/precip')
def precip():
    headers = request.headers
    auth = headers.get("X-Api-Key")
    if auth != api_key:
        return jsonify({"message": "ERROR; Unauthorized"}), 404
    lat = round25(float(request.args.get('lat')))
    lon = round25(float(request.args.get('lon')))
    key = "{:.2f}".format(lat)+"{:.2f}".format(lon)
    year = request.args.get('year')
    scenario = request.args.get('scenario')
    return procPrecip(lat, lon, key, year, scenario)


def get_wind(key):
    sql = """ SELECT * FROM osdbwind WHERE key = %s"""
    try:
        cursor.execute(sql, (key,))
        #updated_rows = cursor.rowcount
        connection.commit()
        #print("Number of Rows:", updated_rows)
        row = cursor.fetchone()
        return row
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
    return {}
    # finally:
    #     if conn is not None:
    #         conn.close()


def procWind(lat, lon, key, year, scenario):
    row = get_wind(key)
    if (row != None):
        ret_Val = {
            "peril": "wind",
            "key": key,
            "latitude": lat,
            "longitude": lon,
            "data": []
        }
        if ((year == None) and (scenario == None)):
            newDict = dict_from_cursor(windNames, row)
        else:
            newDict = dict_from_cursor_params(windNames, row, year, scenario)
        ret_Val["data"] = newDict
        return ret_Val
    else:
        return {"message:": "Error"}


@app.route('/wind')
def wind():
    headers = request.headers
    auth = headers.get("X-Api-Key")
    if auth != api_key:
        return jsonify({"message": "ERROR; Unauthorized"}), 404
    lat = round25(float(request.args.get('lat')))
    lon = round25(float(request.args.get('lon')))
    key = "{:.2f}".format(lat)+"{:.2f}".format(lon)
    year = request.args.get('year')
    scenario = request.args.get('scenario')
    return procWind(lat, lon, key, year, scenario)


@app.route('/allperils')
def allperils():
    headers = request.headers
    auth = headers.get("X-Api-Key")
    if auth != api_key:
        return jsonify({"message": "ERROR; Unauthorized"}), 404
    lat = round25(float(request.args.get('lat')))
    lon = round25(float(request.args.get('lon')))
    key = "{:.2f}".format(lat)+"{:.2f}".format(lon)
    data = []
    data.append(procWind(lat, lon, key, None, None))
    data.append(procPrecip(lat, lon, key, None, None))
    data.append(procHeat(lat, lon, key, None, None))
    data.append(procHail(lat, lon, key, None, None))
    data.append(procDrought(lat, lon, key, None, None))
    data.append(procCombinedFlood(lat, lon, key, None, None))
    data.append(procFire(lat, lon, key, None, None))
    ret_Val = {
        "peril": "all",
        "key": key,
        "latitude": lat,
        "longitude": lon,
        "data": data
    }
    return ret_Val


@app.route('/perils')
def perilsHandler():
    headers = request.headers
    auth = headers.get("X-Api-Key")
    print(auth, api_key,auth==api_key)
    if auth != api_key:
        return jsonify({"message": "ERROR; Unauthorized"}), 404

    return list_of_perils


@app.route('/location', methods=['POST'])
def locationHandler():
    headers = request.headers
    auth = headers.get("X-Api-Key")
    if auth != api_key:
        return jsonify({"message": "ERROR; Unauthorized"}), 404
    records = []
    content = request.json

    if not("locations" in content):
        abort(404)

    locations = content["locations"]

    if "perils" in content:
        perils = content['perils']
    else:
        perils = []

    if "scenarios" in content:
        scenarios = content['scenarios']
    else:
        scenarios = []

    if "years" in content:
        years = content['years']
    else:
        years = []

    retMetrics = []
    print("perils:", perils)
    if perils == []:
        perils = ['fire', 'hail', 'heat',
                  'combinedFlood', 'precip', 'drought', 'wind']
    if scenarios == []:
        scenarios = ['ssp126', 'ssp585']
    if years == []:
        years = [2020, 2030, 2040, 2050, 2075, 2100]
    for location in locations:
        lat = round25(float(location["latitude"]))
        lon = round25(float(location["longitude"]))
        key = "{:.2f}".format(lat)+"{:.2f}".format(lon)

        if ("wind" in perils):
            retMetrics.append("windspeed100yr")
            windRecord = procWind(lat, lon, key, None, None)
            windJSON = procWindRecord(windRecord, scenarios, years)
            # print(windJSON)
            records.extend(windJSON)

        if ("precip" in perils):
            retMetrics.append("onedayprecip100yr")
            record = procPrecip(lat, lon, key, None, None)
            recordJSON = procPrecipRecord(record, scenarios, years)
            # print(windJSON)
            records.extend(recordJSON)

        if ("heat" in perils):
            retMetrics.append("daysexceeding35c")
            retMetrics.append("daysexceeding38c")
            record = procHeat(lat, lon, key, None, None)
            recordJSON = procHeatRecord(record, scenarios, years)
            records.extend(recordJSON)

        if ("hail" in perils):
            retMetrics.append("dayslargehailpossible")
            record = procHail(lat, lon, key, None, None)
            recordJSON = procHailRecord(record, scenarios, years)
            records.extend(recordJSON)

        if ("drought" in perils):
            retMetrics.append("monthsextreme3mospei")
            record = procDrought(lat, lon, key, None, None)
            recordJSON = procDroughtRecord(record, scenarios, years)
            records.extend(recordJSON)

        if ("combinedFlood" in perils):
            retMetrics.append("floodedfraction200yr")
            record = procCombinedFlood(lat, lon, key, None, None)
            recordJSON = procCombinedFloodRecord(record, scenarios, years)
            records.extend(recordJSON)

        if ("fire" in perils):
            retMetrics.append("fireProbability")
            record = procFire(lat, lon, key, None, None)
            recordJSON = procFireRecord(record, scenarios, years)
            records.extend(recordJSON)

    retVal = {
        "settings": {
            "csg_version": "2.1.0",
            "perils": perils,
            "metrics": retMetrics,
            "scenarios": scenarios,
            "years": years
        },
        "records": records
    }
    return retVal


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080, threaded=True, debug=True)
