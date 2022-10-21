from constants import windNames

def procWindRecord(windRecord, scenarios, years):
    data = windRecord['data']
    
    lat = ""
    lon = ""
    records = []
    for windName in windNames:
        if windName == "key":
            pass
        if windName == "latitude":
            lat = windRecord['latitude']
        if windName == "longitude":
            lon = windRecord["longitude"]
        if lat != "" and lon != "":
            if (windName == "windssp1262020windspeed100yrmetric_mean" and
                    (2020 in years or years == []) and
                    ("ssp126" in scenarios or scenarios == [])):
                year = 2020
                scenario = "ssp126"
                metric = "windspeed100yr"
                metric_mean = data["windssp1262020windspeed100yrmetric_mean"]
            elif (windName == "windssp1262030windspeed100yrmetric_mean" and
                  (2030 in years or years == []) and
                    ("ssp126" in scenarios or scenarios == [])):
                year = 2030
                scenario = "ssp126"
                metric = "windspeed100yr"
                metric_mean = data["windssp1262030windspeed100yrmetric_mean"]
            elif (windName == "windssp1262040windspeed100yrmetric_mean" and
                  (2040 in years or years == []) and
                    ("ssp126" in scenarios or scenarios == [])):
                year = 2040
                scenario = "ssp126"
                metric = "windspeed100yr"
                metric_mean = data["windssp1262040windspeed100yrmetric_mean"]
            elif (windName == "windssp1262050windspeed100yrmetric_mean" and
                  (2050 in years or years == []) and
                    ("ssp126" in scenarios or scenarios == [])):
                year = 2050
                scenario = "ssp126"
                metric = "windspeed100yr"
                metric_mean = data["windssp1262050windspeed100yrmetric_mean"]
            elif (windName == "windssp1262075windspeed100yrmetric_mean" and
                  (2075 in years or years == []) and
                    ("ssp126" in scenarios or scenarios == [])):
                year = 2075
                scenario = "ssp126"
                metric = "windspeed100yr"
                metric_mean = data["windssp1262075windspeed100yrmetric_mean"]
            elif (windName == "windssp1262100windspeed100yrmetric_mean" and
                  (2100 in years or years == []) and
                    ("ssp126" in scenarios or scenarios == [])):
                year = 2100
                scenario = "ssp126"
                metric = "windspeed100yr"
                metric_mean = data["windssp1262100windspeed100yrmetric_mean"]

            elif (windName == "windssp5852020windspeed100yrmetric_mean" and
                  (2020 in years or years == []) and
                    ("ssp585" in scenarios or scenarios == [])):
                year = 2020
                scenario = "ssp585"
                metric = "windspeed100yr"
                metric_mean = data["windssp5852020windspeed100yrmetric_mean"]
            elif (windName == "windssp5852030windspeed100yrmetric_mean" and
                  (2030 in years or years == []) and
                    ("ssp585" in scenarios or scenarios == [])):
                year = 2030
                scenario = "ssp585"
                metric = "windspeed100yr"
                metric_mean = data["windssp5852030windspeed100yrmetric_mean"]
            elif (windName == "windssp5852040windspeed100yrmetric_mean" and
                  (2040 in years or years == []) and
                    ("ssp585" in scenarios or scenarios == [])):
                year = 2040
                scenario = "ssp585"
                metric = "windspeed100yr"
                metric_mean = data["windssp5852040windspeed100yrmetric_mean"]
            elif (windName == "windssp5852050windspeed100yrmetric_mean" and
                  (2050 in years or years == []) and
                    ("ssp585" in scenarios or scenarios == [])):
                year = 2050
                scenario = "ssp585"
                metric = "windspeed100yr"
                metric_mean = data["windssp5852050windspeed100yrmetric_mean"]
            elif (windName == "windssp5852075windspeed100yrmetric_mean" and
                  (2075 in years or years == []) and
                    ("ssp585" in scenarios or scenarios == [])):
                year = 2075
                scenario = "ssp585"
                metric = "windspeed100yr"
                metric_mean = data["windssp5852075windspeed100yrmetric_mean"]
            elif (windName == "windssp5852100windspeed100yrmetric_mean" and
                  (2100 in years or years == []) and
                    ("ssp585" in scenarios or scenarios == [])):
                year = 2100
                scenario = "ssp585"
                metric = "windspeed100yr"
                metric_mean = data["windssp5852100windspeed100yrmetric_mean"]

            else:
                year = 0
            if (year != 0):
                newRecord = {
                    "latitude": lat,
                    "longitude": lon,
                    "peril": "wind",
                    "peril_code": "WS",
                    "peril_version": "8.2.3",
                    "scenario": scenario,
                    "year": year,
                    "metric": metric,
                    "metric_units": "m/s",
                    "metric_mean": metric_mean,
                    "errors": [],
                    "status": 200
                }
                records.append(newRecord)
                
    return records