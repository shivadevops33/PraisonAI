from .cli import PraisonAI
import logging
import os
import sys

logging.basicConfig(level=os.environ.get('LOGLEVEL', 'INFO'), format='%(asctime)s - %(levelname)s - %(message)s')

try:
    from .cli import PraisonAI
    praison_ai = PraisonAI()
    praison_ai.main()
except ImportError as e:
    logging.error(f"An import error occurred: {e}")
    sys.exit(1)
except NameError as e:
    logging.error(f"A name error occurred: {e}")
    sys.exit(1)
except Exception as e:
    logging.exception(f"An unexpected error occurred: {e}")
    sys.exit(1)
