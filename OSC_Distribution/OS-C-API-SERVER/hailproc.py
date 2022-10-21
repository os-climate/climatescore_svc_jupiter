from constants import hailNames


def procHailRecord(record, scenarios, years):
    data = record['data']

    lat = ""
    lon = ""
    records = []
    for name in hailNames:
        if name == "key":
            pass
        if name == "latitude":
            lat = record['latitude']
        if name == "longitude":
            lon = record["longitude"]
        if lat != "" and lon != "":
            if (name == "hailssp1262020dayslargehailpossiblemetric_mean" and
                    (2020 in years or years == []) and
                    ("ssp126" in scenarios or scenarios == [])):
                year = 2020
                scenario = "ssp126"
                metric = "dayslargehailpossible"
                metric_mean = data["hailssp1262020dayslargehailpossiblemetric_mean"]
            elif (name == "hailssp1262030dayslargehailpossiblemetric_mean" and
                  (2030 in years or years == []) and
                    ("ssp126" in scenarios or scenarios == [])):
                year = 2030
                scenario = "ssp126"
                metric = "dayslargehailpossible"
                metric_mean = data["hailssp1262030dayslargehailpossiblemetric_mean"]
            elif (name == "hailssp1262040dayslargehailpossiblemetric_mean" and
                  (2040 in years or years == []) and
                    ("ssp126" in scenarios or scenarios == [])):
                year = 2040
                scenario = "ssp126"
                metric = "dayslargehailpossible"
                metric_mean = data["hailssp1262040dayslargehailpossiblemetric_mean"]
            elif (name == "hailssp1262050dayslargehailpossiblemetric_mean" and
                  (2050 in years or years == []) and
                    ("ssp126" in scenarios or scenarios == [])):
                year = 2050
                scenario = "ssp126"
                metric = "dayslargehailpossible"
                metric_mean = data["hailssp1262050dayslargehailpossiblemetric_mean"]
            elif (name == "hailssp1262075dayslargehailpossiblemetric_mean" and
                  (2075 in years or years == []) and
                    ("ssp126" in scenarios or scenarios == [])):
                year = 2075
                scenario = "ssp126"
                metric = "dayslargehailpossible"
                metric_mean = data["hailssp1262075dayslargehailpossiblemetric_mean"]
            elif (name == "hailssp1262100dayslargehailpossiblemetric_mean" and
                  (2100 in years or years == []) and
                    ("ssp126" in scenarios or scenarios == [])):
                year = 2100
                scenario = "ssp126"
                metric = "dayslargehailpossible"
                metric_mean = data["hailssp1262100dayslargehailpossiblemetric_mean"]

            elif (name == "hailssp5852020dayslargehailpossiblemetric_mean" and
                  (2020 in years or years == []) and
                    ("ssp585" in scenarios or scenarios == [])):
                year = 2020
                scenario = "ssp585"
                metric = "dayslargehailpossible"
                metric_mean = data["hailssp5852020dayslargehailpossiblemetric_mean"]
            elif (name == "hailssp5852030dayslargehailpossiblemetric_mean" and
                  (2030 in years or years == []) and
                    ("ssp585" in scenarios or scenarios == [])):
                year = 2030
                scenario = "ssp585"
                metric = "dayslargehailpossible"
                metric_mean = data["hailssp5852030dayslargehailpossiblemetric_mean"]
            elif (name == "hailssp5852040dayslargehailpossiblemetric_mean" and
                  (2040 in years or years == []) and
                    ("ssp585" in scenarios or scenarios == [])):
                year = 2040
                scenario = "ssp585"
                metric = "dayslargehailpossible"
                metric_mean = data["hailssp5852040dayslargehailpossiblemetric_mean"]
            elif (name == "hailssp5852050dayslargehailpossiblemetric_mean" and
                  (2050 in years or years == []) and
                    ("ssp585" in scenarios or scenarios == [])):
                year = 2050
                scenario = "ssp585"
                metric = "dayslargehailpossible"
                metric_mean = data["hailssp5852050dayslargehailpossiblemetric_mean"]
            elif (name == "hailssp5852075dayslargehailpossiblemetric_mean" and
                  (2075 in years or years == []) and
                    ("ssp585" in scenarios or scenarios == [])):
                year = 2075
                scenario = "ssp585"
                metric = "dayslargehailpossible"
                metric_mean = data["hailssp5852075dayslargehailpossiblemetric_mean"]
            elif (name == "hailssp5852100dayslargehailpossiblemetric_mean" and
                  (2100 in years or years == []) and
                    ("ssp585" in scenarios or scenarios == [])):
                year = 2100
                scenario = "ssp585"
                metric = "dayslargehailpossible"
                metric_mean = data["hailssp5852100dayslargehailpossiblemetric_mean"]

            else:
                year = 0
            if (year != 0):
                newRecord = {
                    "latitude": lat,
                    "longitude": lon,
                    "peril": "hail",
                    "peril_code": "HL",
                    "peril_version": "2.3.1",
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
