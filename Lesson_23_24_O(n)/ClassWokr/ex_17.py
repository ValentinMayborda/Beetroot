stack = [
    (1, '('),
    (2, '{'),
]
opens = "([{<"
closes = ")]}>"
symbol = '}'
position = closes.index(symbol)
print(position)
if stack and opens[position] == stack[-1][1]:
    print("Match found")
# (1 + 3* {4 + 5})

print(stack[-1][1])
