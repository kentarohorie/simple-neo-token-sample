from yourcoin.txio import get_asset_attachments
from yourcoin.token import *
from yourcoin.nep5 import *

ctx = GetContext()
NEP5_METHODS = ['name', 'symbol', 'decimals', 'totalSupply', 'balanceOf', 'transfer', 'transferFrom', 'approve', 'allowance']

def Main(operation, args):
    for op in NEP5_METHODS:
        if operation == op:
            return handle_nep51(ctx, operation, args)
    if operation == 'deploy':
        deploy()

def deploy():
    if not CheckWitness(TOKEN_OWNER):
        print("Must be owner to deploy")
        return False

    if not Get(ctx, 'initialized'):
        # do deploy logic
        Put(ctx, 'initialized', 1)
        Put(ctx, TOKEN_OWNER, TOKEN_INITIAL_AMOUNT)
        return add_to_circulation(ctx, TOKEN_INITIAL_AMOUNT)

    return False
