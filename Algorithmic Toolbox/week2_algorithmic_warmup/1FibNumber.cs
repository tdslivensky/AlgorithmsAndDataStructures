using System;

namespace FibNumber
{
    class Program
    {
        static void Main(string[] args)
        {
            var input = Console.ReadLine();
            var tokens = input.Split(' ');
            var a = int.Parse(tokens[0]);
            Console.WriteLine(FibNumber(a));
        }
        // itterate allong the fib sequence to get to the desired sum 
        public static int FibNumber(int n)
        {
            if (n <= 1)
            {
                return n;
            }
            int current = 0;
            int next = 1;
            int temp = 0;

            for (int i = 0; i < n - 1; i++)
            {
                temp = next;
                next = current + next;
                current = temp;
            }
            return next;
        }
    }
}