import unittest

def toUpper(str):
    new_str = ""
    for chr in str:
        new_str.append(chr.upper())

    return str

class MyTest(unittest.TestCase):

    def testToUpper(self):
        self.assertEqual(toUpper('Hello world'), 'HELLO WORLD')

if __name__ == '__main__':
    unittest.main()
