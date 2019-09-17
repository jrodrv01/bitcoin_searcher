from py2neo import Graph, Node, Relationship

class GraphBitcoin(object):

    def __init__(self, host='127.0.0.1', user='neo4j', password='eire'):
        self.graph = Graph(host=host, user=user, password=password)

    def draw_outputs(self, snd_address, hash_transaction, rcv_addresses, block): #Incluir valor del bloque
        
        tx = self.graph.begin()
        tx.run("CREATE (transaction:HashTX {transaction:{transaction}}) RETURN transaction", transaction=hash_transaction)
        tx.commit()

        print("SEND_ADDR: " + snd_address)
        print("HASH: " + hash_transaction)

        list_out_addr = rcv_addresses.keys()
        for addr_out in list_out_addr:
            tx = self.graph.begin()
            tx.run("CREATE (addressOut:AddressOut {addressOut:{addressOut}, amount:{amount}}) RETURN addressOut", addressOut=addr_out,amount=str(rcv_addresses[addr_out]))            

            tx.commit()

            print("ADDR_OUT: " + addr_out + " VALUE ----> " + str(rcv_addresses[addr_out]))

        print("BLOCK: " + str(block))
        tx = self.graph.begin()
        tx.run("CREATE (block:Block {block:{block}}) RETURN block", block=block)
        tx.commit()

        for addr_out in list_out_addr:
            tx = self.graph.begin()
            tx.run("MATCH (a:AddressOut),(tx:HashTX) WHERE (a.addressOut =\'"
                + str(addr_out) + "\' and a.amount=\'" + str(rcv_addresses[addr_out]) 
                + "\') AND tx.transaction = \'" + str(hash_transaction) + "\' CREATE (tx)-[r:SEND_TO]->(a) RETURN a,r,tx")
            tx.commit()

    def draw_inputs(self, snd_address, hash_transaction, rcv_addresses, block):

        list_in_addr = rcv_addresses.keys()
        for addr_in in list_in_addr:
            tx = self.graph.begin()
            tx.run("CREATE (addressIn:AddressIn {addressIn:{addressIn}, amount:{amount}}) RETURN addressIn", addressIn=addr_in,amount=str(rcv_addresses[addr_in]))            

            tx.commit()

            print("ADDR_IN: " + addr_in + " VALUE ----> " + str(rcv_addresses[addr_in]))

        for addr_in in list_in_addr:
            tx = self.graph.begin()
            tx.run("MATCH (a:AddressIn),(tx:HashTX) WHERE (a.addressIn =\'"
                + str(addr_in) + "\' and a.amount=\'" + str(rcv_addresses[addr_in]) 
                + "\') AND tx.transaction = \'" + str(hash_transaction) + "\' CREATE (a)-[s:RECEIVED_FROM]->(tx) RETURN a,s,tx")
            tx.commit()

    def create_nodes(self, list_addresses):
        tx = self.graph.begin()
        for address in list_addresses:
           tx.run("CREATE (address:Address {address:{address}}) RETURN address", address=address)
        
        tx.commit()

