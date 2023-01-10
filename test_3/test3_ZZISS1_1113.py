'''
1. Copy the program to the folder with your tasks.
2. Run the program.
3. You can find your test results in the file test_results.txt
'''

import sys
import unittest

class Test(unittest.TestCase):
    def test_p1(self):
        import p1
        self.assertEqual(p1.f(""), 0)
        self.assertEqual(p1.f("abba"), 7)
        self.assertEqual(p1.f("common"), 8)
        self.assertEqual(p1.f("carefully"), 14)

    def test_p2(self):
        import p2
        self.assertListEqual(p2.f([16],10), [1,0])
        self.assertListEqual(p2.f([157,24,7,192,191],100), [3,2])
        self.assertListEqual(p2.f([157,192,191],150), [3,0])

    def test_p3(self):
        import p3
        self.assertEqual(p3.f("A4"),True)
        self.assertEqual(p3.f("MX5"),True)
        self.assertEqual(p3.f("RC5432"),True)
        self.assertEqual(p3.f("G121212"),False)
        self.assertEqual(p3.f("123F"),False)
        self.assertEqual(p3.f("a6"),False)

    def test_p4(self):
        import p4
        self.assertEqual(p4.f({"BA6":51,"DGX338":6,"TWA44":142},85),"TWA44")
        self.assertEqual(p4.f({"BA6":51,"DGX338":6,"TWA44":142},20),"BA6,TWA44")

    def test_p5(self):
        import p5
        self.assertEqual(p5.C("Robin","Williams",38,2).__str__(),"RWilliams38")
        self.assertEqual(p5.C("Sofie","Pratt",25,6).__str__(),"SPratt25+")

    def test_p6(self):
        import p6
        self.assertEqual(p6.C([[2,4],[2,1],[2,2],[4,2],[2,4],[4,4],[2,4],[2,4]]).m([2,4]),4)
        self.assertEqual(p6.C([[2,4],[2,4],[2,2],[4,2],[2,4],[4,4],[2,4],[2,4]]).m([2,4]),5)

    def test_p7(self):
        import p7
        self.assertEqual(p7.C.m(1234560),2460)
        self.assertEqual(p7.C.m(707072),2)

    def test_p8(self):
        import p8
        self.s1 = p8.C({"X":50,"Y":70,"Z":90,"B":110})
        self.assertEqual(self.s1.m2(["W","Z"]),90)
        self.s1.m1("Y",170)
        self.assertEqual(self.s1.m2(["Y","Z"]),260)
        self.s1.m1("K",10)
        self.assertEqual(self.s1.m2(["K","Y","Z"]),270)

if __name__ == '__main__':
    sys.stderr = open('test_results.txt', 'w', encoding="utf-8")
    unittest.main(verbosity=2)
