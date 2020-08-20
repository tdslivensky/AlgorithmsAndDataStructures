using System;

namespace LCM
{
    class Program
    {
        static void Main(string[] args)
        {
            var input = Console.ReadLine();
            var tokens = input.Split(' ');
            var a = int.Parse(tokens[0]);
            var b = int.Parse(tokens[1]);
            Console.WriteLine(LCM(a,b));
        }

        public static long GCD(long n, long m)
        {
            long a = m;
            long b = n;
            long remainder = 0;
            while(a%b != 0)
            {
                remainder = a % b;
                a = b;
                b = remainder;
            }
            return b;
        }

        public static long LCM(long n, long m)
        {
            return (n * m) / GCD(n, m);
        }
    }
}