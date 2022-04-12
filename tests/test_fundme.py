from scripts.helpful_scripts import get_account, LOCAL_BLOCKCHAIN_EVIRONMENTS
from scripts.deploy import deploy_fundme
from brownie import network, accounts, exceptions
import pytest


def test_fund_et_withdarw():
    account = get_account()
    fund_me = deploy_fundme()
    entrance_fee = fund_me.getEntranceFee()
    tx = fund_me.fund({"from": account, "value": entrance_fee})
    tx.wait(1)
    assert fund_me.addressToAmountFunded(account.address) == entrance_fee
    tx2 = fund_me.withdraw({"from": account})
    tx2.wait(1)
    assert fund_me.addressToAmountFunded(account.address) == 0


def test_only_owner_can_withdraw():
    if network.show_active() not in LOCAL_BLOCKCHAIN_EVIRONMENTS:
        pytest.skip("only for local testing")
    account = get_account()
    fund_me = deploy_fundme()
    bad_actor = accounts.add()
    with pytest.raises(exceptions.VirtualMachineError):
        fund_me.withdraw({"from": bad_actor})
