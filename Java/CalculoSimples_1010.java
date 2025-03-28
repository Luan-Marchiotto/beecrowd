import java.util.Scanner;

public class CalculoSimples_1010  {
    @SuppressWarnings("unused")
    public static void main(String[] args) {

        try (Scanner sc = new Scanner(System.in)){

            String valores1 = sc.nextLine();
            String valores2 = sc.nextLine();


            String[] valores1Array = valores1.split(" ");
            String[] valores2Array = valores2.split(" ");

            int a_1 = Integer.parseInt(valores1Array[0]);
            int b_1 = Integer.parseInt(valores1Array[1]);
            double c_1 = Double.parseDouble(valores1Array[2]);

            // Convertendo os valores da segunda linha
            int a_2 = Integer.parseInt(valores2Array[0]);
            int b_2 = Integer.parseInt(valores2Array[1]);
            double c_2 = Double.parseDouble(valores2Array[2]);

            double total1 = b_1 * c_1;
            double total2 = b_2 * c_2;

            double geral = total1 + total2;

            System.out.printf("VALOR A PAGAR: R$ %.2f\n", geral);

        } 
    }
}