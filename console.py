import module


def run():
    print('Extract words from lyrics\n')
    path = input('Enter the file path: ')
    content = module.load_txt(path)
    words = module.extract_words(content)
    words_listed = module.itemize(words)
    print()
    print('Extracted words')
    print(words_listed)


if __name__ == '__main__':
    run()
