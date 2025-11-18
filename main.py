from mainsearch import search


def main():
    url = "https://en.wikipedia.org/wiki/6-7_(meme)"
    soup = search(url)
    soup.start()


if __name__ == "__main__":
    main()
