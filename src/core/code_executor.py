import io
import contextlib

def run_python_code(code: str):
    stdout_capture = io.StringIO()
    with contextlib.redirect_stdout(stdout_capture):
        try:
            local_vars = {}
            exec(code, {}, local_vars)
            output = stdout_capture.getvalue()
        except Exception as e:
            output = f"An error occurred:\n{e}"
    return output