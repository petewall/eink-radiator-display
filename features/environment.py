"""Register behave hooks"""

def after_scenario(context, _):
    """Prints stderr if the subprocess fails"""
    if context.failed and context.process.stderr != '':
        print('Printing stderr:')
        print(context.process.stderr)
