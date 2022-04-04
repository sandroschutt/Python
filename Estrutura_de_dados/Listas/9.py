#Faça um Programa que leia um vetor A com 10 números inteiros, calcule e mostre a soma dos quadrados dos elementos do vetor.z

A = [1,2,3,4,5,6,7,8,9,10]
somaQuadrados = 0

for i in A:
    somaQuadrados += i**2

print(somaQuadrados)