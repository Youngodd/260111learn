"""Simple program to calculate sum of numbers separated by '+' in input."""


def parse_numbers(expression: str) -> list[float]:
    parts = [part.strip() for part in expression.split("+") if part.strip()]
    if not parts:
        raise ValueError("未检测到有效的数字")
    numbers = []
    for part in parts:
        numbers.append(float(part))
    return numbers


def main() -> None:
    expression = input("请输入用加号连接的数值（如 1+2+3）：").strip()
    numbers = parse_numbers(expression)
    total = sum(numbers)
    if total.is_integer():
        print(f"结果：{int(total)}")
    else:
        print(f"结果：{total}")


if __name__ == "__main__":
    main()
