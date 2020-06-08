import unittest
import soStronk
'''=======================================test cases==================================================================='''
class test_calc(unittest.TestCase):
    def test_case0(self):
        result = soStronk.subset(1,[['bleh', '85'], ['Aequitas', '90'], ['akS', '87'], ['lamiV', '20']],4)
        self.assertEqual(result,{20.0: 'lamiV', 87.0: 'akS', 90.0: 'Aequitas', 85.0: 'bleh'})


    def test_case1(self):
        result = soStronk.subset(2,[['bleh', '85'], ['Aequitas', '90'], ['akS', '87'], ['lamiV', '20']],4)
        self.assertEqual(result,{53.5: 'akS,lamiV', 55.0: 'Aequitas,lamiV', 88.5: 'Aequitas,akS', 52.5: 'bleh,lamiV', 86.0: 'bleh,akS', 87.5: 'bleh,Aequitas'})


    def test_case2(self):
        result = soStronk.subset(3,[['bleh', '85'], ['Aequitas', '90'], ['akS', '87'], ['lamiV', '20']],4)
        self.assertEqual(result,{65.67: 'Aequitas,akS,lamiV', 64.0: 'bleh,akS,lamiV', 65.0: 'bleh,Aequitas,lamiV', 87.33: 'bleh,Aequitas,akS'})


    def test_case3(self):
        result = soStronk.subset(2,[['a', '34'], ['b', '78'], ['c', '98'], ['d', '09'], ['e', '45']],5)
        self.assertEqual(result,{27.0: 'd,e', 71.5: 'c,e', 53.5: 'c,d', 61.5: 'b,e', 43.5: 'b,d', 88.0: 'b,c', 39.5: 'a,e', 21.5: 'a,d', 66.0: 'a,c', 56.0: 'a,b'})


    def test_case4(self):
        result = soStronk.subset(3,[['a', '54'], ['b', '87'], ['c', '67'], ['d', '99'], ['e', '55'], ['f', '89'], ['g', '78']],7)
        self.assertEqual(result,{74.0: 'e,f,g', 88.67: 'd,f,g', 77.33: 'b,c,g', 81.0: 'b,c,f', 78.0: 'c,f,g', 66.66: 'c,e,g', 70.33: 'c,e,f', 81.33: 'c,d,g', 85.0: 'c,d,f', 73.66: 'c,d,e', 84.67: 'b,f,g', 73.33: 'a,c,d', 77.0: 'a,d,g', 88.0: 'b,d,g', 91.67: 'b,d,f', 80.33: 'b,d,e', 69.66: 'b,c,e', 84.33: 'b,c,d', 73.67: 'a,f,g', 62.33: 'a,e,g', 66.0: 'a,e,f', 80.67: 'a,d,f', 69.33: 'a,b,c', 66.33: 'a,c,g', 70.0: 'a,c,f', 58.66: 'a,c,e', 73.0: 'a,b,g', 76.67: 'a,b,f', 65.33: 'a,b,e', 80.0: 'a,b,d'})


if __name__ =="__main__":
    unittest.main()