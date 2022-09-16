def inc(x):
    return x + 1

def test_answer():
    assert inc(3) == 4

def test_answer_fail_1():
  assert inc(3) == 6

def test_answer_fail_2():
  assert inc(3) == 1
