import click

from .helper import LIFECYCLE_ACTIONS 

class EnsureLifecycleTeardownRelease(click.Option):

    def full_process_value(self, ctx, value):
        value = super(EnsureLifecycleTeardownRelease, self).full_process_value(ctx, value)

        if value is None and (ctx.params['action'] == LIFECYCLE_ACTIONS.TEARDOWN.value or ctx.params['action'] == LIFECYCLE_ACTIONS.RELEASE.value):
            msg = 'Required if action = [teardown | release]'
            raise click.MissingParameter(ctx=ctx, param=self, message=msg)
        return value

class EnsureSaveState(click.Option):

    def full_process_value(self, ctx, value):
        value = super(EnsureSaveState, self).full_process_value(ctx, value)

        if value is None and (ctx.params['save_state'] == 'remote' or ctx.params['save_state'] == 'all'):
            msg = 'Required if save_state = [remote | all]'
            raise click.MissingParameter(ctx=ctx, param=self, message=msg)
        return value