from python_terraform import *
import logging

class Processor():
    
    def __init__(self):
        self.tf = Terraform()
        self.action = None
        self.logger = logging.getLogger(__name__)

    def process_action(self, action):
        self.action = action
        self.logger.info('Processing action: {}'.format(self.action))

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
