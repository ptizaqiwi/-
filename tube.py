import json

data = []

for i in range(135):  # Измените значение диапазона на количество записей данных, которое вы хотите
    entry = {
        "id": i+128,
        "type": "TUBE",
        "inletNodeId": i + 128,
        "outletNodeId": 256,
        "innerDiameterMm": 100.0,
        "name": "",
        "profileHorDistanceMSpaceHeightM": [
            "0 0",
            "120 0"
        ],
        "roughnessMm": 0.02541,
        "VFPNumber": 3
    }
    data.append(entry)

# Вывод созданной структуры данных в формате JSON
print(json.dumps(data, indent=4))
