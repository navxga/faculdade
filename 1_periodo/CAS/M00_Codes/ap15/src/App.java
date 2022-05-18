import javax.swing.*;
public class App {
    public static void main(String[] entrada[]) {

        // Declaração
        int n1, n2, p = 1;
        char op = 0;

        // Entrada
        n1 = Integer.parseInt(JOptionPane.showInputDialog("Digite um número inteiro: "));
        n2 = Integer.parseInt(JOptionPane.showInputDialog("Digite outro número inteiro: "));
        op = (JOptionPane.showInputDialog("Digite:\n[1] Para produto\n[2] Para produtória\n")).charAt(0);

        // Processamento
        if (op == '1') {

            if (n1 >= 0 && n2 >= 0) {
                p = n1 * n2;
                System.out.println("O produto entre "+n1+" e "+n2+" é "+p);
            }else {
                System.out.println("Os dois números precisam sem positivos!");
            }

        }

        if (op == '2') {

            for (int i = 1; i <= n2; i = i + 1) {
                p = p * n1;
            }
            System.out.println("Produtoria de "+n1+", "+n2+" vezes é: "+p+"\n");

        }
    }
}     