class Result:
  def __init__(self, report, stdout, stderr, exit_code):
    self.report = report
    self.stdout = stdout
    self.stderr = stderr
    self.exit_code = exit_code

class Report:
  def __init__(self, errors, failures, name, skipped, tests, time):
    # This is all in string
    self.errors = errors
    self.failure = failures
    self.name = name
    self.skipped = skipped
    self.tests = tests
    self.time = time
    self.testcases = []
  
class TestCase:
  def __init__(self, name, time, meta, failure, error):
    self.name = name
    self.time = time
    self.meta = meta
    self.failure = failure
    self.error = error

class Meta:
  def __init__(self, expected, expression, hint, output):
    self.expected = expected
    self.expression = expression
    self.hint = hint
    self.output = output

class Failure:
  def __init__(self, message, failure_type):
    self.message = message
    self.failure_type = failure_type

class Error:
  def __init__(self, message, error_type):
    self.message = message
    self.error_type = error_type
