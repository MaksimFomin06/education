del_symbols = ["-", "(", ")", "+"]


def phone_cleaner(phone: str) -> str:
    clean_phone = "".join(symbol for symbol in phone if symbol not in del_symbols)
    length = len(clean_phone)

    if length == 7:
        return "7495"+clean_phone
    else:
        return clean_phone.replace("8", "7")


new_phone = input()
old1 = input()
old2 = input()
old3 = input() 

new_phone_clean = phone_cleaner(new_phone)

phone_book = [old1, old2, old3]

for phone in phone_book:
    if phone_cleaner(phone) != new_phone_clean:
        print("NO")
    else:
        print("YES")