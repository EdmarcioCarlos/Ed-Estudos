using System.Security.Cryptography.X509Certificates;

class Calculadora
{
    static void Main(string[] args)
    {
        _Calculador();
    }

    public static void _Calculador()
    {
        float Valor1,
            Valor2,
            Opção;

        Console.WriteLine("--------------------------------------");
        Console.WriteLine("Selecione as opções da calculadora:");
        Console.WriteLine("1 - Somar");
        Console.WriteLine("2 - Subtrair");
        Console.WriteLine("3 - Multiplicar");
        Console.WriteLine("4 - Divisão");
        Console.WriteLine("5 - Elevar");
        Console.WriteLine("6 - Sair");
        Console.WriteLine("-------------------------------------");
        Opção = float.Parse(Console.ReadLine());

        switch (Opção)
        {
            case 1: 
                    Console.WriteLine("Digite o primeiro valor da soma:");
                    Valor1 = float.Parse(Console.ReadLine());

                    Console.WriteLine("Digite o segundo valor da soma:");
                    Valor2 = float.Parse(Console.ReadLine());

                    Console.WriteLine("A soma dos dois valores e :"+ (Valor1+Valor2));
                    _retomar_Menu();
            break;

            case 2: 
                    Console.WriteLine("Digite o primeiro valor da subtração:");
                    Valor1 = float.Parse(Console.ReadLine());

                    Console.WriteLine("Digite o segundo valor da subtração:");
                    Valor2 = float.Parse(Console.ReadLine());

                    Console.WriteLine("A subtração dos dois valores e :"+ (Valor1-Valor2));
                    _retomar_Menu();
            break;
            case 3:
                    Console.WriteLine("Digite o valor que deve ser multiplicado:");
                    Valor1 = float.Parse(Console.ReadLine());

                    Console.WriteLine("Digite a quantidade de vezes: :");
                    Valor2 = float.Parse(Console.ReadLine());

                    Console.WriteLine("A multiplicação e :"+ (Valor1*Valor2));
                    _retomar_Menu();
            break;
            case 4:
                    Console.WriteLine("Digite o primeiro valor a ser dividido:");
                    Valor1 = float.Parse(Console.ReadLine());

                    Console.WriteLine("Digite por quantas vezes ele sera dividido :");
                    Valor2 = float.Parse(Console.ReadLine());

                    Console.WriteLine("A divisão e :"+ (Valor1/Valor2));
                    _retomar_Menu();
            break;
            case 5:
                    Console.WriteLine("Digite o valor a ser elevado:");
                    Valor1 = int.Parse(Console.ReadLine());

                    Console.WriteLine("Digite a qual potencia ele deve ser elevado:");
                    Valor2 = float.Parse(Console.ReadLine());

                    Console.WriteLine("O resultado e:" + (Math.Pow(Valor1,Valor2)));
                    _retomar_Menu();
            break;
            case 6:
                    _sair();
            break;

            default: Console.WriteLine("!!! Digite uma opção valida !!!");
                _Calculador();
             break;
        }

        static void _sair()
        {
            Console.WriteLine("!!! Saindo !!!");
        }
        static void _retomar_Menu()
        {
            string escolha;
            Console.WriteLine("-------------------------------------");
            Console.WriteLine("Aperte S para sair e R pare retornar ao menu:");
            escolha = Console.ReadLine();
            if(escolha != "s" && escolha !="r")
            {
                _retomar_Menu();
            }
            else if(escolha == "s")
            {
                _sair();
            }
            else if(escolha == "r")
            {
                _Calculador();
            }
        }
    }
}