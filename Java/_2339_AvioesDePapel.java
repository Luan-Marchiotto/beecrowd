import java.util.Scanner;
public class _2339_AvioesDePapel{
    public static void main(String[] args) {
        try(Scanner sc = new Scanner(System.in)){
            int compe = sc.nextInt();
            int comprada = sc.nextInt();
            int pedida = sc.nextInt();

            int soma = compe * pedida;

            if(soma <= comprada){
                System.out.println("S");
            }
            else{
                System.out.println("N");
            }
        }
    }
}