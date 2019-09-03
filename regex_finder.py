import re

# cartera Bitcoin [1 3][a-km-zA-HJ-NP-Z1-9]{25,34}
# cartera Ethereum 0x[a-z0-9]{40} 
# Onion service (?:https?\:\/\/)?[\w\-\.]+\.onion
# Email addres ([\w\.,]+@[\w\.,]+\.\w+)

bitcoin_address_finder=(r'[1 3][a-km-zA-HJ-NP-Z1-9]{25,34}')
ethereum__address_finder=(r'0x[a-z0-9]{40}')
onion_service_finder=(r'(?:https?\:\/\/)?[\w\-\.]+\.onion')
email_address_finder=(r'([\w\.,]+@[\w\.,]+\.\w+)')
bitcoin_hash_finder=(r'[a-fA-F0-9]{64}')


import re
class SearchAddress:
    __init__(self):
        self.regExpBitcoin = r'[1 3][a-km-zA-HJ-NP-Z1-9]{25,34}'

    def bitcoin_address_finder(self, comments):
    addresBitconins = []
        for comment in comments:
            addresBitconins.extend(re.findall(self.regExpBitcoin, comment))
        return addresBitconins


class CommentReader:
    __init__(self):
        pass
    
    def search_comments(self):
        

archivo_leer = f.open

text = 'gfgfdAAA1234ZZZuijjk'

#try:
#    found = re.search('AAA(.+?)ZZZ', text).group(0)
#except AttributeError:
    # AAA, ZZZ not found in the original string
 #   found = '' # apply your error handling

baf = re.findall(bitcoin_address_finder, archivo_o_string, re.MULTILINE)
for b_address in baf:
    guardar(b_address)

eaf = re.findall(ethereum__address_finder, archivo_o_string, re.MULTILINE)
for e_address in eaf
    guardar(e_address)

bhf= re.findall(bitcoin_hash_finder, archivo_o_string, re.MULTILINE)
for b_hash in bhf
    guardar(b_hash)

osf = re.findall(onion_service_finder, archivo_o_string, re.MULTILINE)
for onion_service in osf:
    guardar(onion_service)

emails = re.findall(email_address_finder, archivo_o_string, re.MULTILINE)
for email in emails:
    guardar(email)