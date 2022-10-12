from distutils.command.config import config
from brownie import FundMe, MockV3Aggregator, accounts, config, network
#In order to import from other project scripts we need t create __init__.py file to let python be aware that we can import from  project files.
from scripts.helpful_scripts import FORKED_LOCAL_ENVIRONMENTS, deploy_mocks, get_account, LOCAL_DEVELOPMENT_ENVIRONMENTS

def deploy_fund_me():
    account = get_account()
    # If we are on persistent network like Goerli use the associeted address
    # otherwise deploy mocks

    # FORKING in INFURA command: brownie networks add development mainnet-fork-dev cmd=ganache-cli host=http://127.0.0.1 
    # fork='https://mainnet.infura.io/V3/$WEB3_INFURA_PROJECT_ID' accounts=10 mnemonic=brownie port=8545

    # FORKING in ALCHEMY command: brownie networks add development mainnet-fork-dev cmd=ganache-cli host=http://127.0.0.1 
    # fork='https://eth-mainnet.g.alchemy.com/v2/1RJBssE10J0aYwa9_Rvy1DbhssnpYcgp' accounts=10 mnemonic=brownie port=8545

    if (network.show_active() not in LOCAL_DEVELOPMENT_ENVIRONMENTS) and ( network.show_active() not in FORKED_LOCAL_ENVIRONMENTS):
        price_fee_address = config["networks"][{network.show_active()}]["eth_usd_price_feed"]
    else:
        print(f"The active network is {network.show_active()}") 
        #deploying mocks
        deploy_mocks()
        #price feed address
        price_fee_address = MockV3Aggregator[-1].address
                   
    # In the below contract deployment "get("verify")" was used to avoid indexe error. otherwise we could have used "publish_source=config["networks"][network.show_active()]["verify"]"
    fund_me = FundMe.deploy(price_fee_address,{"from":account},publish_source=config["networks"][network.show_active()].get("verify"))
    print(f"Contract deployed to {fund_me.address}")
    return fund_me

def main():
    deploy_fund_me()