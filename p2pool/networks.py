from p2pool.bitcoin import networks
from p2pool.util import math

# CHAIN_LENGTH = number of shares back client keeps
# REAL_CHAIN_LENGTH = maximum number of shares back client uses to compute payout
# REAL_CHAIN_LENGTH must always be <= CHAIN_LENGTH
# REAL_CHAIN_LENGTH must be changed in sync with all other clients
# changes can be done by changing one, then the other

nets = dict(

    ###Neisklar: BOOTSTRAP_ADDRS need to be set for a real p2pool network
    ###          PERSIST=True for a p2pool network.
    ###          the settings now are for a solo node, acting as pool
    ###          dunno if these share values needs some tweaking
    ###          The two SPREAD values should definatly be a higher value for such fast coin
    ###          with a relativly low difficulty, so maybe 60, which when we assume the pool 
    ###          gets every third block it's around 90 minutes, means a better distribution of
    ###          earnings, but newer miners will take some time to build up the income.
    quarkbar=math.Object(
        PARENT=networks.nets['quarkbar'],
        SHARE_PERIOD=15, # seconds
        NEW_SHARE_PERIOD=15, # seconds
        CHAIN_LENGTH=24*60*60//10, # shares
        REAL_CHAIN_LENGTH=24*60*60//10, # shares
        TARGET_LOOKBEHIND=50, # shares  //with that the pools share diff is adjusting faster, important if huge hashing power comes to the pool
        SPREAD=30, # blocks
        NEW_SPREAD=30, # blocks
        IDENTIFIER='fc70135c7a811c6f'.decode('hex'),
        PREFIX='9472ef181e1cd37b'.decode('hex'),
        P2P_PORT=17077,
        MIN_TARGET=0,
        MAX_TARGET=2**256//2**20 - 1,
        PERSIST=False,
        WORKER_PORT=7377,
        BOOTSTRAP_ADDRS='67.207.208.166.split(' '),
        ANNOUNCE_CHANNEL='#p2pool-qb',
        VERSION_CHECK=lambda v: True,
    )
    ### Neisklar: that local one was a local testnet
    #quarkcoin_local=math.Object(
        #PARENT=networks.nets['quarkcoin_local'],
        #SHARE_PERIOD=15, # seconds
        #NEW_SHARE_PERIOD=15, # seconds
        #CHAIN_LENGTH=24*60*60//10, # shares
        #REAL_CHAIN_LENGTH=24*60*60//10, # shares
        #TARGET_LOOKBEHIND=200, # shares
        #SPREAD=10, # blocks
        #NEW_SPREAD=10, # blocks
        #IDENTIFIER='fc70335c7a81bc6f'.decode('hex'),
        #PREFIX='7472ef181efcd37b'.decode('hex'),
        #P2P_PORT=18333,
        #MIN_TARGET=0,
        #MAX_TARGET=2**256//2**20 - 1,
        #PERSIST=False,
        #WORKER_PORT=18334,
        #BOOTSTRAP_ADDRS=''.split(' '),
        #ANNOUNCE_CHANNEL='#p2pool',
        #VERSION_CHECK=lambda v: True,
    #),
    
    ###Neisklar: with the changes in the code (hardcoded decimals, use of new POW_HASH config
    ###          and so one, using this version with other coins won't work out of the box

)
for net_name, net in nets.iteritems():
    net.NAME = net_name
