import os


def filename_from_path(path:str):
    return os.path.split(path)[-1]


def load_txt(filename: str):
    content = 'ERROR: Only .txt files allowed'

    if filename.endswith('.txt'):
        fp = os.path.join(os.path.dirname(__file__), filename)

        with open(fp, 'r', encoding='utf-8') as f:
            content = f.read()

    return content


def extract_words(lyrics: str):
    # remove song sections label such as [Intro]
    song_sections = re.findall(r'\[\w+.+', lyrics)
    
    for section in song_sections:
        lyrics = lyrics.replace(section, '')

    # remove the word case difference by making everything lower case
    lyrics = lyrics.lower()

    # remove extra symbols
    symbols = ['(', ')', ',', '.', '?', ':', '-']

    for symbol in symbols:
        lyrics = lyrics.replace(symbol, ' ')

    # remove line breaks
    if '\n' in lyrics:
        lyrics = lyrics.replace('\n', ' ')

    # break the lyrics into list containing the words
    words = lyrics.split(' ')

    # remove trailing spaces
    words = [word.strip() for word in words]

    # remove duplicates
    words = set(words)
    words = list(words)

    # remove empty string from list
    for index, word in enumerate(words):
        if word == '':
            words.pop(index)

    # capitalize words
    words = [word.capitalize() for word in words]

    return words


# quick testing
if __name__ == '__main__':
    sample = load_txt('sample_lyrics.txt')
    words = extract_words(sample)
    print(words)
