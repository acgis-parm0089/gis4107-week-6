def has_x_code(in_text):
    if in_text.find('Tx6op3') != -1:
        return True
    else:
        return False
    
def get_x_code_position(in_text):
    code= 'Tx6op3'
    find_position = in_text.find(code)
    if find_position != -1:
        return find_position + 1
    else:
        return -1
    
print(get_x_code_position('gscgjdkjwkjfhkewhdkTx6op3'))
    
    

    