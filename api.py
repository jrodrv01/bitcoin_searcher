import http.client
import json
from datetime import datetime
from Detector import Detector

class API():
    URL = "blockchain.info"
    END_POINT = "/rawaddr/"
    detector=Detector()
    def get_info_address_bitcoin(self, address, out_file):
        connection = http.client.HTTPSConnection(self.URL)
        #169ScU5kenSR4oAvqhWjzDhMZ2iXLCrnVe
        connection.request("GET", self.END_POINT+address,headers={'Content-type':'application/json'})
        response = connection.getresponse()
        my_address =json.loads(response.read())
        
        for _addr in my_address["txs"]:
            print("HASH: " + _addr["hash"])
            for outputs in _addr["out"]:
                out_addr = outputs["value"]
                #transaccion_fecha = out["time"]
                print("OUT ---> " + outputs["addr"])
                print(out_addr)

            
            for inputs in _addr["inputs"]:
                #print(type(inputs["prev_out"]))
                print("INT ---> "+inputs["prev_out"]["addr"])
                print(inputs["prev_out"]["value"])
                #inputJSON = json.loads(inputs)
                #print("-------->" + inputJSON["prev_out"]["addr"])

        s = json.dumps(my_address, indent=4, sort_keys=True)

        f = open (out_file,'w')
        f.write(s)
        f.close()

    def get_info_address_ethereum(self, address, out_file,):
        pass

    def get_evidences(self, list_reg_exp=[r'(?:https?\:\/\/)?[\w\-\.]+\.onion',r'([\w\.,]+@[\w\.,]+\.\w+)']):
        has_evidences=False

        if False:
            pass
            
        return has_evidences

    def run(self):
        self.detector.run()
#print(s)
# cartera Bitcoin [1 3][a-km-zA-HJ-NP-Z1-9]{25,34}
# cartera Ethereum 0x[a-z0-9]{40} 
# Onion service (?:https?\:\/\/)?[\w\-\.]+\.onion
# Email addres ([\w\.,]+@[\w\.,]+\.\w+)

API().get_rawaddress('169ScU5kenSR4oAvqhWjzDhMZ2iXLCrnVe','salida.json')