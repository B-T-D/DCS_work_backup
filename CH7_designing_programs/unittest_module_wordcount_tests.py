import unittest
from c3_wordcount_tests_version import count, get_word_counts

class TestWordcount(unittest.TestCase):

    quote = 'Diligence is the mother of good luck.'

    text = "Call me Ishmael. Some years ago—never mind how long precisely—having \
little or no money in my purse, and nothing particular \
to interest me on shore, I thought I would sail about a little and see \
the watery part of the world. It is a way I have of driving off the \
spleen and regulating the circulation."

    def test_count_common_cases(self):
        """Test common cases for the count() function."""
        self.assertEqual(count(self.quote, 'the'), 2)

    def test_get_word_counts_common_cases(self):
        """Test common cases for the get_word_counts() function."""

##        self.assertEqual(get_word_counts(text, 'the', 20), 4 / 15)
        self.assertEqual(get_word_counts(self.text, 'spleen', 20), 1 / 15)
        self.assertEqual(get_word_counts(self.text, 'I', 20), 5 / 15)

    def test_get_word_counts_boundary_cases(self):
        """Test boundary cases for get_word_counts() function."""

        # Window length is on boundary of requirement that it be a positive int:
        self.assertEqual(get_word_counts(self.text, 'spleen', 1), 0)
        # Text same size as window length (requirement is len(text) >= window length_
        self.assertEqual(get_word_counts(self.text, 'I', 301), 5 / 1)

    def test_get_word_counts_corner_cases(self):
        """Test corner cases for get_word_counts() function."""

        # What if text and word are the same?
        self.assertEqual(get_word_counts('a', 'a', 1), 1)

if __name__ == '__main__':
    unittest.main()
        
        
