import java.util.Scanner;

public class ProdutoSimples_1004 {
    public static void main(String[] args) {
        
        try (Scanner sc = new Scanner(System.in)) {
            int a = sc.nextInt();
            int b = sc.nextInt();

            int prod = a * b;

            System.out.print("PROD = " + prod + "\n");
        }
    }
}