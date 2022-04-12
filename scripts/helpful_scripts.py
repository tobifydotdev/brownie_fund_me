from brownie import network, config, accounts, MockV3Aggregator
from web3 import Web3

FORKED_LOCAL_ENVIRONMENTS = ["mainnet-fork-dev", "mainnet-forks"]
LOCAL_BLOCKCHAIN_EVIRONMENTS = ["development", "ganache-local"]
DECIMALS = 8
STARTING_PRICE = 2000 * 10**8


def get_account():
    if (
        network.show_active() in LOCAL_BLOCKCHAIN_EVIRONMENTS
        or network.show_active in FORKED_LOCAL_ENVIRONMENTS
    ):
        return accounts[0]
    else:
        return accounts.add(config["wallets"]["from_key"])


def deploy_mocks():
    print(f"The active network is {network.show_active}()")
    print("Deploying Mocks...")
    if len(MockV3Aggregator) <= 0:
        mockv3 = MockV3Aggregator.deploy(
            DECIMALS, STARTING_PRICE, ({"from": get_account()})
        )
    print("mocks deployed")
