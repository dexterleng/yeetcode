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
      """
    })
  else:
    code = request.json["code"]
    evaluator = QuestionEvaluator()
    result = evaluator.evaluate(code)
    report = result.report
    testcases = report.testcases if report is not None else []
    response = {
      "testcases": list(map(lambda x: convert_testcase_to_dict(x), testcases))
    }
    return jsonify(response)
