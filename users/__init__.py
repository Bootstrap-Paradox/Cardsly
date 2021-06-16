from .authentication import Authenticate

import sys
sys.path.append("..")
from backend.mail import Mailing_system


auth = Authenticate()

mailing = Mailing_system()