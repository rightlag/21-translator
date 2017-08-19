from flask import Flask

from two1.wallet import Wallet
from two1.bitserv.flask import Payment

application = Flask(__name__)
payment = Payment(application, Wallet())

import translator.views  # noqa: E402,F401
