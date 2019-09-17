import http.client
import json
from datetime import datetime
from detector import Detector
from graphbitcoin import GraphBitcoin
import os

class API():
    URL = "blockchain.info"
    END_POINT = "/rawaddr/"
    REG_EXP_BITCOIN = [r'[1 3][a-km-zA-HJ-NP-Z1-9]{25,34}']
    REG_EXP_EVIDENCES = [r'(?:https?\:\/\/)?[\w\-\.]+\.onion',r'([\w\.,]+@[\w\.,]+\.\w+)']

    detector=Detector()
    def get_info_address_bitcoin(self, address, out_file):
        connection = http.client.HTTPSConnection(self.URL)
        connection.request("GET", self.END_POINT+address,headers={'Content-type':'application/json'})
        response = connection.getresponse()
        my_address =json.loads(response.read())
        
        list_data = {}
        list_data_input = {}
        list_hashes_address = []
        

        for _addr in my_address["txs"]:
            
            height_block = _addr["block_height"]
            
            data_hash = {}

            for outputs in _addr["out"]:
                out_addr = outputs["addr"]
                data_hash[out_addr] = outputs["value"]
                

            list_data[_addr["hash"]] = data_hash
            graph_bitcoin = GraphBitcoin()
            graph_bitcoin.draw_outputs(address,_addr["hash"],data_hash,height_block)

            data_hash = {}
            
            for inputs in _addr["inputs"]:
                in_addr = inputs["prev_out"]["addr"]
                data_hash[in_addr] = inputs["prev_out"]["value"]

            list_data_input[_addr["hash"]] = data_hash

            graph_bitcoin = GraphBitcoin()
            graph_bitcoin.draw_inputs(address,_addr["hash"],data_hash,height_block)

        list_hashes_address.append(dict.fromkeys(list_data).keys())
        list_hashes_address.append(dict.fromkeys(list_data_input).keys())

        s = json.dumps(my_address, indent=4, sort_keys=True)

        f = open (out_file,'w')
        f.write(s)
        f.close()

    def search_addr_bitcoin(self,file_name='web.csv',output_file_name='address_bitcoin.txt'):
        return self.detector.run(reg_exps=self.REG_EXP_BITCOIN,
         file_name=file_name,output_file_name=output_file_name)

    def search_evidences(self,file_name='web.csv',output_file_name='evidences.txt'):
        return self.detector.run(reg_exps=self.REG_EXP_EVIDENCES, 
         file_name=file_name,output_file_name=output_file_name)

#MAIN#

os.system("rm *.json *.txt")

evidences = API().search_evidences()
addr_bitcoin = API().search_addr_bitcoin()

graph_bitcoin = GraphBitcoin()

graph_bitcoin.create_nodes(addr_bitcoin[0])

for addr in addr_bitcoin[0]:
    address  = addr.strip(' ')
    API().get_info_address_bitcoin(address,  str(address)+'.json')

