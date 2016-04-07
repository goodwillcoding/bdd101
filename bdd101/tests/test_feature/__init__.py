from planterbox import step


@step(r'I add (\d+) and (\d+)')
def add(test, a, b):
    a = int(a)
    b = int(b)
    test.result = a + b


@step(r'the result should be (\d+)')
def check_result(test, value):
    value = int(value)
    test.assertEqual(test.result, value)
