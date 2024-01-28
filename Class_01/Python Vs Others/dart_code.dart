String longest(String a, String b) {
  String a_plus_b = a + b;
  String a_to_z = 'abcdefghijklmnopqrstuvwxyz';
  String unique_letters = '';
  a_to_z.split('').forEach((letter) {
    a_plus_b.contains(letter) ? unique_letters += letter : '';
  });
  return unique_letters;
}

void main() {
  print(longest('abce', 'defg'));
}