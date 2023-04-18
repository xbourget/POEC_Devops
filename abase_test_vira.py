import unittest


def moyenne(liste):
    if not liste:
        return 0
    somme = 0
    count = 0
    for element in liste:
        try:
            somme += float(element)
            count += 1
        except ValueError:
            pass
    if count == 0:
        return 0
    else:
        return somme / count


def somme(liste):
    if not liste:
        return 0
    total = 0
    for element in liste:
        try:
            total += float(element)
        except ValueError:
            pass
    return total


class TestStat(unittest.TestCase):
    def test_somme(self):
        self.assertEqual(somme([]), 0)
        self.assertEqual(somme([5, 10, 20]), 35)
        self.assertEqual(somme([5, "10", 20]), 35)

    def test_moyenne(self):
        self.assertEqual(moyenne([]), 0)
        self.assertEqual(moyenne([5, 10, 15]), 10)


if __name__ == '__main__':
    unittest.main()
