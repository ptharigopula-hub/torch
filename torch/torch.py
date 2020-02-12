#!/usr/bin/env python
import click
import os
import logging.config
from .application import handler

"""torch.torch: provides entry point main()."""

__version__ = "1.0.0"

logging_conf_path = os.path.normpath(os.path.join(os.path.dirname(__file__), 'logging.conf'))
logging.config.fileConfig(logging_conf_path)
log = logging.getLogger(__name__)

@click.command()
@click.argument('action')
def main(action):
    log.info("Executing torch version %s" % __version__)
    log.info("Action: %s" % action)
    handler.handle_action(action)