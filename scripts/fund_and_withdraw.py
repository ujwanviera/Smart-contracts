from brownie import accounts, FundMe
from scripts.helpful_scripts import get_account

def funding():
    fund_me=FundMe[-1]
    account=get_account()
    entrance_fee = fund_me.getEntranceFee()
    print(entrance_fee)
    print(f"The entry fee is {entrance_fee}")
    print("Funding")
    fund_me.fund({"from":account,"value":entrance_fee})

def withdraw():
    fund_me = FundMe[-1]
    account = get_account()
    fund_me.withdraw({"from":account})

def main():
    funding()   
    withdraw()