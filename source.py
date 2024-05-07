import json

data = []

for i in range(128):  
    name = f"W{i}"  
    entry = {
        "liqRateM3ToDay": 186.9219,
        "id": i,
        "name": name,
        "type": "SOURCE",
        "debitLiquidCoefficientM3ToDayToBar": 3.0,
        "reservoirPressureBar": 181.0,
        "GOR": 117.0007,
        "WCT": 0.54
    }
    data.append(entry)

print(json.dumps(data, indent=4))
