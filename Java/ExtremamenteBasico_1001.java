import java.util.Scanner;

public class ExtremamenteBasico_1001 {
    public static void main(String[] args) {
        
        try (Scanner sc = new Scanner(System.in)) {
            int a = sc.nextInt();
            int b = sc.nextInt();

            int soma = a + b;
                
            System.out.println(soma);
        }
    }
}