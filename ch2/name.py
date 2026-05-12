name = "ada lovelace"
print(name.title())
print(name.lower())
print(name.upper())

first_name = "ada"
last_name = "lovelace"
full_name = f"{first_name} {last_name}"
print(f"Hello, {full_name.title()}")

full_name_old = "old method name: {} {}".format(first_name, last_name)
print(full_name_old)

print("List:\n\t-meat\n\t-sugar\n\t-apple\n\t-tomato")

word = " Bye my    "
print(f"{word} Bro")
print(f"{word.rstrip()} Bro")
print(f"{word} Bro")
word = word.rstrip()
print(f"{word} Bro")
word = word.lstrip()
print(f"{word} Bro")
word = "    Bye my    "
print(f"{word} Bro")
word = word.strip()
print(f"{word} Bro")