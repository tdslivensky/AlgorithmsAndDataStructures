using System;

namespace FibLastDigit
{
    class Program
    {
        static void Main(string[] args)
        {
            var input = Console.ReadLine();
            var tokens = input.Split(' ');
            var a = int.Parse(tokens[0]);
            Console.WriteLine(FibLastDigit(a));
        }

        // itterate along the sequence but only take the modulo 10 to get the last digit
        public static int FibLastDigit(int n)
        {
            if(n <= 1)
            {
                return n;
            }

            int current = 0;
            int next = 1;
            int temp = 0;

            for (int i = 0; i < n - 1; i++)
            {
                temp = next;
                next = (current + next) % 10;
                current = temp;
            }

            return next;
        }
    }
}