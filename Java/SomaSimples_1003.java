import java.util.Scanner;

public class SomaSimples_1003{
    public static void main(String[] args) {
        
        try (Scanner sc = new Scanner(System.in)){
            int a = sc.nextInt();
            int b = sc.nextInt();
    
            int soma = a + b;
    
            System.out.println(soma);
        }
    }
}
