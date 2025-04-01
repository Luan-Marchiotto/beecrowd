import java.util.Scanner;

public class Tomadas_1930 {
    public static void main(String[] args) {
        try (Scanner sc = new Scanner(System.in)) {
            int[] tomadas = new int[4]; 
            
            int totalTomadas = 0;
            for (int i = 0; i < 4; i++) {
                tomadas[i] = sc.nextInt();
                totalTomadas += tomadas[i];
            }

            totalTomadas -= 3;

            System.out.println(totalTomadas);
        }
    }
}