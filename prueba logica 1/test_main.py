from funtions import fibonacci_funtion,fizz_buzz_numbers, text_contained

def test_fibonacci():
  assert fibonacci_funtion(8)==21

def test_fizz_buzz_numbers():
  assert fizz_buzz_numbers()[0]=='fizz buzz'

def test_text_contained():
  text="Hi how are things? How are you? Are you a developer? I am also a developer"
  assert text_contained(text)=={'a': 2,'also': 1, 'am': 1,'are': 3,'developer': 2,'hi': 1,'how': 2,'i': 1,'things': 1,'you': 2}