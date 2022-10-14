def after_scenario(context, scenario):
    if context.failed and context.process.stderr != "":
        print("Printing stderr:")
        print(context.process.stderr)
