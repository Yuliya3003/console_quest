from existences import Hero


def game():
    with open('ASCIIs/logo.txt') as logo:
        print(logo.read())

    hero = Hero()


if __name__ == "__main__":
    game()
