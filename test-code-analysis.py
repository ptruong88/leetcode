def test_with_complexity():
    a = 3
    b = 4
    c = 5

    if a < b:
        if b < c:
            return a < c
    
    return False