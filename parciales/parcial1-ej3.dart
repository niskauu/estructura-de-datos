// ignore_for_file: unused_local_variable
import 'dart:io';
import 'dart:math';

void main() {
  List lista1 = [];
  List lista2 = [];
  List lista3 = [];
  for (int i = 0; i < 10; i++) {
    lista1.add(Random().nextInt(11) + 10);
    lista2.add(Random().nextInt(11) + 10);
  }
  for (int i = 0; i < 5; i++) {
    print("ingrese valores para la tercera lista: ");
    lista3.add(int.parse(stdin.readLineSync()!));
  }
  print("Las listas son: ");
  print(lista1);
  print(lista2);
  print(lista3);
  List lista4 = lista1 + lista2 + lista3;
  print("Las listas concatenadas resulta en: $lista4");
  int len = lista4.length;
  double promedio = 0;
  for (int i = 0; i < len; i++) {
    promedio = promedio + lista4[i];
  }
  promedio = promedio / len;
  print("El promedio de la lista es: $promedio");
  lista4.sort();
  print("La lista ordenada de forma ascendente es: $lista4");
}
