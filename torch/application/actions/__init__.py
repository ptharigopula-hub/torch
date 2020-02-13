from python_terraform import *
import logging

class Processor():
    
    def __init__(self):
        self.tf = Terraform()
        self.action = None
        self.logger = logging.getLogger(__name__)

    def __getattr__(self, item):
        def action_wrapper(*args, **kwargs):
            cmd_name = str(item)
            self.logger.info('called with %r and %r' % (args, kwargs))

            return self.version(cmd_name, *args, **kwargs)

        return action_wrapper

    def process_action(self, action):
        self.action = action
        self.logger.info('Processing action: {}'.format(self.action))
        self.version(self.action)

    def cmd_exection(self, action, *args, **options):
        return_code, stdout, stderr = self.tf.cmd(action, *args, **options)

    def version(self, action, *args, **options):
        return_code, stdout, stderr = self.tf.cmd(action, *args, **options)
        self.logger.info('{}, {}, {}'.format(return_code, stdout, stderr))

    def init(self, *args, **options):
        return_code, stdout, stderr = self.tf.init(*args, **options)

    def plan(self, *args, **options):
        return_code, stdout, stderr = self.tf.plan(*args, **options)

    def apply(self, *args, **options):
        return_code, stdout, stderr = self.tf.apply(*args, **options)

    def destroy(self, *args, **options):
        return_code, stdout, stderr = self.tf.destroy(*args, **options)

    def show(self, *args, **options):
        return_code, stdout, stderr = self.tf.show(*args, **options)
