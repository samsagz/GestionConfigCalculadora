from application import app
from flask import json
import sys
import unittest
import flask_testing

def testSuma():
    response = app.test_client().post(
        '/calcular',
        data=dict(expr='1+1')
    )

    data = (response.get_data(as_text=True))
    assert response.status_code == 200
    assert int(float(data)) == 2

def testResta():
    response = app.test_client().post(
        '/calcular',
        data=dict(expr='5-1')
    )

    data = (response.get_data(as_text=True))
    assert response.status_code == 200
    assert int(float(data)) == 4
    
def testMultiplicacion():
    response = app.test_client().post(
        '/calcular',
        data=dict(expr='3*3')
    )

    data = (response.get_data(as_text=True))
    assert response.status_code == 200
    assert int(float(data)) == 9

def testDivision():
    response = app.test_client().post(
        '/calcular',
        data=dict(expr='8/2')
    )

    data = (response.get_data(as_text=True))
    assert response.status_code == 200
    assert int(float(data)) == 4
    
def testCompuesta():
    response = app.test_client().post(
        '/calcular',
        data=dict(expr='5+2-3*4/2')
    )

    data = (response.get_data(as_text=True))
    assert response.status_code == 200
    assert int(float(data)) == 1 

def testDecimal():
    response = app.test_client().post(
        '/calcular',
        data=dict(expr='2.5*2.0')
    )

    data = (response.get_data(as_text=True))
    assert response.status_code == 200
    assert float(data) == 5.0   
    
def testNegativos():
    response = app.test_client().post(
        '/calcular',
        data=dict(expr='3-4')
    )

    data = (response.get_data(as_text=True))
    assert response.status_code == 200
    assert int(float(data)) == -1

def testInvalido():
    response = app.test_client().post(
        '/calcular',
        data=dict(expr='hola')
    )

    data = (response.get_data(as_text=True))
    assert response.status_code == 200
    assert data == 'error'

class TestPagina(flask_testing.TestCase):
    def create_app(self):
        return app

    def testHtml(self):
        response = self.client.get('/')
        self.assertEqual(response.status_code, 200)
        self.assert_template_used('index.html')  
         
if __name__ == "__main__":
    unittest.main()   
            