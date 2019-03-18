#!/usr/local/bin/python3
import datetime as date
import hashlib as hashing

class Block:
    def __init__(self,index,timestamp,data,prevhash):
        self.index=index
        self.data=data
        self.timestamp=timestamp
        self.prevhash=prevhash
        self.hash=self.hashblock()




    def hashblock(self):
        sha=hashing.sha256()
        sha.update(str(self.index).encode())
        sha.update(str(self.timestamp).encode())
        sha.update(str(self.data).encode())
        sha.update(str(self.prevhash).encode())
        return sha.hexdigest()

def create_genesis_block():
  # Manually construct a block with
  # index zero and arbitrary previous hash
  return Block(0, date.datetime.now(), "Genesis Block", "0")
def create_nextblock(prevblock):
    #create next block.
    this_ndx=prevblock.index+1
    this_timestamp=date.datetime.now()
    this_data= "I'am block number" +str(this_ndx)
    this_hash=prevblock.hash
    return Block( this_ndx, this_timestamp,this_data,this_hash)


def main():
    blockchain=[create_genesis_block()]
    previousblock=blockchain[0]
    blocknum=10
    for i in range(0,blocknum):
        blocktoadd=create_nextblock(previousblock)
        blockchain.append(blocktoadd)
        previousblock=blocktoadd
        print ("Block #{} has been added to the blockchain!".format(blocktoadd.index))
        print ("Hash: {}\n".format(blocktoadd.hash))


if __name__=='__main__':
    main()


