# Assignment One
# Task 1: Simple Calculator
# Task 2: QA Bot


# =========================
# Task 1 - Simple Calculator
# =========================

print("=== Simple Calculator ===")

first_number = float(input("Enter first number: "))
second_number = float(input("Enter second number: "))
operator = input("Choose operator (+, -, *, /): ")

if operator == "+":
    result = first_number + second_number
elif operator == "-":
    result = first_number - second_number
elif operator == "*":
    result = first_number * second_number
elif operator == "/":
    if second_number == 0:
        print("Error: Cannot divide by zero.")
        result = None
    else:
        result = first_number / second_number
else:
    print("Error: Invalid operator.")
    result = None

if result is not None:
    print("Result:", first_number, operator, second_number, "=", result)


# =========================
# Task 2 - QA Bot
# =========================

print("\n=== QA Bot ===")
print("Ask me something! Type 'quit' to exit.")

question = input("You: ").lower()

if "quit" in question:
    print("Bot: Goodbye!")

elif "hello" in question:
    print("Bot: Hello! Nice to meet you.")

elif "python" in question:
    print("Bot: Python is a popular programming language.")

elif "jetson" in question:
    print("Bot: Jetson is a platform for AI and edge computing.")

elif "ai" in question:
    print("Bot: AI stands for Artificial Intelligence.")

elif "name" in question:
    print("Bot: My name is QA Bot.")

else:
    print("Bot: Sorry, I don't understand your question.")
12