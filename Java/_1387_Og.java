import java.util.Scanner;

public class _1387_Og {
    public static void main(String[] args) {
        
        try(Scanner sc = new Scanner(System.in)){
            int x;
            int y;
    
            while (true) {
                x = sc.nextInt();
                y = sc.nextInt();
                int sx = 0;
                int sy = 0;
    
                if (x == 0 && y == 0) {
                    break;
                } else {
                    sx += x;
                    sy += y;
                    System.out.println(sx + sy);
                }
            }
        }
    }
}