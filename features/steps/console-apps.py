import subprocess
import os

from behave import *


@given("a command line argument of '{argument}'")
def step_impl(context, argument):
    if not hasattr(context, 'cmd_args'):
        context.cmd_args = []

    context.cmd_args.append(argument)


@when("the {app_name} application is run")
def step_impl(context, app_name):
    app_path = os.path.join("bin", app_name)

    # Build up the args to pass to the app.
    args = [app_path]
    if hasattr(context, 'cmd_args'):
        args.extend(context.cmd_args)

    context.app_run_result = subprocess.run(args, capture_output=True, encoding='UTF-8')


@then('"{text}" is displayed')
def step_impl(context, text: str):
    assert text in context.app_run_result.stdout, f"'{text}' not found in '{context.app_run_result.stdout}'"
