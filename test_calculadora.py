from calculadora import sumar, restar, multiplicar

def test_suma():
    assert sumar(2, 3) == 5

def test_resta():
    assert restar(5, 3) == 2

def test_multiplicacion():
    assert multiplicar(2, 4) == 8
