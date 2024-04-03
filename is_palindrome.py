import unittest
def is_palindrome(word):
    for letra in range(len(word)):
        pal1 = word[letra]
        letra = - (letra +1)
        pal2 = word[letra]
        if pal1 == pal2:
            return True
        else:
            return False





class TestIsPalindrome(unittest.TestCase):
    def test_with_a(self):
        input = 'a'
        result = is_palindrome(input)
        self.assertTrue(result)

    def test_with_ala(self):
        input = 'ala'
        result = is_palindrome(input)
        self.assertTrue(result)

    def test_with_neuquen(self):
        input = 'neuquen'
        result = is_palindrome(input)
        self.assertTrue(result)

    def test_with_hola(self):
        input = 'hola'
        result = is_palindrome(input)
        self.assertFalse(result)

    def test_with_alaala(self):
        input = 'ala ala ala'
        result = is_palindrome(input)
        self.assertTrue(result)

if __name__ == "__main__":
    unittest.main()