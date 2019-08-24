Feature: Como el stakeholder de la calculadora, deseo probar las operaciones basicas

Scenario: realizar una suma
Given yo estoy en la pagina de la calculadora
When presiono el numero 2
And presiono la operacion de suma
And presiono el numero 3
And presiono el igual
Then el resultado debe ser 5

Scenario: realizar una resta
Given yo estoy en la pagina de la calculadora
When presiono el numero 5
And presiono la operacion de resta
And presiono el numero 2
And presiono el igual
Then el resultado debe ser 3


Scenario: realizar una multiplicacion
Given yo estoy en la pagina de la calculadora
When presiono el numero 2
And presiono la operacion de multiplicacion
And presiono el numero 3
And presiono el igual
Then el resultado debe ser 6


Scenario: realizar una division
Given yo estoy en la pagina de la calculadora
When presiono el numero 6
And presiono la operacion de division
And presiono el numero 3
And presiono el igual
Then el resultado debe ser 2

Scenario: realizar operacion compuesta
Given yo estoy en la pagina de la calculadora
When presiono el numero 5
And presiono la operacion de suma
And presiono el numero 2
And presiono la operacion de resta
And presiono el numero 3
And presiono la operacion de multiplicacion
And presiono el numero 4
And presiono la operacion de division
And presiono el numero 2
And presiono el igual
Then el resultado debe ser 1

Scenario: realizar operacion decimal
Given yo estoy en la pagina de la calculadora
When presiono el numero 2
And presiono el punto
And presiono el numero 5
And presiono la operacion de multiplicacion
When presiono el numero 2
And presiono el punto
And presiono el numero 0
And presiono el igual
Then el resultado debe ser 5