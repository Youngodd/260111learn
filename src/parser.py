class ParseError(ValueError):
    """输入表达式格式错误（给用户看的错误）"""


def parse_numbers(expression: str) -> list[float]:
    expr = expression.strip()
    if not expr:
        raise ParseError("请输入表达式，例如：1+2+3")

    if expr.startswith("+") or expr.endswith("+"):
        raise ParseError("表达式不能以 + 开头或结尾，例如：1+2+3")

    raw_parts = expr.split("+")

    # 处理 1++2 这种情况：split 后会出现空字符串
    if any(part.strip() == "" for part in raw_parts):
        raise ParseError("表达式格式不正确：出现连续的 + 或空项，例如：1+2+3")

    numbers: list[float] = []
    for part in raw_parts:
        token = part.strip()
        try:
            numbers.append(float(token))
        except ValueError:
            raise ParseError(f"不是有效数字：{token}")

    return numbers
