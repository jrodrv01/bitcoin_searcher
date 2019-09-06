from py2neo import Graph, Node, Relationship

class GraphBitcoin(object):

    def __init__(self, host='127.0.0.1', user='neo4j', password='eire'):
        self.graph = Graph(host=host, user=user, password=password)

    def draw_outputs(self, snd_address, hash_transaction, rcv_address, amount):
        tx = self.graph.begin()
        #tx.run("CREATE (transaction:HashTX {transaction:{transaction}}) RETURN transaction", transaction=hash_transaction)
        #tx.commit()
        tx.run("MATCH (snd_address:Address), (transaction:HashTX) CREATE ({snd_address:{snd_address}})-[:pepe_TO]->({transaction:{transaction}})", snd_address=snd_address, transaction=hash_transaction)
        ## pintar relacion addr-bitcoin - hash
        ## Pintar nodo hash transaccion
        ## pintar relacion hash-addr-bitcoin-output
        tx.commit()
        pass
        
    #MATCH (ES:Sender), (BTC:eWallet) CREATE (ES)-[:SEND_TO]->(BTC)
    def draw_inputs(self):
        pass

    def create_nodes(self, list_addresses):
        tx = self.graph.begin()
        for address in list_addresses:
            tx.run("CREATE (address:Address {address:{address}}) RETURN address", address=address)
        
        tx.commit()

