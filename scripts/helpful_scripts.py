from brownie import network,config,accounts, MockV3Aggregator
from web3 import Web3

DECIMALS=8
STARTING_PRICE=2
FORKED_LOCAL_ENVIRONMENTS = ["mainnet-fork","mainnet-fork-dev"]
LOCAL_DEVELOPMENT_ENVIRONMENTS =["development","ganache-local"]

def get_account():
    if(network.show_active() in LOCAL_DEVELOPMENT_ENVIRONMENTS or network.show_active() in FORKED_LOCAL_ENVIRONMENTS):
        return  accounts[0]   
    else:
        return accounts.add(config["wallets"]["from_key"])

def deploy_mocks():

    if len(MockV3Aggregator) <=0:
      print("Deploying Mocks...") 
      # refactoring 2000000000000000000 to Web3.toWei(2000,"ether")
      mock_me= MockV3Aggregator.deploy(DECIMALS,Web3.toWei(STARTING_PRICE,"ether"),{"from":get_account()})
      print(f"Mocks deployed to {mock_me.address}")
# Adding ganache/or any other network to brownie we use the command
# brownie networks add Ethereum ganache-local host=http://127.0.0.1:7545 chainid=1337      