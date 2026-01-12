from flask import Flask, render_template, request, session

from src.expression import evaluate_expression, ParseError
from src.calculator import calculate_sum

app = Flask(__name__)
app.secret_key = "dev-secret-key-change-later"

from datetime import datetime

@app.route("/", methods=["GET", "POST"])
def index():
    expression = ""
    result = None
    error = None

    # 读取历史（没有就创建空列表）
    history = session.get("history", [])

    if request.method == "POST":
        expression = (request.form.get("expression") or "").strip()
        ts = datetime.now().strftime("%H:%M:%S")

        try:
            total = evaluate_expression(expression)
            result = int(total) if total.is_integer() else total

            # 记录成功历史
            history.insert(0, {
                "ts": ts,
                "expression": expression,
                "ok": True,
                "result": str(result),
            })
        except ParseError as e:
            error = str(e)

            # 记录失败历史
            history.insert(0, {
                "ts": ts,
                "expression": expression,
                "ok": False,
                "error": error,
            })
        except Exception as e:
            error = f"发生未预期错误：{repr(e)}"
            history.insert(0, {
                "ts": ts,
                "expression": expression,
                "ok": False,
                "error": error,
            })

        # 只保留最近 10 条
        history = history[:10]
        session["history"] = history

    return render_template(
        "index.html",
        expression=expression,
        result=result,
        error=error,
        history=history,
    )



if __name__ == "__main__":
    app.run(debug=True)
