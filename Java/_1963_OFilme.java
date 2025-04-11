import java.util.Scanner;

public class _1963_OFilme{
    public static void main(String[] args) {
        try(Scanner sc = new Scanner(System.in)){

            float antigo = sc.nextFloat();
            float novo = sc.nextFloat();

            float resultado = ((novo - antigo) / antigo) * 100;

            System.out.printf("%.2f%%\n", resultado);
        }
    }
}