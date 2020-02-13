from .actions import Processor
from .config import helper
from .config.helper import LIFECYCLE_ACTIONS
from .config.helper import context

def handle_action(action, build, *args, **kwargs):
    print('coming')
    process_handler = Processor()
    pre_context = context({})
    lifecycle = False
    for lc_action in LIFECYCLE_ACTIONS:
        if action == lc_action.value:
            lifecycle = True
    
    if lifecycle:
        pre_context = helper.set_context_for_build(action, build)
    else:
        pre_context.action = action
    print('pre_context' ,pre_context)
    process_handler.process_action(pre_context, *args, **kwargs)
    
