import 'dart:io';

void main() {
  List<int> numeros = [];
  print("Cuantos elementos tiene su lista?");
  int num = int.parse(stdin.readLineSync()!);
  for (int i = 1; i <= num; i++) {
    print("Ingrese elemento de la lista: ");
    int nums = int.parse(stdin.readLineSync()!);
    numeros.add(nums);
  }
  print("\nLa Lista ingresada fue: $numeros\n");
  int suma = 0;
  for (int i = 0; i < num; i++) {
    suma = suma + numeros[i];
  }
  print("La suma de los elementos de la lista es: $suma");
}
