import http.client
import json
from datetime import datetime
from detector import Detector
from graphbitcoin import GraphBitcoin

class API():
    URL = "blockchain.info"
    END_POINT = "/rawaddr/"
    REG_EXP_BITCOIN = [r'[1 3][a-km-zA-HJ-NP-Z1-9]{25,34}']
    REG_EXP_EVIDENCES = [r'(?:https?\:\/\/)?[\w\-\.]+\.onion',r'([\w\.,]+@[\w\.,]+\.\w+)']

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
                graph_bitcoin = GraphBitcoin()
                graph_bitcoin.draw_outputs(address,_addr["hash"],out_addr,"asas")
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

        f = open (out_file,'a')
        f.write(s)
        f.close()

    def search_addr_bitcoin(self,file_name='web.csv',output_file_name='address_bicoin.txt'):
        return self.detector.run(reg_exps=self.REG_EXP_BITCOIN,
         file_name=file_name,output_file_name=output_file_name)

    def search_evidences(self,file_name='web.csv',output_file_name='evidences.txt'):
        return self.detector.run(reg_exps=self.REG_EXP_EVIDENCES, 
         file_name=file_name,output_file_name=output_file_name)
#print(s)
# cartera Bitcoin [1 3][a-km-zA-HJ-NP-Z1-9]{25,34}
# cartera Ethereum 0x[a-z0-9]{40} 
# Onion service (?:https?\:\/\/)?[\w\-\.]+\.onion
# Email addres ([\w\.,]+@[\w\.,]+\.\w+)



#MAIN#

evidences = API().search_evidences()
addr_bitcoin = API().search_addr_bitcoin()
print(evidences)
print(addr_bitcoin)

for addr in addr_bitcoin[0]:
    address  = addr.strip(' ')
    API().get_info_address_bitcoin(address,  str(address)+'.json')

graph_bitcoin = GraphBitcoin()
graph_bitcoin.create_nodes(addr_bitcoin[0])
