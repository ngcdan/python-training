# How the input() function work
# The input() function pauses your program and waits for the user to enter something.

mgs = input("Tell me something, and I will repeat it back to you!\n")
print(mgs)


print("\n---------------Build prompt over several lines -----------------")

prompt = "If you tell us who you are, we can personalize the messages you see."
prompt += "\nWhat is your first name? "
name = input(prompt)
print(f"\nHello, {name}!")


