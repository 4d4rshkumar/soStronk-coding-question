import unittest
import soStronk
'''=======================================test cases==================================================================='''
class test_calc(unittest.TestCase):
    def test_case0(self):
        result = soStronk.subset(2,[['bleh', '85'], ['aequitas', '90'], ['aks', '87'], ['lamiV', '20']],4)
        self.assertEqual(result,{'aks,lamiV': 53.5, 'aequitas,lamiV': 55.0, 'aequitas,aks': 88.5, 'bleh,lamiV': 52.5, 'bleh,aks': 86.0, 'bleh,aequitas': 87.5})


    def test_case1(self):
        result = soStronk.subset(3,[['goal', '21'], ['lol', '345'], ['soo', '987'], ['good', '345'], ['knight', '45'], ['hunter', '678']],6)
        self.assertEqual(result,{'good,knight,hunter': 356.0, 'soo,knight,hunter': 570.0, 'soo,good,hunter': 670.0, 'soo,good,knight': 459.0, 'lol,knight,hunter': 356.0, 'lol,good,hunter': 456.0, 'lol,good,knight': 245.0, 'lol,soo,hunter': 670.0, 'lol,soo,knight': 459.0, 'lol,soo,good': 559.0, 'goal,knight,hunter': 248.0, 'goal,good,hunter': 348.0, 'goal,good,knight': 137.0, 'goal,soo,hunter': 562.0, 'goal,soo,knight': 351.0, 'goal,soo,good': 451.0, 'goal,lol,hunter': 348.0, 'goal,lol,knight': 137.0, 'goal,lol,good': 237.0, 'goal,lol,soo': 451.0})


    def test_case2(self):
        result = soStronk.subset(1,[['asd', '123'], ['bff', '234'], ['cnd', '345'], ['gost', '456']],4)
        self.assertEqual(result,{'gost': 456.0, 'cnd': 345.0, 'bff': 234.0, 'asd': 123.0})


if __name__ =="__main__":
    unittest.main()
