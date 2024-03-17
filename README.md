import java.util.Scanner;
public class Menuopciones {

    public static void main(String[] args) {
        System.out.println("MENU DE OPCIONES: ");
        
        System.out.println("ELIGE ALGUNA DE LAS OPCIONES: ");
        
        System.out.println("PERSONAS ===  1: ");
        System.out.println("VEHICULOS === 2: ");
        System.out.println("UNIVERSIDADES ==== 3: ");
        System.out.println("NOTAS === 4: ");
        System.out.println("SALIR === 5: ");
        
        System.out.println("TU OPCION:");
        
        Scanner leer = new Scanner(System.in);
        int opcion = leer.nextInt();

        switch(opcion){
          case 1: System.out.println("has presionado la opcion personas " );break;
          case 2: System.out.println("has presionado la opcion vehiculos");break;
          case 3: System.out.println("has presionado la opcion universidades" );break;
          case 4: System.out.println("has presionado la opcion notas");break;
          case 5: break;
          default: System.out.println("error, ingresa una opcion valida");
        }

    }
}
