import docker
import os
import time
import tempfile
import tarfile
import xml.etree.ElementTree as ET
from io import BytesIO
from result import Result, Report, TestCase, Meta, Failure, Error

# Taken from: https://github.com/docker/docker-py/blob/master/tests/helpers.py
def untar_file(tardata, filename):
  with tarfile.open(mode='r', fileobj=tardata) as t:
      f = t.extractfile(filename)
      result = f.read()
      f.close()
  return result

class QuestionEvaluator:
  def __init__(self):
    self.client = docker.from_env()
  
  # hardcoded for Python3.7
  def evaluate(self, solution, question):
    container = None
    try:
      container = self.client.containers.create(image="coursemology/evaluator-image-python:3.7")
      self.copy_question_to_container(container, question)
      self.copy_solution_to_container(container, solution)
      container.start()
      # wait for container to stop
      exit_code = container.wait()['StatusCode']
      stdout = container.logs(stdout=True, stderr=False)
      stderr = container.logs(stdout=False, stderr=True)
      report = self.extract_report(container)
      return Result(report, stdout, stderr, exit_code)
    except:
      raise
    finally:
      # Delete container regardless of error.
      if container is not None:
        container.remove()
  
  # question_path is relative
  # question should contain coursemology/package/ directory
  # TODO: Figure out how to create nested directories on the fly so the above need not be true.
  def copy_question_to_container(self, container, question_path):
    question_path = os.path.join(os.path.dirname(__file__), question_path)
    with docker.utils.tar(question_path) as question_tar:
      container.put_archive("/home/", question_tar)
    
  # overwrite submission/template.py
  # Taken from: https://gist.github.com/zbyte64/6800eae10ce082bb78f0b7a2cca5cbc2
  def copy_solution_to_container(self, container, solution):
    solution_tarstream = BytesIO()
    solution_tar = tarfile.TarFile(fileobj=solution_tarstream, mode='w')
    file_data = solution.encode('utf8')
    tarinfo = tarfile.TarInfo(name='template.py')
    tarinfo.size = len(file_data)
    tarinfo.mtime = time.time()
    solution_tar.addfile(tarinfo, BytesIO(file_data))
    solution_tar.close()
    solution_tarstream.seek(0)
    container.put_archive("/home/coursemology/package/submission/", solution_tarstream)

  def extract_file_from_container(self, container, filename):
    strm, stat = container.get_archive("/home/coursemology/package/" + filename)
    with tempfile.NamedTemporaryFile() as destination:
      for d in strm:
        destination.write(d)
      destination.seek(0)
      retrieved_data = untar_file(destination, filename)
      return retrieved_data
  
  def extract_report(self, container):
    try:
      report_content = self.extract_file_from_container(container, "report-public.xml")
      # Taken from: https://stackoverflow.com/a/18281386/10390454
      tree = ET.ElementTree(ET.fromstring(report_content))
      root = tree.getroot()
      test_suite = root[0]
      ts_attr = test_suite.attrib
      report = Report(ts_attr["errors"], ts_attr["failures"], ts_attr["name"], ts_attr["skipped"], ts_attr["tests"], ts_attr["time"])
      for test_case in test_suite.findall("testcase"):
        tc_attr = test_case.attrib
        tcm_attr = test_case.find("meta").attrib
        output = None
        if "output" in tcm_attr:
          output = tcm_attr["output"]
        meta = Meta(tcm_attr["expected"], tcm_attr["expression"], tcm_attr["hint"], output)
        tcf = test_case.find("failure")
        failure = None
        if tcf is not None:
          tcf_attr = tcf.attrib
          failure = Failure(tcf_attr["message"], tcf_attr["type"])
        tce = test_case.find("error")
        error = None
        if tce is not None:
          tce_attr = tce.attrib
          error = Error(tce_attr["message"], tce_attr["type"])
        test_case = TestCase(tc_attr["name"], tc_attr["time"], meta, failure, error)
        report.testcases.append(test_case)
      return report
    except docker.errors.NotFound:
      return None
    except:
      raise
    


# qe = QuestionEvaluator()
# #content = "def two_sum(numbers, target):\n  lookup = {}\n  for i in range(len(numbers)):\n    n = numbers[i]\n    if (target - n) in lookup:\n      return [lookup[target - n], i]\n    lookup[n] = i\n  return -1\n"
# # print(content)
# qe.evaluate("fsfdsffsdfdsafdsfsda")
