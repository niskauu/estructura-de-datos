import 'dart:math';

void main() {
  int rango = Random().nextInt(20) + 10;
  List<int> lista = [];
  for (int i = 1; i <= rango; i++) {
    lista.add(Random().nextInt(10));
  }
  print("El largo de la lista es: $rango");
  print("La lista generafa es:  $lista");
  lista.sort();
  print("La lista ordenada de forma ascendente es: $lista");
  lista.shuffle();
  print("La lista ordenada de forma aleatoria es: $lista");
}
