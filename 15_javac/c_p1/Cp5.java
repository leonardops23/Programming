public class Cp5 {
    // Swap two numbers
    public static void main(String[] args) {
        int valor1 = 23;
        int valor2 = 32;

        int tem = valor2;

        System.out.println("First Value: " + (valor1 = tem));
        System.out.println("Second Value: " + (valor2 = valor1));
    }
}
