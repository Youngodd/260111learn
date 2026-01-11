from src.expression import evaluate_expression, ParseError
from calculator import calculate_sum


def main() -> None:
    print("欢迎使用加法计算器")
    print("输入形如 1+2+3 的表达式。输入 q 退出。")

    while True:
        expression = input("\n请输入：").strip()
        if expression.lower() in {"q", "quit", "exit"}:
            print("已退出。")
            return

        try:
            total = evaluate_expression(expression)

            if total.is_integer():
                print(f"结果：{int(total)}")
            else:
                print(f"结果：{total}")
        except ParseError as e:
            # 给用户看的错误（友好、可理解）
            print(f"输入有误：{e}")
        except Exception as e:
            # 兜底：出现你没想到的错误，也别让程序直接炸
            print("发生了未预期的错误，请把下面信息复制给我：")
            print(repr(e))


if __name__ == "__main__":
    main()
