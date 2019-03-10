from flask import Flask, request, jsonify
from flask_cors import CORS, cross_origin
from question_evaluator import QuestionEvaluator

app = Flask(__name__)
cors = CORS(app)
app.config['CORS_HEADERS'] = 'Content-Type'

@app.route("/")
def root():
  return "yo"

def convert_testcase_to_dict(x):
  return {
    "name": x.name,
    "correct": x.meta.expected == x.meta.output
  }

@app.route("/two_sum/", methods=["GET", "POST"])
@cross_origin()
def two_sum():
  if request.method == "GET":
    return jsonify({
      "title": "Two Sum",
      "description": """
      Given an array of integers, return indices of the two numbers such that they add up to a specific target.

      You may assume that each input would have exactly one solution, and you may not use the same element twice.
      """,
      "testcases": [
        { "name": "test_public_01", "expression": "two_sum([2, 7, 11, 15], 9)", "expected": "[0, 1]" },
        { "name": "test_public_02", "expression": "two_sum([2, 7, 11, 15], 100)", "expected": "-1" }
      ]
    })
  else:
    code = request.json["code"]
    evaluator = QuestionEvaluator()
    result = evaluator.evaluate(code, "questions/two_sum")
    report = result.report
    testcases = report.testcases if report is not None else []
    response = {
      "testcases": list(map(lambda x: convert_testcase_to_dict(x), testcases))
    }
    return jsonify(response)

@app.route("/fib/", methods=["GET", "POST"])
@cross_origin()
def fib():
  if request.method == "GET":
    return jsonify({
      "title": "N-th Fibonacci",
      "description": """
      Return the N-th fibonacci number.
      """,
      "testcases": [
        { "name": "test_public_01", "expression": "fib(0)", "expected": "0" },
        { "name": "test_public_02", "expression": "fib(1)", "expected": "1" },
        { "name": "test_public_03", "expression": "fib(8)", "expected": "21" }
      ]
    })
  else:
    code = request.json["code"]
    evaluator = QuestionEvaluator()
    result = evaluator.evaluate(code, "questions/fib")
    report = result.report
    testcases = report.testcases if report is not None else []
    response = {
      "testcases": list(map(lambda x: convert_testcase_to_dict(x), testcases))
    }
    return jsonify(response)

@app.route("/squares_of_sorted_array/", methods=["GET", "POST"])
@cross_origin()
def squares_of_sorted_array():
  if request.method == "GET":
    return jsonify({
      "title": "Squares of a Sorted Array",
      "description": """
      Given an array of integers A sorted in non-decreasing order, return an array of the squares of each number, also in sorted non-decreasing order.
      """,
      "testcases": [
        { "name": "test_public_01", "expression": "sorted_squares([-4,-1,0,3,10])", "expected": "[0,1,9,16,100]" },
        { "name": "test_public_02", "expression": "sorted_squares([-7,-3,2,3,11])", "expected": "[4,9,9,49,121]" }
      ]
    })
  else:
    code = request.json["code"]
    evaluator = QuestionEvaluator()
    result = evaluator.evaluate(code, "questions/squares_of_sorted_array")
    report = result.report
    testcases = report.testcases if report is not None else []
    response = {
      "testcases": list(map(lambda x: convert_testcase_to_dict(x), testcases))
    }
    return jsonify(response)
