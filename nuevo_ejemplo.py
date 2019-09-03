import http.client
import json
from datetime import datetime

connection = http.client.HTTPSConnection("blockchain.info")
connection.request("GET", "/rawaddr/3PftbRdnKTQfyZ8fWdH7ddQpxXT6Wh5nfD",headers={'Content-type':'application/json'})
response = connection.getresponse()
str=response.read()
carteraPrimaria = json.loads(str)

for newCartera in carteraPrimaria["txs"]:
    print("HASH: " + newCartera["hash"])
    for out in newCartera["out"]:
        panoja = out["value"]
        #transaccion_fecha = out["time"]
        print("OUT ---> " + out["addr"])
        print(panoja)

    
    for inputs in newCartera["inputs"]:
        #print(type(inputs["prev_out"]))
        print("INT ---> "+inputs["prev_out"]["addr"])
        print(inputs["prev_out"]["value"])
        #inputJSON = json.loads(inputs)
        #print("-------->" + inputJSON["prev_out"]["addr"])

s = json.dumps(carteraPrimaria, indent=4, sort_keys=True)
print(s)
