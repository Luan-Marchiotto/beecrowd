import java.util.Scanner;

public class _1004_ProdutoSimples {
    public static void main(String[] args) {
        
        try (Scanner sc = new Scanner(System.in)) {
            int a = sc.nextInt();
            int b = sc.nextInt();

            int prod = a * b;

            System.out.print("PROD = " + prod + "\n");
        }
    }
}