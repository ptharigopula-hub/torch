from .actions import Processor
from .config import helper
from .config.helper import LIFECYCLE_ACTIONS

def handle_action(action, *args, **kwargs):
    process_handler = Processor()
    context = {}
    context['lifecycle'] = False
    context['action'] = action
    for lc_action in LIFECYCLE_ACTIONS:
        if context['action'] == lc_action.value:
            context['lifecycle'] = True
    
    if context['lifecycle']:
        helper.set_context_for_build()
    
    process_handler.process_action(context, *args, **kwargs)
    
