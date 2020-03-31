#!/usr/bin/python3
import sys
import os
import logging

logging.basicConfig(stream=sys.stderr)
sys.path.insert(0, "/var/www/haddock-api/")
sys.path.insert(0, "/var/www/haddock-api/haddock_api")

VIRTUALENV_LOC = os.environ['VIRTUAL_ENV']

# Activation de l'environnement virtuel
activate_env=os.path.join(VIRTUALENV_LOC, 'bin/activate_this.py')
exec(compile(open(activate_env, "rb").read(), activate_env, 'exec'), {'__file__':activate_env})


from haddock_api.main import app as application

application.secret_key = "d2is1wi921e0938e@(*E*8`&79edejwfd2oies2uU~(*UwEu32"

