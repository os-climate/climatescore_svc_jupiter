from constants import combinedFloodNames


def procCombinedFloodRecord(record, scenarios, years):
    data = record['data']

    lat = ""
    lon = ""
    records = []
    for name in combinedFloodNames:
        if name == "key":
            pass
        if name == "latitude":
            lat = record['latitude']
        if name == "longitude":
            lon = record["longitude"]
        if lat != "" and lon != "":
          
            if (name == "combinedfloodssp1262020floodedfraction200yrmetric_mean" and
                    (2020 in years or years == []) and
                    ("ssp126" in scenarios or scenarios == [])):
                year = 2020
                scenario = "ssp126"
                metric = "floodedfraction200yr"
                metric_mean = data["combinedfloodssp1262020floodedfraction200yrmetric_mean"]
            elif (name == "combinedfloodssp1262030floodedfraction200yrmetric_mean" and
                  (2030 in years or years == []) and
                    ("ssp126" in scenarios or scenarios == [])):
                year = 2030
                scenario = "ssp126"
                metric = "floodedfraction200yr"
                metric_mean = data["combinedfloodssp1262030floodedfraction200yrmetric_mean"]
            elif (name == "combinedfloodssp1262040floodedfraction200yrmetric_mean" and
                  (2040 in years or years == []) and
                    ("ssp126" in scenarios or scenarios == [])):
                year = 2040
                scenario = "ssp126"
                metric = "floodedfraction200yr"
                metric_mean = data["combinedfloodssp1262040floodedfraction200yrmetric_mean"]
            elif (name == "combinedfloodssp1262050floodedfraction200yrmetric_mean" and
                  (2050 in years or years == []) and
                    ("ssp126" in scenarios or scenarios == [])):
                year = 2050
                scenario = "ssp126"
                metric = "floodedfraction200yr"
                metric_mean = data["combinedfloodssp1262050floodedfraction200yrmetric_mean"]
            elif (name == "combinedfloodssp1262075floodedfraction200yrmetric_mean" and
                  (2075 in years or years == []) and
                    ("ssp126" in scenarios or scenarios == [])):
                year = 2075
                scenario = "ssp126"
                metric = "floodedfraction200yr"
                metric_mean = data["combinedfloodssp1262075floodedfraction200yrmetric_mean"]
            elif (name == "combinedfloodssp1262100floodedfraction200yrmetric_mean" and
                  (2100 in years or years == []) and
                    ("ssp126" in scenarios or scenarios == [])):
                year = 2100
                scenario = "ssp126"
                metric = "floodedfraction200yr"
                metric_mean = data["combinedfloodssp1262100floodedfraction200yrmetric_mean"]

            elif (name == "combinedfloodssp5852020floodedfraction200yrmetric_mean" and
                  (2020 in years or years == []) and
                    ("ssp585" in scenarios or scenarios == [])):
                year = 2020
                scenario = "ssp585"
                metric = "floodedfraction200yr"
                metric_mean = data["combinedfloodssp5852020floodedfraction200yrmetric_mean"]
            elif (name == "combinedfloodssp5852030floodedfraction200yrmetric_mean" and
                  (2030 in years or years == []) and
                    ("ssp585" in scenarios or scenarios == [])):
                year = 2030
                scenario = "ssp585"
                metric = "floodedfraction200yr"
                metric_mean = data["combinedfloodssp5852030floodedfraction200yrmetric_mean"]
            elif (name == "combinedfloodssp5852040floodedfraction200yrmetric_mean" and
                  (2040 in years or years == []) and
                    ("ssp585" in scenarios or scenarios == [])):
                year = 2040
                scenario = "ssp585"
                metric = "floodedfraction200yr"
                metric_mean = data["combinedfloodssp5852040floodedfraction200yrmetric_mean"]
            elif (name == "combinedfloodssp5852050floodedfraction200yrmetric_mean" and
                  (2050 in years or years == []) and
                    ("ssp585" in scenarios or scenarios == [])):
                year = 2050
                scenario = "ssp585"
                metric = "floodedfraction200yr"
                metric_mean = data["combinedfloodssp5852050floodedfraction200yrmetric_mean"]
            elif (name == "combinedfloodssp5852075floodedfraction200yrmetric_mean" and
                  (2075 in years or years == []) and
                    ("ssp585" in scenarios or scenarios == [])):
                year = 2075
                scenario = "ssp585"
                metric = "floodedfraction200yr"
                metric_mean = data["combinedfloodssp5852075floodedfraction200yrmetric_mean"]
            elif (name == "combinedfloodssp5852100floodedfraction200yrmetric_mean" and
                  (2100 in years or years == []) and
                    ("ssp585" in scenarios or scenarios == [])):
                year = 2100
                scenario = "ssp585"
                metric = "floodedfraction200yr"
                metric_mean = data["combinedfloodssp5852100floodedfraction200yrmetric_mean"]

            else:
                year = 0
            if (year != 0):
                newRecord = {
                    "latitude": lat,
                    "longitude": lon,
                    "peril": "combinedflood",
                    "peril_code": "FL",
                    "peril_version": "2.1.8",
                    "scenario": scenario,
                    "year": year,
                    "metric": metric,
                    "metric_units": "fraction",
                    "metric_mean": metric_mean,
                    "errors": [],
                    "status": 200
                }
                records.append(newRecord)
                
    return records
