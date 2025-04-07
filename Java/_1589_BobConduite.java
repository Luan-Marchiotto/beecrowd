import java.util.Scanner;
public class _1589_BobConduite {
    public static void main(String[] args) {
        try(Scanner sc = new Scanner(System.in)){
            int rep, a, b;

            rep = sc.nextInt();

            for(int i = 0; i < rep; i++){

                a = sc.nextInt();
                b = sc.nextInt();

                System.out.println(a + b);
            }
        }
    }
}