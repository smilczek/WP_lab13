import main

def test_factorial():
  assert main.factorial(5) == 120
  assert main.factorial(4) == 24
  
def test_sum():
  assert main.sum(1, 1) == 2
  assert main.sum(1, 0) == 1
