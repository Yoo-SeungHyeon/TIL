import user

def main():
    alice = user.User('Alice', 'alice@example.com')
    bob = user.User('Bob', 'bob@example.com')
    alice.get_data()
    bob.get_data()


if __name__ == "__main__":
    main()

