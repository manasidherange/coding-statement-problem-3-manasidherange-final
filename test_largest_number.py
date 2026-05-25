# MANASI DHERANGE PROBLEM STATEMENT 3
import unittest
from largest_number import largest_number

class TestLargestNumber(unittest.TestCase):
  #test 1-basuc case with 3 no.
  def test_basic_case(self):
    result = largest_number([23, 24, 25])
    self.assertEqual(result,"252423")
    
  #test case 2 classic e.g. from problem
  def test_classic_example(self):
    result = largest_number([3, 30, 34, 5, 9])
    self.assertEqual(result, "9534330")
    
  #test 3 - 2 numbers
  def test_two_numbers(self):
    result = largest_number([10,2])
    self.assertEqual(result,"210")
    
  #test4- all zeros
  def test_all_zeros(self):
    result = largest_number([0,0])
    self.assertEqual(result, "0")
    
  #test 5 single number
  def test_single_number(self):
    result = largest_number([5])
    self.assertEqual(result,"5")

  #test6= numbers with same prefix
  def test_same_prefix(self):
    result = largest_number([12,121])
    self.assertEqual(result, "12121")

  #test 7 large no
  def test_large_numbers(self):
    result = largest_number([999,998,1000])
    self.assertEqual(result, "9999981000")

  #test 8 mixed single and doube digits
  def test_mixed_digits(self):
    result = largest_number([9,99,999])
    self.assertEqual(result,"999999")

  #test 9 including zero with non 0
  def test_with_zero_and_numbers(self):
    result = largest_number([0,1,2])
    self.assertEqual(result,"210")

  #test 10 multiple 0 and numbers
  def test_multiple_zeros(self):
    result = largest_number([0,0,5,0])
    self.assertEqual(result,"5000")

def run_tests():
  suite = unittest.TestLoader().loadTestsFromTestCase(TestLargestNumber)
  runner = unittest.TextTestRunner(verbosity=2)
  result = runner.run(suite)
  return result

if __name__ =="__main__":
  print("="*60)
  print("Running largest concatenated number tests")
  print("="*60)
  print()
  run_tests()
  print()
  print("="*60)
  print("To test manually, run : python largest_number.py")
  print("="*60)

