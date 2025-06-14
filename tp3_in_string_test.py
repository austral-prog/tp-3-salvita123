import io
import unittest.mock
import in_string as ex1  # Asegurate de que tu archivo se llame in_string.py

import unittest

class TP3InStringTestCases(unittest.TestCase):
    @unittest.mock.patch('sys.stdout', new_callable=io.StringIO)
    def test_check_vowels(self, mock_stdout):
        with unittest.mock.patch('builtins.input', return_value="Augusto"):
            ex1.check_vowels()
            results = mock_stdout.getvalue().splitlines()
            self.assertEqual(results[0], "Contiene a: True")
            self.assertEqual(results[1], "Contiene e: False")
            self.assertEqual(results[2], "Contiene i: False")
            self.assertEqual(results[3], "Contiene o: True")
            self.assertEqual(results[4], "Contiene u: True")

if __name__ == "__main__":
    unittest.main()
