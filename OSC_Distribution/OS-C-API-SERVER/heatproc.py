from constants import heatNames


def procHeatRecord(record, scenarios, years):
    data = record['data']
 
    lat = ""
    lon = ""
    records = []
    for name in heatNames:
        if name == "key":
            pass
        if name == "latitude":
            lat = record['latitude']
        if name == "longitude":
            lon = record["longitude"]
        if lat != "" and lon != "":
            if (name == "heatssp1262020daysexceeding35cmetric_mean" and
                    (2020 in years or years == []) and
                    ("ssp126" in scenarios or scenarios == [])):
                year = 2020
                scenario = "ssp126"
                metric = "daysexceeding35c"
                metric_mean = data["heatssp1262020daysexceeding35cmetric_mean"]
            elif (name == "heatssp1262030daysexceeding35cmetric_mean" and
                  (2030 in years or years == []) and
                    ("ssp126" in scenarios or scenarios == [])):
                year = 2030
                scenario = "ssp126"
                metric = "daysexceeding35c"
                metric_mean = data["heatssp1262030daysexceeding35cmetric_mean"]
            elif (name == "heatssp1262040daysexceeding35cmetric_mean" and
                  (2040 in years or years == []) and
                    ("ssp126" in scenarios or scenarios == [])):
                year = 2040
                scenario = "ssp126"
                metric = "daysexceeding35c"
                metric_mean = data["heatssp1262040daysexceeding35cmetric_mean"]
            elif (name == "heatssp1262050daysexceeding35cmetric_mean" and
                  (2050 in years or years == []) and
                    ("ssp126" in scenarios or scenarios == [])):
                year = 2050
                scenario = "ssp126"
                metric = "daysexceeding35c"
                metric_mean = data["heatssp1262050daysexceeding35cmetric_mean"]
            elif (name == "heatssp1262075daysexceeding35cmetric_mean" and
                  (2075 in years or years == []) and
                    ("ssp126" in scenarios or scenarios == [])):
                year = 2075
                scenario = "ssp126"
                metric = "daysexceeding35c"
                metric_mean = data["heatssp1262075daysexceeding35cmetric_mean"]
            elif (name == "heatssp1262100daysexceeding35cmetric_mean" and
                  (2100 in years or years == []) and
                    ("ssp126" in scenarios or scenarios == [])):
                year = 2100
                scenario = "ssp126"
                metric = "daysexceeding35c"
                metric_mean = data["heatssp1262100daysexceeding35cmetric_mean"]

            elif (name == "heatssp5852020daysexceeding35cmetric_mean" and
                  (2020 in years or years == []) and
                    ("ssp585" in scenarios or scenarios == [])):
                year = 2020
                scenario = "ssp585"
                metric = "daysexceeding35c"
                metric_mean = data["heatssp5852020daysexceeding35cmetric_mean"]
            elif (name == "heatssp5852030daysexceeding35cmetric_mean" and
                  (2030 in years or years == []) and
                    ("ssp585" in scenarios or scenarios == [])):
                year = 2030
                scenario = "ssp585"
                metric = "daysexceeding35c"
                metric_mean = data["heatssp5852030daysexceeding35cmetric_mean"]
            elif (name == "heatssp5852040daysexceeding35cmetric_mean" and
                  (2040 in years or years == []) and
                    ("ssp585" in scenarios or scenarios == [])):
                year = 2040
                scenario = "ssp585"
                metric = "daysexceeding35c"
                metric_mean = data["heatssp5852040daysexceeding35cmetric_mean"]
            elif (name == "heatssp5852050daysexceeding35cmetric_mean" and
                  (2050 in years or years == []) and
                    ("ssp585" in scenarios or scenarios == [])):
                year = 2050
                scenario = "ssp585"
                metric = "daysexceeding35c"
                metric_mean = data["heatssp5852050daysexceeding35cmetric_mean"]
            elif (name == "heatssp5852075daysexceeding35cmetric_mean" and
                  (2075 in years or years == []) and
                    ("ssp585" in scenarios or scenarios == [])):
                year = 2075
                scenario = "ssp585"
                metric = "daysexceeding35c"
                metric_mean = data["heatssp5852075daysexceeding35cmetric_mean"]
            elif (name == "heatssp5852100daysexceeding35cmetric_mean" and
                  (2100 in years or years == []) and
                    ("ssp585" in scenarios or scenarios == [])):
                year = 2100
                scenario = "ssp585"
                metric = "daysexceeding35c"
                metric_mean = data["heatssp5852100daysexceeding35cmetric_mean"]

            elif (name == "heatssp1262020daysexceeding38cmetric_mean" and
                    (2020 in years or years == []) and
                    ("ssp126" in scenarios or scenarios == [])):
                year = 2020
                scenario = "ssp126"
                metric = "daysexceeding38c"
                metric_mean = data["heatssp1262020daysexceeding38cmetric_mean"]
            elif (name == "heatssp1262030daysexceeding38cmetric_mean" and
                  (2030 in years or years == []) and
                    ("ssp126" in scenarios or scenarios == [])):
                year = 2030
                scenario = "ssp126"
                metric = "daysexceeding38c"
                metric_mean = data["heatssp1262030daysexceeding38cmetric_mean"]
            elif (name == "heatssp1262040daysexceeding38cmetric_mean" and
                  (2040 in years or years == []) and
                    ("ssp126" in scenarios or scenarios == [])):
                year = 2040
                scenario = "ssp126"
                metric = "daysexceeding38c"
                metric_mean = data["heatssp1262040daysexceeding38cmetric_mean"]
            elif (name == "heatssp1262050daysexceeding38cmetric_mean" and
                  (2050 in years or years == []) and
                    ("ssp126" in scenarios or scenarios == [])):
                year = 2050
                scenario = "ssp126"
                metric = "daysexceeding38c"
                metric_mean = data["heatssp1262050daysexceeding38cmetric_mean"]
            elif (name == "heatssp1262075daysexceeding38cmetric_mean" and
                  (2075 in years or years == []) and
                    ("ssp126" in scenarios or scenarios == [])):
                year = 2075
                scenario = "ssp126"
                metric = "daysexceeding38c"
                metric_mean = data["heatssp1262075daysexceeding38cmetric_mean"]
            elif (name == "heatssp1262100daysexceeding38cmetric_mean" and
                  (2100 in years or years == []) and
                    ("ssp126" in scenarios or scenarios == [])):
                year = 2100
                scenario = "ssp126"
                metric = "daysexceeding38c"
                metric_mean = data["heatssp1262100daysexceeding38cmetric_mean"]

            elif (name == "heatssp5852020daysexceeding38cmetric_mean" and
                  (2020 in years or years == []) and
                    ("ssp585" in scenarios or scenarios == [])):
                year = 2020
                scenario = "ssp585"
                metric = "daysexceeding38c"
                metric_mean = data["heatssp5852020daysexceeding38cmetric_mean"]
            elif (name == "heatssp5852030daysexceeding38cmetric_mean" and
                  (2030 in years or years == []) and
                    ("ssp585" in scenarios or scenarios == [])):
                year = 2030
                scenario = "ssp585"
                metric = "daysexceeding38c"
                metric_mean = data["heatssp5852030daysexceeding38cmetric_mean"]
            elif (name == "heatssp5852040daysexceeding38cmetric_mean" and
                  (2040 in years or years == []) and
                    ("ssp585" in scenarios or scenarios == [])):
                year = 2040
                scenario = "ssp585"
                metric = "daysexceeding38c"
                metric_mean = data["heatssp5852040daysexceeding38cmetric_mean"]
            elif (name == "heatssp5852050daysexceeding38cmetric_mean" and
                  (2050 in years or years == []) and
                    ("ssp585" in scenarios or scenarios == [])):
                year = 2050
                scenario = "ssp585"
                metric = "daysexceeding38c"
                metric_mean = data["heatssp5852050daysexceeding38cmetric_mean"]
            elif (name == "heatssp5852075daysexceeding38cmetric_mean" and
                  (2075 in years or years == []) and
                    ("ssp585" in scenarios or scenarios == [])):
                year = 2075
                scenario = "ssp585"
                metric = "daysexceeding38c"
                metric_mean = data["heatssp5852075daysexceeding38cmetric_mean"]
            elif (name == "heatssp5852100daysexceeding38cmetric_mean" and
                  (2100 in years or years == []) and
                    ("ssp585" in scenarios or scenarios == [])):
                year = 2100
                scenario = "ssp585"
                metric = "daysexceeding38c"
                metric_mean = data["heatssp5852100daysexceeding38cmetric_mean"]


            else:
                year = 0
            if (year != 0):
                newRecord = {
                    "latitude": lat,
                    "longitude": lon,
                    "peril": "heat",
                    "peril_code": "HT",
                    "peril_version": "7.2.1",
                    "scenario": scenario,
                    "year": year,
                    "metric": metric,
                    "metric_units": "days",
                    "metric_mean": metric_mean,
                    "errors": [],
                    "status": 200
                }
                records.append(newRecord)
               
    return records