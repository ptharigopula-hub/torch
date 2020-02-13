from python_terraform import *
import logging
from ..config.helper import LIFECYCLE_ACTIONS
from ..config.helper import LIFECYCLE_COMMANDS

class Processor():

    def __init__(self):
        self.tf = Terraform()
        self.action = None
        self.logger = logging.getLogger(__name__)

    # def __getattr__(self, item):
    #     def action_wrapper(*args, **kwargs):
    #         cmd_name = str(item)
    #         self.logger.info('called with %r and %r' % (args, kwargs))

    #         return self.process_cmd(cmd_name, *args, **kwargs)

    #     return action_wrapper

    def process_action(self, context, *args, **kwargs):
        self.action = context['action']
        self.logger.info('Processing action: {}'.format(self.action))
        if self.action == LIFECYCLE_ACTIONS.DEPLOY.value:
            self.process_lifecycle_deploy(context, *args, **kwargs)
        elif self.action == LIFECYCLE_ACTIONS.TEARDOWN.value:
            self.process_lifecycle_teardown(context, *args, **kwargs)
        else:
            self.process_cmd(self.action, *args, **kwargs)

    def process_lifecycle_deploy(self, context, *args, **kwargs):
        for command in LIFECYCLE_COMMANDS.DEPLOY.value:
            self.process_cmd(command, *args, **kwargs)

    def process_lifecycle_teardown(self, context, *args, **kwargs):
        for command in LIFECYCLE_COMMANDS.TEARDOWN.value:
            self.process_cmd(command, *args, **kwargs)

    def process_lifecycle_release(self, context, *args, **kwargs):
        """
        Reserved for future implementation
        """
        pass

    def process_cmd(self, action, *args, **options):
        self.logger.info('Processing command: {0}'.format(action))
        return_code, stdout, stderr = self.tf.cmd(action, *args, **options)
        self.logger.info('Return code: {}, Stdout: {}, {}'.format(return_code, stdout, stderr))
