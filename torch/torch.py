#!/usr/bin/env python
import click
import os
import logging.config
from application import handler
from application.config import clickutil

"""torch.torch: provides entry point main()."""

__version__ = "1.0.0"

logging_conf_path = os.path.normpath(os.path.join(os.path.dirname(__file__), 'logging.conf'))
logging.config.fileConfig(logging_conf_path)
log = logging.getLogger(__name__)

@click.command(name='torch')
@click.argument('action')
@click.option('--build', '-b', 'build', type=click.INT, cls=clickutil.EnsureLifecycleTeardownRelease)
@click.option('--mode', '-m', 'mode', type=click.Choice(['local', 'pipeline'], case_sensitive=False), default='local')
@click.option('--save-state', '-s', 'save_state', type=click.Choice(['local', 'remote', 'all'], case_sensitive=False), default='local')
@click.option('--bucket-name', '-n', 'bucket_name', type=click.STRING, cls=clickutil.EnsureSaveState)
def main(action, build, mode, save_state, bucket_name):
    """Terraform Orchestrator command line utility"""
    log.info("Executing torch version %s" % __version__)
    log.info("Action: %s" % action)
    handler.handle_action(action, build)

if __name__ == "__main__":
    main()
