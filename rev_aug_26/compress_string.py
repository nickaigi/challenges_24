def compress_string(s: str) -> str:
    if not s:
        return ""

    res = []
    count = 1
    for i in range(1, len(s)):
        if s[i] == s[i - 1]:
            count += 1
        else:
            res.append(f"{s[i - 1]}{count}")
            count = 1
    res.append(f"{s[-1]}{count}")
    return "".join(res)


if __name__ == "__main__":
    assert compress_string("AAAABBBBCCCCCDDEEEE") == "A4B4C5D2E4"
    assert compress_string("AAB") == "A2B1"
    assert compress_string("AAAaaa") == "A3a3"
    assert compress_string("") == ""
    print("All Tests Passed")
