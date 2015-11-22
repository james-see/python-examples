#!/usr/bin/python3
# Author: James Campbell
# Date: November 22 2015
# What: Accesses the blockchain module and queries some data as example

import blockchain
import datetime
from blockchain import blockexplorer
# example address test
address = blockexplorer.get_address('1SDude3hVWoAT2sFxy3JkH2VrcUXPM4PA')
# final balance 
print (address.final_balance) # add decimal after first
transactions = address.transactions
for trans in transactions:
    print(trans.relayed_by) # print ip address of the relayed transaction
    print(trans.hash) # hash of the transaction
    print(trans.time) # time of the transaction
    timestamp = trans.time 
    value = datetime.datetime.fromtimestamp(timestamp)
    print('Converted time:',value.strftime('%Y-%m-%d %H:%M:%S'))
    # inventory only works for transactions up to 1 hour old
    # inv = blockexplorere.get_inventory_data(trans.hash)
    # print('Initial Time: %s Initial IP: %s' % (inv.intial_time,inv.initial_ip))

exit()
