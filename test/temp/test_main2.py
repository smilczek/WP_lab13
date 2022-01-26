from temp import main2

def test_five_times():
  assert main2.five_times('#') == '#####'
  assert main2.five_times('some text') == 'some textsome textsome textsome textsome text'
  
def test_what_is():
  assert main2.what_is('whatever') == 'garbage'
  assert main2.what_is('gold') == 'garbage'
  assert main2.what_is('garbage') == 'garbage'
