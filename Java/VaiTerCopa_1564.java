import java.util.Scanner;

public class VaiTerCopa_1564 {
    public static void main(String[] args) {
        try (Scanner scanner = new Scanner(System.in)) {
            while (scanner.hasNextInt()) {
                int reclamacao = scanner.nextInt();
                
                if (reclamacao == 0) {
                    System.out.println("vai ter copa!");
                } else {
                    System.out.println("vai ter duas!");
                }
            }
        }
    }
}