import java.util.Scanner;

public class _3145_UmaJornadaInesperada {
    public static void main(String[] args) {
        try (Scanner sc = new Scanner(System.in)) {
            int quantidade = sc.nextInt();
            int distancia = sc.nextInt();
            
            float divisao = (float) distancia / (quantidade + 2);

            System.out.println(String.format("%.2f", divisao));
        }
    }
}