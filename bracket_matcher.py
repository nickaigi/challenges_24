def main(s: str) -> int:
    seen = []
    for char in s:
        if char == "(":
            seen.append(char)
        elif char in ")":
            if not seen:
                return 0
            seen.pop()

    return 1 if len(seen) == 0 else 0


if __name__ == "__main__":
    s = "(coder)(byte))"
    assert main(s) == 0
    s = "(c(oder))b(yte)"
    assert main(s) == 1
