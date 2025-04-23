import java.util.Scanner;

public class _1865_Mjolnir {
    public static void main(String[] args) {
        try (Scanner sc = new Scanner(System.in)) {
            int rep = sc.nextInt();
            
            for (int i = 0; i < rep; i++) {
                String nome = sc.next();
                @SuppressWarnings("unused")
                        int forca = sc.nextInt();
                
                if (nome.equals("Thor")) {
                    System.out.println("Y");
                } else {
                    System.out.println("N");
                }
            }
        }
    }
}