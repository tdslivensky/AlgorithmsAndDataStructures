using System;
using System.Collections.Generic;

namespace ConsoleApp1
{
    class Program
    {
        static void Main(string[] args)
        {
            var input = Console.ReadLine();
            var tokens = input.Split(' ');
            var a = long.Parse(tokens[0]);
            var b = int.Parse(tokens[1]);
            Console.WriteLine(GCD(a, b));
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

        public static int PisanoPeriod(int m)
        {
            int current = 0;
            int next = 1;
            int period = 0;

            for (int i = 0; i < 73; i++)
            {
                var temp = next;
                next = (current + next) % m;
                current = temp;
                
                period += 1;
                if(current == 0 && next == 1)
                {
                    break;
                }
            }
            Console.WriteLine(current);
            return period;
        }

        public static int SumOfSquare(int n)
        {
            int period = PisanoPeriod(100);
            return 1;
        }
    }
}
