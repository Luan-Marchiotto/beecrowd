import java.util.Scanner;

public class _1573_FabricaDeChocolate {
    public static void main(String[] args) {
        
        try (Scanner sc = new Scanner(System.in)) {
            
            while (true) { 
                int a = sc.nextInt();
                int b = sc.nextInt();
                int c = sc.nextInt();

                if (a == 0 && b == 0 && c == 0) {
                    break;
                }

                int volume = a * b * c;

                double cubo = Math.cbrt(volume);
                
                int resultado = (int) Math.floor(cubo);
                
                System.out.println(resultado);
            }
        }
    }
}