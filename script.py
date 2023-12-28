# Testing AceBank Class in src/AceBank
import logging
import os
import sys

from src.BankAccount import AceBank

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
    datefmt="%Y-%m-%d %H:%M:%S %p",
)
LOG = logging.getLogger(os.path.basename(sys.argv[0]))

if __name__ == "__main__":
    # initiate AceBank with customer id 234
    ab = AceBank(LOG)
    # setup account for customer 234
    ab.create_account(account_number="0808", balance=1000.00, customer_id=234)
    # deposit money for account 0808
    ab.deposit_fund("0808", 500.00, "USD", 234)

    # withdraw from account 0808
    ab.withdraw_funds("0808", 100.00, "CAD", 234)

    # get balance from account 0808
    balance = ab.get_balance("0808", 234)
    LOG.info(f"Balance of account 0808 after last transaction is {balance}")

    # initiate AceBank with customer id 756
    ab = AceBank(LOG)
    # setup accounts for customer 756
    ab.create_account(account_number="0903", balance=100.00, customer_id=756)
    ab.create_account(account_number="0875", balance=6000.00, customer_id=756)

    # withdraw from account 0875
    ab.withdraw_funds("0875", 700.00, "USD", 756)
    # deposit fund to 0903
    ab.deposit_fund("0903", 2500.00, "EUROS", 756)

    # transfer fund from 0875 to 0903
    ab.transfer_funds("0875", "0903", 1100.00, 756, 756)

    # get balance from account 0808
    balance_0875 = ab.get_balance("0875", 756)
    balance_0903 = ab.get_balance("0903", 756)
    LOG.info(f"Balance of account 0875 after last transaction is {balance_0875}")
    LOG.info(f"Balance of account 0903 after last transaction is {balance_0903}")
