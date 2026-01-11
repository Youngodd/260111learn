from parser import parse_numbers
from calculator import calculate_sum


def main() -> None:
    expression = input("请输入用加号连接的数值（如 1+2+3）：").strip()

    numbers = parse_numbers(expression)
    total = calculate_sum(numbers)

    if total.is_integer():
        print(f"结果：{int(total)}")
    else:
        print(f"结果：{total}")


if __name__ == "__main__":
    main()

