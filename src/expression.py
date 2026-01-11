import ast
import operator as op


class ParseError(ValueError):
    """输入表达式格式错误（给用户看的错误）"""


# 允许的运算符
_ALLOWED_BINOPS = {
    ast.Add: op.add,
    ast.Sub: op.sub,
    ast.Mult: op.mul,
    ast.Div: op.truediv,
}

_ALLOWED_UNARYOPS = {
    ast.UAdd: op.pos,
    ast.USub: op.neg,
}


def _eval_node(node: ast.AST) -> float:
    if isinstance(node, ast.Constant):  # Python 3.8+
        if isinstance(node.value, (int, float)):
            return float(node.value)
        raise ParseError("只允许输入数字和运算符")

    if isinstance(node, ast.Num):  # 兼容旧节点类型
        return float(node.n)

    if isinstance(node, ast.BinOp):
        left = _eval_node(node.left)
        right = _eval_node(node.right)

        op_type = type(node.op)
        if op_type not in _ALLOWED_BINOPS:
            raise ParseError("只支持 + - * / 和括号")

        # 处理除 0
        if op_type is ast.Div and right == 0:
            raise ParseError("除数不能为 0")

        return _ALLOWED_BINOPS[op_type](left, right)

    if isinstance(node, ast.UnaryOp):
        op_type = type(node.op)
        if op_type not in _ALLOWED_UNARYOPS:
            raise ParseError("不支持该一元运算")
        operand = _eval_node(node.operand)
        return _ALLOWED_UNARYOPS[op_type](operand)

    if isinstance(node, ast.Expression):
        return _eval_node(node.body)

    # 任何其他节点都拒绝
    raise ParseError("表达式包含不支持的内容")


def evaluate_expression(expression: str) -> float:
    expr = (expression or "").strip()
    if not expr:
        raise ParseError("请输入表达式，例如：1+2*3 或 (1+2)*3")

    # 可选：简单限制字符，提升错误友好度
    for ch in expr:
        if ch.isdigit() or ch in ".+-*/() ":
            continue
        raise ParseError(f"出现不支持的字符：{ch}")

    try:
        tree = ast.parse(expr, mode="eval")
    except SyntaxError:
        raise ParseError("表达式格式不正确，请检查运算符或括号")

    return _eval_node(tree)
