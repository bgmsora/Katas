def test_it(a, b):
    result=0
    for x in (str(a)):
        print(x)
        for y in (str(b)):
            result=result+int(x)*int(y)
    
    return result