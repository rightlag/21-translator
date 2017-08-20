import os

from flask import Flask

from two1.wallet import Two1Wallet
from two1.bitserv.flask import Payment

application = Flask(__name__)
payment = Payment(
    application,
    Two1Wallet.import_from_mnemonic(mnemonic=os.getenv('TWO1_WALLET_MNEMONIC')),  # noqa: E501
    username=os.getenv('TWO1_USERNAME')
)

import translator.views  # noqa: E402,F401
