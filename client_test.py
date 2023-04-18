import unittest
from client3 import getDataPoint
from client3 import getRatio

class ClientTest(unittest.TestCase):
  def test_getDataPoint_calculatePrice(self):
    quotes = [
      {'top_ask': {'price': 121.2, 'size': 36}, 'timestamp': '2019-02-11 22:06:30.572453', 'top_bid': {'price': 120.48, 'size': 109}, 'id': '0.109974697771', 'stock': 'ABC'},
      {'top_ask': {'price': 121.68, 'size': 4}, 'timestamp': '2019-02-11 22:06:30.572453', 'top_bid': {'price': 117.87, 'size': 81}, 'id': '0.109974697771', 'stock': 'DEF'}
    ]
    """ ------------ Add the assertion below ------------ """
    for quote in quotes:
      expected_stock = quote['stock']
      expected_ask   = quote['top_ask']['price']
      expected_bid   = quote['top_bid']['price']
      expected_price = (expected_bid +expected_ask)/2

      real_stock, real_bid, real_ask, real_price = getDataPoint(quote)
      self.assertEqual(expected_stock, real_stock)
      self.assertEqual(expected_bid, real_bid)
      self.assertEqual(expected_ask, real_ask)
      self.assertEqual(expected_price, real_price)
  def test_getDataPoint_calculatePriceBidGreaterThanAsk(self):
    quotes = [
      {'top_ask': {'price': 119.2, 'size': 36}, 'timestamp': '2019-02-11 22:06:30.572453', 'top_bid': {'price': 120.48, 'size': 109}, 'id': '0.109974697771', 'stock': 'ABC'},
      {'top_ask': {'price': 121.68, 'size': 4}, 'timestamp': '2019-02-11 22:06:30.572453', 'top_bid': {'price': 117.87, 'size': 81}, 'id': '0.109974697771', 'stock': 'DEF'}
    ]
    """ ------------ Add the assertion below ------------ """
    for quote in quotes:
      expected_stock = quote['stock']
      expected_ask   = quote['top_ask']['price']
      expected_bid   = quote['top_bid']['price']
      expected_price = (expected_bid +expected_ask)/2

      real_stock, real_bid, real_ask, real_price = getDataPoint(quote)
      self.assertEqual(expected_stock, real_stock)
      self.assertEqual(expected_bid, real_bid)
      self.assertEqual(expected_ask, real_ask)
      self.assertEqual(expected_price, real_price)

  """ ------------ Add more unit tests ------------ """
class MyTest(unittest.TestCase):
  def test_getRatio_CalculateRatio(self):
      #testcase
      price_a = 129.80
      price_b = 175.4
      #excepted output
      Excepted_output = (price_a/ price_b)
      #test
      real_output = getRatio(price_a, price_b)
      #Checking correctness
      self.assertEqual(Excepted_output, real_output)

  def test_getRatio_price_b_0(self):
    #testcase
      price_a_whileb_0 =135.78
      price_b_0 = 0

    #excepted output
      real_output_whileb_0 = getRatio(price_a_whileb_0, price_b_0)

if __name__ == '__main__':
    unittest.main()
