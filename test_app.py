from app import sumar

def test_suma():
    assert sumar(5, 3) == 8

def test_suma_negativos():
    assert sumar(-2, -3) == -5

def test_suma_cero():
    assert sumar(0, 0) == 0