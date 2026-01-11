from flask import Flask, render_template, request

from src.expression import evaluate_expression, ParseError
from src.calculator import calculate_sum

app = Flask(__name__)


@app.route("/", methods=["GET", "POST"])
def index():
    expression = ""
    result = None
    error = None

    if request.method == "POST":
        expression = (request.form.get("expression") or "").strip()
        try:
           total = evaluate_expression(expression)
            result = int(total) if total.is_integer() else total
        except ParseError as e:
            error = str(e)
        except Exception as e:
            error = f"发生未预期错误：{repr(e)}"

    return render_template("index.html", expression=expression, result=result, error=error)


if __name__ == "__main__":
    app.run(debug=True)
