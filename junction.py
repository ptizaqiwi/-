import json

data = []

for i in range(135): 
    name = f"J{i+1}"
    entry = {
        "id": i+128,
        "name": name,
        "type": "JUNCTION"
    }
    data.append(entry)

print(json.dumps(data, indent=4))
