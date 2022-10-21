from constants import droughtNames


def procDroughtRecord(record, scenarios, years):
    data = record['data']

    lat = ""
    lon = ""
    records = []
    for name in droughtNames:
        if name == "key":
            pass
        if name == "latitude":
            lat = record['latitude']
        if name == "longitude":
            lon = record["longitude"]
        if lat != "" and lon != "":
            if (name == "droughtssp1262020monthsextreme3mospeimetric_mean" and
                    (2020 in years or years == []) and
                    ("ssp126" in scenarios or scenarios == [])):
                year = 2020
                scenario = "ssp126"
                metric = "monthsextreme3mospei"
                metric_mean = data["droughtssp1262020monthsextreme3mospeimetric_mean"]
            elif (name == "droughtssp1262030monthsextreme3mospeimetric_mean" and
                  (2030 in years or years == []) and
                    ("ssp126" in scenarios or scenarios == [])):
                year = 2030
                scenario = "ssp126"
                metric = "monthsextreme3mospei"
                metric_mean = data["droughtssp1262030monthsextreme3mospeimetric_mean"]
            elif (name == "droughtssp1262040monthsextreme3mospeimetric_mean" and
                  (2040 in years or years == []) and
                    ("ssp126" in scenarios or scenarios == [])):
                year = 2040
                scenario = "ssp126"
                metric = "monthsextreme3mospei"
                metric_mean = data["droughtssp1262040monthsextreme3mospeimetric_mean"]
            elif (name == "droughtssp1262050monthsextreme3mospeimetric_mean" and
                  (2050 in years or years == []) and
                    ("ssp126" in scenarios or scenarios == [])):
                year = 2050
                scenario = "ssp126"
                metric = "monthsextreme3mospei"
                metric_mean = data["droughtssp1262050monthsextreme3mospeimetric_mean"]
            elif (name == "droughtssp1262075monthsextreme3mospeimetric_mean" and
                  (2075 in years or years == []) and
                    ("ssp126" in scenarios or scenarios == [])):
                year = 2075
                scenario = "ssp126"
                metric = "monthsextreme3mospei"
                metric_mean = data["droughtssp1262075monthsextreme3mospeimetric_mean"]
            elif (name == "droughtssp1262100monthsextreme3mospeimetric_mean" and
                  (2100 in years or years == []) and
                    ("ssp126" in scenarios or scenarios == [])):
                year = 2100
                scenario = "ssp126"
                metric = "monthsextreme3mospei"
                metric_mean = data["droughtssp1262100monthsextreme3mospeimetric_mean"]

            elif (name == "droughtssp5852020monthsextreme3mospeimetric_mean" and
                  (2020 in years or years == []) and
                    ("ssp585" in scenarios or scenarios == [])):
                year = 2020
                scenario = "ssp585"
                metric = "monthsextreme3mospei"
                metric_mean = data["droughtssp5852020monthsextreme3mospeimetric_mean"]
            elif (name == "droughtssp5852030monthsextreme3mospeimetric_mean" and
                  (2030 in years or years == []) and
                    ("ssp585" in scenarios or scenarios == [])):
                year = 2030
                scenario = "ssp585"
                metric = "monthsextreme3mospei"
                metric_mean = data["droughtssp5852030monthsextreme3mospeimetric_mean"]
            elif (name == "droughtssp5852040monthsextreme3mospeimetric_mean" and
                  (2040 in years or years == []) and
                    ("ssp585" in scenarios or scenarios == [])):
                year = 2040
                scenario = "ssp585"
                metric = "monthsextreme3mospei"
                metric_mean = data["droughtssp5852040monthsextreme3mospeimetric_mean"]
            elif (name == "droughtssp5852050monthsextreme3mospeimetric_mean" and
                  (2050 in years or years == []) and
                    ("ssp585" in scenarios or scenarios == [])):
                year = 2050
                scenario = "ssp585"
                metric = "monthsextreme3mospei"
                metric_mean = data["droughtssp5852050monthsextreme3mospeimetric_mean"]
            elif (name == "droughtssp5852075monthsextreme3mospeimetric_mean" and
                  (2075 in years or years == []) and
                    ("ssp585" in scenarios or scenarios == [])):
                year = 2075
                scenario = "ssp585"
                metric = "monthsextreme3mospei"
                metric_mean = data["droughtssp5852075monthsextreme3mospeimetric_mean"]
            elif (name == "droughtssp5852100monthsextreme3mospeimetric_mean" and
                  (2100 in years or years == []) and
                    ("ssp585" in scenarios or scenarios == [])):
                year = 2100
                scenario = "ssp585"
                metric = "monthsextreme3mospei"
                metric_mean = data["droughtssp5852100monthsextreme3mospeimetric_mean"]

            else:
                year = 0
            if (year != 0):
                newRecord = {
                    "latitude": lat,
                    "longitude": lon,
                    "peril": "drought",
                    "peril_code": "DT",
                    "peril_version": "7.4.1",
                    "scenario": scenario,
                    "year": year,
                    "metric": metric,
                    "metric_units": "months",
                    "metric_mean": metric_mean,
                    "errors": [],
                    "status": 200
                }
                records.append(newRecord)
                
    return records
