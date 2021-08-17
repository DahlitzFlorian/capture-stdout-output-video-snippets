import contextlib

with open("help_output.txt", "w") as f:
    with contextlib.redirect_stdout(f):
        help(pow)
