from constants import fireNames


def procFireRecord(record, scenarios, years):
    data = record['data']

    lat = ""
    lon = ""
    records = []
    for name in fireNames:
        if name == "key":
            pass
        if name == "latitude":
            lat = record['latitude']
        if name == "longitude":
            lon = record["longitude"]
        if lat != "" and lon != "":

            if (name == "firessp1262020metric_mean" and
                    (2020 in years or years == []) and
                    ("ssp126" in scenarios or scenarios == [])):
                year = 2020
                scenario = "ssp126"
                metric = "fireprobability"
                metric_mean = data["firessp1262020metric_mean"]
            elif (name == "firessp1262030metric_mean" and
                  (2030 in years or years == []) and
                    ("ssp126" in scenarios or scenarios == [])):
                year = 2030
                scenario = "ssp126"
                metric = "fireprobability"
                metric_mean = data["firessp1262030metric_mean"]
            elif (name == "firessp1262040metric_mean" and
                  (2040 in years or years == []) and
                    ("ssp126" in scenarios or scenarios == [])):
                year = 2040
                scenario = "ssp126"
                metric = "fireprobability"
                metric_mean = data["firessp1262040metric_mean"]
            elif (name == "firessp1262050metric_mean" and
                  (2050 in years or years == []) and
                    ("ssp126" in scenarios or scenarios == [])):
                year = 2050
                scenario = "ssp126"
                metric = "fireprobability"
                metric_mean = data["firessp1262050metric_mean"]
            elif (name == "firessp1262075metric_mean" and
                  (2075 in years or years == []) and
                    ("ssp126" in scenarios or scenarios == [])):
                year = 2075
                scenario = "ssp126"
                metric = "fireprobability"
                metric_mean = data["firessp1262075metric_mean"]
            elif (name == "firessp1262100metric_mean" and
                  (2100 in years or years == []) and
                    ("ssp126" in scenarios or scenarios == [])):
                year = 2100
                scenario = "ssp126"
                metric = "fireprobability"
                metric_mean = data["firessp1262100metric_mean"]

            elif (name == "firessp5852020metric_mean" and
                  (2020 in years or years == []) and
                    ("ssp585" in scenarios or scenarios == [])):
                year = 2020
                scenario = "ssp585"
                metric = "fireprobability"
                metric_mean = data["firessp5852020metric_mean"]
            elif (name == "firessp5852030metric_mean" and
                  (2030 in years or years == []) and
                    ("ssp585" in scenarios or scenarios == [])):
                year = 2030
                scenario = "ssp585"
                metric = "fireprobability"
                metric_mean = data["firessp5852030metric_mean"]
            elif (name == "firessp5852040metric_mean" and
                  (2040 in years or years == []) and
                    ("ssp585" in scenarios or scenarios == [])):
                year = 2040
                scenario = "ssp585"
                metric = "fireprobability"
                metric_mean = data["firessp5852040metric_mean"]
            elif (name == "firessp5852050metric_mean" and
                  (2050 in years or years == []) and
                    ("ssp585" in scenarios or scenarios == [])):
                year = 2050
                scenario = "ssp585"
                metric = "fireprobability"
                metric_mean = data["firessp5852050metric_mean"]
            elif (name == "firessp5852075metric_mean" and
                  (2075 in years or years == []) and
                    ("ssp585" in scenarios or scenarios == [])):
                year = 2075
                scenario = "ssp585"
                metric = "fireprobability"
                metric_mean = data["firessp5852075metric_mean"]
            elif (name == "firessp5852100metric_mean" and
                  (2100 in years or years == []) and
                    ("ssp585" in scenarios or scenarios == [])):
                year = 2100
                scenario = "ssp585"
                metric = "fireprobability"
                metric_mean = data["firessp5852100metric_mean"]

            else:
                year = 0
            if (year != 0):
                newRecord = {
                    "latitude": lat,
                    "longitude": lon,
                    "peril": "fire",
                    "peril_code": "FR",
                    "peril_version": "3.2.1",
                    "scenario": scenario,
                    "year": year,
                    "metric": metric,
                    "metric_units": "percent",
                    "metric_mean": metric_mean,
                    "errors": [],
                    "status": 200
                }
                records.append(newRecord)

    return records
