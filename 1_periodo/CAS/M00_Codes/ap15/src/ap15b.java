import javax.swing.*;
public class ap15b {
    public static void main(String[] args) throws Exception {
        
        // Declaração
        int n;
        char op = 0; // op == opção

        // Entrada
        n = Integer.parseInt(JOptionPane.showInputDialog("Digite um número inteiro"));
        op = (JOptionPane.showInputDialog("Digite a sua escolha:\n[1] se é Par/Ímpar\n[2] se é Positivo/Negativo").charAt(0));

        // Processamento
        if (op == '1') {

            int par_impar = n % 2;
            if (par_impar == 0) {
                System.out.println("O número "+n+" é par.");
            } else {
                System.out.println("O número "+n+" é ímpar.");
            }

        }

        if (op == '2') {

            if (n >= 0) {
                System.out.println("O número "+n+" é positivo");
            } else {
                System.out.println("O número "+n+" é negativo");
            }

        }
    }
}
