def after_scenario(context, _):
    if context.failed and context.process.stderr != "":
        print("Printing stderr:")
        print(context.process.stderr)
