def parse_numbers(expression: str) -> list[float]:
    parts = [part.strip() for part in expression.split("+") if part.strip()]
    if not parts:
        raise ValueError("未检测到有效的数字")

    numbers = []
    for part in parts:
        numbers.append(float(part))
    return numbers

