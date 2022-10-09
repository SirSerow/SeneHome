import json

def convert_json():
    with open('decoding.json') as readings:
        dataj = json.load(readings)
    readings.close()
    data = json.loads(dataj)
    converted = str(data["Dn"]) + ':' + str(data["Dm"]) + ':' + str(data["Dx"]) + ':' + str(data["Sn"]) + ':' + str(data["Sm"]) + ':' + str(data["Sx"]) + ':' + str(data["Ta"]) + ':' + str(data["Ua"]) + ':' + str(data["Pa"]) + ':' + str(data["Rc"])
    return converted

def convert_json_input(json_obj):
    data = json.loads(json_obj)
    converted = str(data["Dn"]) + ':' + str(data["Dm"]) + ':' + str(data["Dx"]) + ':' + str(data["Sn"]) + ':' + str(data["Sm"]) + ':' + str(data["Sx"]) + ':' + str(data["Ta"]) + ':' + str(data["Ua"]) + ':' + str(data["Pa"]) + ':' + str(data["Rc"])
    return converted