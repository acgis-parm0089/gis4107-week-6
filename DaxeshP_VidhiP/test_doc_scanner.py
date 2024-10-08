from doc_scanner import has_x_code

def test_has_x_code():
    in_text ='help'
    answer = has_x_code(in_text)
    expected = False
    assert answer == expected

def test_has_x_code():
    in_text = 'jhjjhdcgjTx6op3jhgxjhgj'
    answer = has_x_code(in_text)
    expected = True
    assert answer == expected



