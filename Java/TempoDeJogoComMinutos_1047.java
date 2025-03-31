import java.util.Scanner;

public class TempoDeJogoComMinutos_1047 {
    public static void main(String[] args) {
        try (Scanner sc = new Scanner(System.in)) {

            int h1 = sc.nextInt();
            int m1 = sc.nextInt();
            int h2 = sc.nextInt();
            int m2 = sc.nextInt();
            
            if (h2 <= h1 && m2 <= m1) {
                h2 += 24;
            } else if (m2 <= m1) {
                m2 += 60;
                h2 -= 1;
            }
            
            int soma1 = (h1 * 3600) + (m1 * 60);
            int soma2 = (h2 * 3600) + (m2 * 60);
            
            int tempo = soma2 - soma1;
            
            int hora = tempo / 3600;
            int minuto = (tempo - (hora * 3600)) / 60;
            
            System.out.printf("O JOGO DUROU %d HORA(S) E %d MINUTO(S)\n", hora, minuto);
        }
    }
}