"""Word Finder: finds random words from a dictionary."""
import random

class WordFinder:
    """Word Finder: finds random words from a dictionary."""
    def __init__(self, file_path):
        """Initializes Word Finder with the Words from the Given File"""
        file_words = open(file_path)
        self.words = self.parse(file_path)

    def parse(self, file):
        """Parses the Given File for the List of Words"""
        return [word.strip() for word in file]

    def random(self):
        """Returns a Random Word from the File"""
        return random.choice(self.words)

class SpecialWordFinder(WordFinder):
    def parse(self, file):
        return [word.strip() for word in file if word.strip() and not word.startwith("#")]