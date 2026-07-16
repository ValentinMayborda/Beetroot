import unittest
import phonebook as pb
from unittest.mock import patch


class TestPhonebook(unittest.TestCase):

    def setUp(self):
        self.phonebook = {"contacts": []}

    # Перевірка додавання контакту
    @patch("builtins.input", side_effect=["1234567890", "Valentyn", "Maiboroda", "Chernihiv", "UA"])
    def test_add_entry(self, mock_input):
        result = pb.add_entry(self.phonebook)

        # Перевірка чи додався контакт
        self.assertEqual(len(result["contacts"]), 1)
        self.assertEqual(result["contacts"][0]["first_name"], "Valentyn")
        self.assertEqual(result["contacts"][0]["phone_number"], "1234567890")


    # Перевірка на дублікати
    # @patch("builtins.input", side_effect=["1234567890", "Valentyn", "Maiboroda", "Chernihiv", "UA"])
    # def test_duplicate_phone(self, mock_input):
    #     pb.add_entry(self.phonebook)
    #
    #     #mock_input.side_effect = ["1234567890", "Valentyn", "Maiboroda", "Chernihiv", "UA"]
    #     #pb.add_entry(self.phonebook)
    #
    #     self.assertEqual(len(self.phonebook["contacts"]), 1)


if __name__ == "__main__":
    unittest.main()






