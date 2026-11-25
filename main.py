"""Museum of the Year 3000 - museum label for a CAPTCHA, c. 2024."""

LABEL = "CAPTCHA, c. 2024. To prove they were human, citizens identified traffic lights nine times a day. Machines passed in four seconds."


def main():
    import os

    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(LABEL)


assert 1 <= len(LABEL) <= 200, "label must be 1-200 characters"
assert LABEL.strip() == LABEL
assert "\n" not in LABEL


if __name__ == "__main__":
    main()
