
def print_countdown(n):
    print(n)
    if n > 0:
        print_countdown(n-1)

if __name__ == "__main__":
    print_countdown(3)
