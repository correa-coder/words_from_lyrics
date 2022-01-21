import module


def run():
    print('Extract words from lyrics\n')
    path = input('Enter the file path: ')
    content = module.load_txt(path)
    words = module.extract_words(content)
    print()
    print('Extracted words')

    for word in words:
        print(f'- {word}')


if __name__ == '__main__':
    run()
