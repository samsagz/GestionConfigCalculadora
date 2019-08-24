import time
import unittest
import os
from behave import *
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options 

"""----------Escenario realizar una suma-------------""" 

@given('yo estoy en la pagina de la calculadora')
def step_impl(context):
    inicio(context)

@when('presiono el numero 2')
def step_impl(context):
    presionoTecla(context, '2')
    
@when('presiono la operacion de suma')
def step_impl(context):
    presionoTecla(context, 'suma')

@when('presiono el numero 3')
def step_impl(context):
    presionoTecla(context, '3')
    
@when('presiono el igual')
def step_impl(context):
    presionoTecla(context, 'resolver')
    time.sleep(2)

@then('el resultado debe ser 5')
def step_impl(context):
    verificar(context,'5')
    fin(context)

"""----------Escenario realizar una resta-------------""" 

@when('presiono el numero 5')
def step_impl(context):
    presionoTecla(context, '5')
    
@when('presiono la operacion de resta')
def step_impl(context):
    presionoTecla(context, 'resta')

@then('el resultado debe ser 3')
def step_impl(context):
    verificar(context,'3')
    fin(context)
    
"""----------Escenario realizar una multiplicacion-------------""" 
   
@when('presiono la operacion de multiplicacion')
def step_impl(context):
        presionoTecla(context, 'multiplicacion')

@then('el resultado debe ser 6')
def step_impl(context):
    verificar(context,'6')
    fin(context)
    
"""----------Escenario realizar una division-------------""" 

@when('presiono el numero 6')
def step_impl(context):
    presionoTecla(context, '6')
    
@when('presiono la operacion de division')
def step_impl(context):
    presionoTecla(context, 'division')

@then('el resultado debe ser 2')
def step_impl(context):
    verificar(context,'2')
    fin(context)
    
"""----------Escenario realizar operacion compuesta-------------""" 

@when('presiono el numero 4')
def step_impl(context):
        presionoTecla(context, '4')
        
@then('el resultado debe ser 1')
def step_impl(context):
    verificar(context,'1')
    fin(context)
    
"""----------Escenario realizar operacion decimal-------------""" 
    
@when('presiono el punto')
def step_impl(context):
    presionoTecla(context, 'punto')
    
@when('presiono el numero 0')
def step_impl(context):
    presionoTecla(context, '0')
            
"""----------Operaciones genericas-------------"""    
    
def inicio(context):
    time.sleep(2)
    chrome_options = webdriver.ChromeOptions()
    chrome_options.add_argument('--headless')
    chrome_options.add_argument('--no-sandbox')      
    context.driver = webdriver.Chrome(executable_path='/home/dev/chromedriver', options=chrome_options, service_args=['--verbose', '--log-path=/workspace/flask/chromedriver.log'])
    context.driver.set_window_size(1120, 550)
    context.driver.get("https://calculadora.run.goorm.io")
    
def presionoTecla(context, id):
    context.driver.find_element(By.ID, id).click()
    
def verificar(context, checkValue):
    value = context.driver.find_element(By.ID, "result").get_attribute("value")
    assert value == checkValue
    
def fin(context):
    context.driver.close()
    context.driver.quit()

    