import json

data = []

for i in range(128): 
    name = f"W{i}" 
    entry = {
        "id": i,
        "type": "WELL",
        "inletNodeId": i,
        "outletNodeId": i + 128,
        "innerDiameterMm": 100.0,
        "name": name,
        "profileHorDistanceMSpaceHeightM": [
            "0 0",
            "120 0"
        ],
        "roughnessMm": 0.02541,
        "VFPNumber": 1
    }
    data.append(entry)

print(json.dumps(data, indent=4))
