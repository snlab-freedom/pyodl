# Set default logging handler to avoid "No handler found" warnings.
import logging
import logging.config

try:  # Python 2.7+
    from logging import NullHandler
except ImportError:
    class NullHandler(logging.Handler):
        def emit(self, record):
            pass

log = logging.getLogger(__name__)
logging.config.fileConfig('logging.conf')
log.addHandler(NullHandler())
