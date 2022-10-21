from constants import precipNames


def procPrecipRecord(record, scenarios, years):
    data = record['data']
 
    lat = ""
    lon = ""
    records = []
    for name in precipNames:
        if name == "key":
            pass
        if name == "latitude":
            lat = record['latitude']
        if name == "longitude":
            lon = record["longitude"]
        if lat != "" and lon != "":
            if (name == "precipssp1262020onedayprecip100yrmetric_mean" and
                    (2020 in years or years == []) and
                    ("ssp126" in scenarios or scenarios == [])):
                year = 2020
                scenario = "ssp126"
                metric = "onedayprecip100yr"
                metric_mean = data["precipssp1262020onedayprecip100yrmetric_mean"]
            elif (name == "precipssp1262030onedayprecip100yrmetric_mean" and
                  (2030 in years or years == []) and
                    ("ssp126" in scenarios or scenarios == [])):
                year = 2030
                scenario = "ssp126"
                metric = "onedayprecip100yr"
                metric_mean = data["precipssp1262030onedayprecip100yrmetric_mean"]
            elif (name == "precipssp1262040onedayprecip100yrmetric_mean" and
                  (2040 in years or years == []) and
                    ("ssp126" in scenarios or scenarios == [])):
                year = 2040
                scenario = "ssp126"
                metric = "onedayprecip100yr"
                metric_mean = data["precipssp1262040onedayprecip100yrmetric_mean"]
            elif (name == "precipssp1262050onedayprecip100yrmetric_mean" and
                  (2050 in years or years == []) and
                    ("ssp126" in scenarios or scenarios == [])):
                year = 2050
                scenario = "ssp126"
                metric = "onedayprecip100yr"
                metric_mean = data["precipssp1262050onedayprecip100yrmetric_mean"]
            elif (name == "precipssp1262075onedayprecip100yrmetric_mean" and
                  (2075 in years or years == []) and
                    ("ssp126" in scenarios or scenarios == [])):
                year = 2075
                scenario = "ssp126"
                metric = "onedayprecip100yr"
                metric_mean = data["precipssp1262075onedayprecip100yrmetric_mean"]
            elif (name == "precipssp1262100onedayprecip100yrmetric_mean" and
                  (2100 in years or years == []) and
                    ("ssp126" in scenarios or scenarios == [])):
                year = 2100
                scenario = "ssp126"
                metric = "onedayprecip100yr"
                metric_mean = data["precipssp1262100onedayprecip100yrmetric_mean"]

            elif (name == "precipssp5852020onedayprecip100yrmetric_mean" and
                  (2020 in years or years == []) and
                    ("ssp585" in scenarios or scenarios == [])):
                year = 2020
                scenario = "ssp585"
                metric = "onedayprecip100yr"
                metric_mean = data["precipssp5852020onedayprecip100yrmetric_mean"]
            elif (name == "precipssp5852030onedayprecip100yrmetric_mean" and
                  (2030 in years or years == []) and
                    ("ssp585" in scenarios or scenarios == [])):
                year = 2030
                scenario = "ssp585"
                metric = "onedayprecip100yr"
                metric_mean = data["precipssp5852030onedayprecip100yrmetric_mean"]
            elif (name == "precipssp5852040onedayprecip100yrmetric_mean" and
                  (2040 in years or years == []) and
                    ("ssp585" in scenarios or scenarios == [])):
                year = 2040
                scenario = "ssp585"
                metric = "onedayprecip100yr"
                metric_mean = data["precipssp5852040onedayprecip100yrmetric_mean"]
            elif (name == "precipssp5852050onedayprecip100yrmetric_mean" and
                  (2050 in years or years == []) and
                    ("ssp585" in scenarios or scenarios == [])):
                year = 2050
                scenario = "ssp585"
                metric = "onedayprecip100yr"
                metric_mean = data["precipssp5852050onedayprecip100yrmetric_mean"]
            elif (name == "precipssp5852075onedayprecip100yrmetric_mean" and
                  (2075 in years or years == []) and
                    ("ssp585" in scenarios or scenarios == [])):
                year = 2075
                scenario = "ssp585"
                metric = "onedayprecip100yr"
                metric_mean = data["precipssp5852075onedayprecip100yrmetric_mean"]
            elif (name == "precipssp5852100onedayprecip100yrmetric_mean" and
                  (2100 in years or years == []) and
                    ("ssp585" in scenarios or scenarios == [])):
                year = 2100
                scenario = "ssp585"
                metric = "onedayprecip100yr"
                metric_mean = data["precipssp5852100onedayprecip100yrmetric_mean"]

            else:
                year = 0
            if (year != 0):
                newRecord = {
                    "latitude": lat,
                    "longitude": lon,
                    "peril": "precip",
                    "peril_code": "PR",
                    "peril_version": "3.2.1",
                    "scenario": scenario,
                    "year": year,
                    "metric": metric,
                    "metric_units": "mm",
                    "metric_mean": metric_mean,
                    "errors": [],
                    "status": 200
                }
                records.append(newRecord)
               
    return records
