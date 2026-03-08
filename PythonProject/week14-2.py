import sys
import json
import ast


class LibrarySystem:
    def __init__(self, capacity: int):
        self.capacity = capacity
        self.books = []  # 目前館藏(可借)書名清單，可允許重複書名

    def addBook(self, title: str) -> bool:
        # 若仍有空位 -> 加入書籍，回傳 True；若滿了 -> 回傳 False
        if len(self.books) < self.capacity:
            self.books.append(title)
            return True
        return False

    def borrowBook(self, title: str) -> bool:
        # 若書存在 -> 借出並從館藏移除，回傳 True；不存在 -> 回傳 False
        try:
            self.books.remove(title)  # 移除第一本符合的書
            return True
        except ValueError:
            return False

    def returnBook(self, title: str) -> bool:
        # 若仍有空位 -> 歸還(加回)書籍，回傳 True；若沒有空位 -> 回傳 False
        if len(self.books) < self.capacity:
            self.books.append(title)
            return True
        return False


def _extract_two_arrays(text: str):
    """從整段輸入中抓出前兩個 [ ... ] 區塊，支援中間夾雜 ===input=== 之類文字。"""
    arrays = []
    i = 0
    n = len(text)

    while i < n and len(arrays) < 2:
        if text[i] == "[":
            depth = 0
            j = i
            while j < n:
                if text[j] == "[":
                    depth += 1
                elif text[j] == "]":
                    depth -= 1
                    if depth == 0:
                        arrays.append(text[i : j + 1].strip())
                        i = j
                        break
                j += 1
        i += 1

    if len(arrays) < 2:
        raise ValueError("Input must contain two array blocks like: [..]\\n[..]")

    def load(s: str):
        try:
            return json.loads(s)        # JSON 風格
        except Exception:
            return ast.literal_eval(s)  # Python list 風格

    return load(arrays[0]), load(arrays[1])


def main():
    data = sys.stdin.read()
    if not data.strip():
        return

    ops, args = _extract_two_arrays(data)

    lib = None
    output = []

    for k in range(len(ops)):
        op = ops[k]
        arg = args[k]

        if op == "LibrarySystem":
            lib = LibrarySystem(arg[0])
            output.append(None)
        elif op == "addBook":
            output.append(lib.addBook(arg[0]))
        elif op == "borrowBook":
            output.append(lib.borrowBook(arg[0]))
        elif op == "returnBook":
            output.append(lib.returnBook(arg[0]))
        else:
            raise ValueError(f"Unknown operation: {op}")

    print(output)


if __name__ == "__main__":
    main()
