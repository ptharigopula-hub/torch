from .actions import Processor

def handle_action(action, *args, **kwargs):
    process_handler = Processor()
    process_handler.process_action(action)