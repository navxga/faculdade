import javax.swing.*;
class ap14 {
    public static void main (String entrada[]) {

        // Declaração
        int n1, n2, div;
        double pot;

        // Entrada
        n1 = Integer.parseInt(JOptionPane.showInputDialog("Digite um número inteiro: "));
        n2 = Integer.parseInt(JOptionPane.showInputDialog("Digite outro número inteiro: "));

        // Processamento
        div = (int)n1 / (int)n2;
        pot = Math.pow(n1, n2);

        // Saída
        System.out.println("n1 = "+n1+"\nn2 = "+n2+"\n");
        System.out.println("O quociente da divisão de "+n1+" por "+n2+" é "+div+"\n");
        System.out.println("A potência de "+n1+" por "+n2+" é "+pot+"\n");

        System.exit(0);

    }
}