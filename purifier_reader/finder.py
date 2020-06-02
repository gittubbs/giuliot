from miio.miioprotocol import MiIOProtocol
import logging
#from miio.vacuum_cli
logger = logging.getLogger(__name__)
logging.basicConfig(level=logging.INFO)

MiIOProtocol.discover()