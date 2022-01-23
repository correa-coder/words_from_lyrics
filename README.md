# Introduction

With the goal of learning some vocabulary words in **Spanish**, I decided to create an app that extracts the words from a ``.txt`` file containing the lyrics of a song, it should work with **any** language, not just Spanish.

# Usage

There are two ways to use this software, with a console interface by running the ``console.py`` file or with a GUI by running the ``main.py``.

> Note: Python 3.7 or higher is required

In the project folder there's a `sample_lyrics.txt` file that contains the lyrics of the song **A Tu Lado** by **RBD** which can be found on [Genius](https://genius.com/Rbd-a-tu-lado-lyrics).

## Console
Run the ``console.py`` file, enter the absolute path for the ``.txt`` file containing the lyrics and press enter.

### Example:
```
Enter the file path: C:/users/username/desktop/lyrics.txt

Extracted words
- Hello
- World
- Foo
- Bar
```

## GUI
Click on the ``Open lyrics file`` button and choose the ``.txt`` file containing the lyrics.

# Settings
Customization can be done by editing the ``settings.json`` file, the following items can be customized:

- Which symbols to be ignored while extracting the words
- Which words to be ignored, e.g filler words such as ooh, ah, yeah, ...
- Font name and size used in GUI
- Colors used in GUI
