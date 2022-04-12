from brownie import FundMe, accounts, network, config, MockV3Aggregator
from scripts.helpful_scripts import (
    get_account,
    deploy_mocks,
    LOCAL_BLOCKCHAIN_EVIRONMENTS,
)
import time


def deploy_fundme():
    account = get_account()
    # pass the pricefeed address to our fund me contract
    # if on a prsisrtent networkk like rinkeby, use associaed address
    # else ,deploy mocks
    if network.show_active() not in LOCAL_BLOCKCHAIN_EVIRONMENTS:
        pricefeed_address = config["networks"][network.show_active()][
            "eth_usd_price_feed"
        ]

    else:
        deploy_mocks()
        pricefeed_address = MockV3Aggregator[-1].address

    fund_me = FundMe.deploy(
        pricefeed_address,
        {"from": account},
        publish_source=config["networks"][network.show_active()].get("verify"),
    )
    # print(f"contract deployed to{fund_me.address}")
    fund_me.wait(1)
    return fund_me


def main():
    deploy_fundme()
