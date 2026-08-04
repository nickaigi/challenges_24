import re


def longest_word_two(sen: str) -> str:
    res = ""
    for char in sen:
        if char.isalnum():
            res += char
        else:
            res += " "
    return max(res.split(), key=len)


def longest_word(sen: str) -> str:
    cleaned = re.sub(r"[^\w]", " ", sen)
    words = cleaned.split()

    return max(words, key=len) if words else ""


if __name__ == "__main__":
    sen = "fun&!! time"
    assert longest_word(sen) == "time"
    assert longest_word_two(sen) == "time"
    sen = "I love dogs"
    assert longest_word(sen) == "love"
    assert longest_word_two(sen) == "love"
