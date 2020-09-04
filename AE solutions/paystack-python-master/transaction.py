"""Script used to define the paystack Transaction class."""

from paystackapi.base import PayStackBase
import requests
import json
from bs4 import BeautifulSoup

class Transaction(PayStackBase):
    """docstring for Transaction."""

    @classmethod
    def initialize(cls, **kwargs):
        """
        Initialize transaction.

        Args:
            reference: unique transaction reference
            amount: amount
            email: email address
            plan: specified plan(optional)

        Returns:
            Json data from paystack API.
        """

        return cls().requests.post('transaction/initialize', data=kwargs)

    @classmethod
    def charge(cls, **kwargs):
        """
        Charge authorization.

        Args:
            reference: Unique transaction reference
            authorization_code: Authorization code for the transaction
            email: Email Address of the user with the authorization code
            amount: Amount in kobo

        Returns:
            Json data from paystack API.
        """
        return cls().requests.post('transaction/charge_authorization', data=kwargs)

    @classmethod
    def charge_token(cls, **kwargs):
        """
        Charge token.

        Args:
            reference: unique transaction reference
            token: paystack token
            email: Email Address
            amount: Amount in Kobo

        Returns:
            Json data from paystack API.
        """
        return cls().requests.post('transaction/charge_token', data=kwargs)

    @classmethod
    def get(cls, transaction_id):
        """
        Get a single transaction.

        Args:
            transaction_id: Transaction id(integer).

        Returns:
            Json data from paystack API.
        """
        return cls().requests.get(f"transaction/{transaction_id}")

    @classmethod
    def list(cls):
        """
        List transactions.

        Args:
            No argument required.

        Returns:
            Json data from paystack API.
        """
        return cls().requests.get('transaction')

    @classmethod
    def totals(cls):
        """
        Get totals.

        Args:
            No argument required.

        Returns:
            Json data from paystack API.
        """
        return cls().requests.get('transaction/totals')

    @classmethod
    def verify(cls, reference):
        """
        Verify transactions.

        Args:
            reference: a unique value needed for transaction.

        Returns:
            Json data from paystack API.
        """
        return cls().requests.get(f"transaction/verify/{reference}")

money_trans = Transaction()
init = money_trans.initialize(reference='payment013', amount=12000, email='giftoghosa@gmail.com')
#print(init['data']["authorization_url"])
response = requests.get("https://checkout.paystack.com/0b0nv2j427g2brw")
soup = BeautifulSoup(response.text, "html.parser")
print(soup)
#_charge = money_trans.charge(reference='getupall', authorization_code='sk_test_c283fd1e67a0c8ae7ef617e6zbedd7f31c52d66e',
#            email='giftoghosa@gmail.com', amount= 12000)
#veri = money_trans.verify("payment02")
#print(veri["status"],veri["message"],veri["data"])




















