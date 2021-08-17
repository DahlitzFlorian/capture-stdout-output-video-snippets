import contextlib
import io

output_stream = io.StringIO()

with contextlib.redirect_stdout(output_stream):
    help(pow)

output_value = output_stream.getvalue()
print(output_value)
