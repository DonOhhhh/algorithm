import os
import unittest


class myTest(unittest.TestCase):
    def test_1(self):
        with os.popen("type inputs\\1 | python 18111.py") as f:
            result = f.read()
        with os.popen("type inputs\\1.a") as f:
            answer = f.read()
        self.assertEqual(answer, result)

    def test_2(self):
        with os.popen("type inputs\\2 | python 18111.py") as f:
            result = f.read()
        with os.popen("type inputs\\2.a") as f:
            answer = f.read()
        self.assertEqual(answer, result)

    def test_3(self):
        with os.popen("type inputs\\3 | python 18111.py") as f:
            result = f.read()
        with os.popen("type inputs\\3.a") as f:
            answer = f.read()
        self.assertEqual(answer, result)

    def test_4(self):
        with os.popen("type inputs\\4 | python 18111.py") as f:
            result = f.read()
        with os.popen("type inputs\\4.a") as f:
            answer = f.read()
        self.assertEqual(answer, result)

    def test_5(self):
        with os.popen("type inputs\\5 | python 18111.py") as f:
            result = f.read()
        with os.popen("type inputs\\5.a") as f:
            answer = f.read()
        self.assertEqual(answer, result)

    def test_6(self):
        with os.popen("type inputs\\6 | python 18111.py") as f:
            result = f.read()
        with os.popen("type inputs\\6.a") as f:
            answer = f.read()
        self.assertEqual(answer, result)

    def test_7(self):
        with os.popen("type inputs\\7 | python 18111.py") as f:
            result = f.read()
        with os.popen("type inputs\\7.a") as f:
            answer = f.read()
        self.assertEqual(answer, result)

    def test_8(self):
        with os.popen("type inputs\\8 | python 18111.py") as f:
            result = f.read()
        with os.popen("type inputs\\8.a") as f:
            answer = f.read()
        self.assertEqual(answer, result)

    def test_9(self):
        with os.popen("type inputs\\9 | python 18111.py") as f:
            result = f.read()
        with os.popen("type inputs\\9.a") as f:
            answer = f.read()
        self.assertEqual(answer, result)

    def test_10(self):
        with os.popen("type inputs\\10 | python 18111.py") as f:
            result = f.read()
        with os.popen("type inputs\\10.a") as f:
            answer = f.read()
        self.assertEqual(answer, result)


if __name__ == "__main__":
    unittest.main()
