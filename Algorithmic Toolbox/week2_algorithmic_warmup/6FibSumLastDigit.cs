using System;

namespace FibSumLastDigit
{
    class Program
    {
        static void Main(string[] args)
        {
            var input = Console.ReadLine();
            var tokens = input.Split(' ');
            var a = long.Parse(tokens[0]);
            Console.WriteLine(FibSumLastDigit(a));
        }

        public static long FibLastDigit(long n)
        {
            if(n <= 1)
            {
                return n;
            }

            long current = 0;
            long next = 1;
            long temp = 0;

            for (int i = 0; i < n - 1; i++)
            {
                temp = next;
                next = (current + next) % 10;
                current = temp;
            }

            return next;
        }

        public static long FibSumLastDigit(long n)
        {
            return (FibLastDigit((n + 2) % 60)) - 1 % 10;
        }    
    }
}