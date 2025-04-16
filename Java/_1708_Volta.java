import java.util.Scanner;

public class _1708_Volta {
    public static void main(String[] args) {
        try(Scanner sc = new Scanner(System.in)){

            int diferenca = 0;
            int volta = 0;

            int rapido = sc.nextInt();
            int lento = sc.nextInt();


            while (true) { 
                diferenca += lento - rapido;


                if(diferenca > lento - 1){
                    break;
                }

                volta += 1;
            }
            System.out.println(volta + 1);
        }
    }
}