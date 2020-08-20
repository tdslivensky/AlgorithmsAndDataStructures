using System;

namespace GCD
{
    class Program
    {
        static void Main(string[] args)
        {
            var input = Console.ReadLine();
            var tokens = input.Split(' ');
            var a = int.Parse(tokens[0]);
            var b = int.Parse(tokens[1]);
            Console.WriteLine(GCD(a,b));
        }

        public static int GCD(int n, int m)
        {
            int a = m;
            int b = n;
            int remainder = 0;
            while(a%b != 0)
            {
                remainder = a % b;
                a = b;
                b = remainder;
            }
            return b;
        }
    }
}

