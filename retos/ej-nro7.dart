import 'dart:math';
import 'dart:io';

void main() {
  List<int> lista = [];
  print("Cuantos elementos tiene su lista?");
  int num = int.parse(stdin.readLineSync()!);
  for (int i = 1; i <= num; i++) {
    print("Ingrese elemento de la lista: ");
    int nums = int.parse(stdin.readLineSync()!);
    if (nums > 0) {
      lista.add(nums);
    } else {
      print("Recuerde ingresar un número positivo");
      i = i - 1;
    }
  }
  print("La lista ingresada es: $lista");
  lista.sort();
  print("La lista ordenada de forma ascendente es: $lista");
  print("La lista ordenada de forma descendente es: ${lista.reversed}");
  int minimo = lista.reduce(min);
  int maximo = lista.reduce(max);
  print("el menor elemento de la lista es: $minimo");
  print("el mayor elemento de la lista es: $maximo");
}
