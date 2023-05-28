// ignore_for_file: unused_local_variable

import 'dart:io';
import 'dart:math';

void main() {
  List<int> lista1 = [14, 2, 5, 3, 9];
  print("la primera lista es: $lista1");
  List<int> lista2 = [];
  for (int i = 1; i <= 5; i++) {
    print("ingrese elemento $i de la segunda lista");
    int elemento = int.parse(stdin.readLineSync()!);
    lista2.add(elemento);
  }
  print("la segunda lista es $lista2");
  List<int> lista3 = [];
  for (int i = 1; i <= 5; i++) {
    int elemento = Random().nextInt(10) - 25;
    lista3.add(elemento);
  }
  print("la tercera lista es $lista3");
  List<int> lista_resta = [];
  for (int i = 0; i < 5; i++) {
    int elemento = lista1[i] - lista2[i];
    lista_resta.add(elemento);
  }
  print("la resta de la primera y la segunda matriz es $lista_resta");
  List<int> lista_suma = [];
  for (int i = 0; i < 5; i++) {
    int elemento = lista_resta[i] + lista3[i];
    lista_suma.add(elemento);
  }
  print("la suma de la matriz anterior y la tercera matriz es $lista_suma");
  lista_suma.insertAll(0, [17, 24]);
  print("la lista con los elementos 17 y 24 agregados es $lista_suma");
  lista_suma.sort();
  final lista_des = lista_suma.reversed;
  print("la lista con los elementos en forma descendente es $lista_des");
}
