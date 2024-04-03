import unittest
from is_palindrome import is_palindrome

def obtener_cantidad_de_palabras_palindrome(palabras):
    cont_pal = 0
    for palabra in palabras:
        palabra = palabra.replace(" ", "")
        palabra = palabra.replace(":", "")
        palabra = palabra.replace("-", "")
        palabra = palabra.replace(",", "")
        palabra = palabra.lower()

        if is_palindrome(palabra) is True:
            cont_pal = cont_pal + 1
    return cont_pal



class TestCantidadDePalabrasPalindromes(unittest.TestCase):
    def test_cantidad_de_palabras_palindromes_simple(self):
        palabras = ["ala"]
        resultado = obtener_cantidad_de_palabras_palindrome(palabras)
        self.assertEqual(resultado, 1)

    def test_cantidad_de_palabras_palindromes_con_2(self):
        palabras = ["ala", "neuquen"]
        resultado = obtener_cantidad_de_palabras_palindrome(palabras)
        self.assertEqual(resultado, 2)

    def test_cantidad_de_palabras_palindromes_con_3(self):
        palabras = ["ala", "neuquen", "hola"]
        resultado = obtener_cantidad_de_palabras_palindrome(palabras)
        self.assertEqual(resultado, 2)

    def test_cantidad_de_palabras_palindromes_con_4(self):
        palabras = ["ala", "neuquen", "hola", "programacion"]
        resultado = obtener_cantidad_de_palabras_palindrome(palabras)
        self.assertEqual(resultado, 2)

    def test_cantidad_de_palabras_palindromes_con_5(self):
        palabras = ["ala", "neuquen", "hola", "programacion", "palap"]
        resultado = obtener_cantidad_de_palabras_palindrome(palabras)
        self.assertEqual(resultado, 3)

    def test_cantidad_de_palabras_palindromes_complejo(self):
        palabras = ["ala", "neuquen", "hola", "programacion", "palap", "neu  quen"]
        resultado = obtener_cantidad_de_palabras_palindrome(palabras)
        self.assertEqual(resultado, 4)

    def test_cantidad_de_palabras_palindromes_complejo_2(self):
        palabras = [
            "ala",
            "neuquen",
            "hola",
            "programacion",
            "palap",
            "neu  quen",
            "agita falsos usos la fatiga",
            "presidente de la camara de diputados: martin menem",
            "A man, a plan, a canal - Panama"
        ]
        resultado = obtener_cantidad_de_palabras_palindrome(palabras)
        self.assertEqual(resultado, 6)


unittest.main()