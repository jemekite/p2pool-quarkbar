import os
import platform

from twisted.internet import defer

from . import data
from p2pool.util import math, pack

nets = dict(
    ###Neisklar: IMPORTANT!!!!!!!!!!!!!1111!!11einself
    ###          The SUBSIDY_FUNC is NOT correctly in terms of keeping the minimum 1 QRK
    ###          Reward for the end of the regular mining period. Means: it will work now
    ###          and some time in the future. I think a simple max(..., 1) around it will fix it
    ###          Maybe the dust threshold should also be rised somewhat, since we only have 5 decimals...
    quarkbar=math.Object(
        P2P_PREFIX='fea503dd'.decode('hex'),
        P2P_PORT=31616,
        ADDRESS_VERSION=58,
        RPC_PORT=31515,
        RPC_CHECK=defer.inlineCallbacks(lambda bitcoind: defer.returnValue(
            'quarkbaraddress' in (yield bitcoind.rpc_help()) and
            not (yield bitcoind.rpc_getinfo())['testnet']
        )),
        SUBSIDY_FUNC=lambda height: 2048*100000000 >> (height + 1)//40320,
        BLOCKHASH_FUNC=lambda data: pack.IntType(256).unpack(__import__('quark_hash').getPoWHash(data)),
        POW_FUNC=lambda data: pack.IntType(256).unpack(__import__('quark_hash').getPoWHash(data)),
        BLOCK_PERIOD=30, # s
        SYMBOL='QB',
        CONF_FILE_FUNC=lambda: os.path.join(os.path.join(os.environ['APPDATA'], 'Quark-bar') if platform.system() == 'Windows' else os.path.expanduser('~/Library/Application Support/Quark-bar/') if platform.system() == 'Darwin' else os.path.expanduser('~/.quark-bar'), 'quarkbar.conf'),
        BLOCK_EXPLORER_URL_PREFIX='',
        ADDRESS_EXPLORER_URL_PREFIX='',
        SANE_TARGET_RANGE=(2**256//2**32//1000 - 1, 2**256//2**20 - 1), 
        DUMB_SCRYPT_DIFF=1,
        DUST_THRESHOLD=0.001e8,
    )
)
for net_name, net in nets.iteritems():
    net.NAME = net_name
