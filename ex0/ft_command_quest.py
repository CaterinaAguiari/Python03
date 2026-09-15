import sys
print("=== Command Quest ===")
print(f"Program name: {sys.argv[0]}")
if len(sys.argv) == 1:
    print("No arguments provided!")
else:
    total_arg: int = len(sys.argv) - 1
    print(f"Arguments received: {total_arg}")
    count: int = total_arg
    i: int = 1
    while count > 0:
        print(f"Argument {i}: {sys.argv[i]}")
        i = i + 1
        count = count - 1
total_args: int = len(sys.argv)
print(f"Total arguments: {total_args}")
