from src.Ejercicio4 import contarBanana

def test_contarBanana():
    assert contarBanana("a") == 3
    assert contarBanana("b") == 1
    assert contarBanana("n") == 2
