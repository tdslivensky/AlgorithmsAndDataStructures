using System;

namespace FibLastDigit
{
    class Program
    {
        static void Main(string[] args)
        {
            var input = Console.ReadLine();
            var tokens = input.Split(' ');
            var a = long.Parse(tokens[0]);
            var b = long.Parse(tokens[1]);
            Console.WriteLine(GetFibLastDigit(a,b));
        }
        //# for num n the Fn mod m is 
        //# Fn mod p(the period) mod m 
        public static long PisanoPeriod( long m )
        {
            long a = 0;
            long b = 1;
            long c = a + b;
            long period = 0;
            for(int i = 0; i < m*m; i++)
            {
                c = (a + b) % m;
                a = b;
                b = c;
                if(a == 0 && b == 1)
                {
                    period = i + 1;
                    break;
                }
            }
            return period;
        }

        public static long GetFibLastDigit(long n, long m)
        {
            if(n <= 1)
            {
                return n;
            }

            // the F(n)%m of any fib value is equal to the F(n%m)%m so 𝐹2015 mod 3 we just need to find the remainder of 2015 when divided by 8. Since 2015 = 251 · 8 + 7,
            //we conclude that 𝐹2015 mod 3 = 𝐹7 mod 3 = 1.
            // find period ie 8
            //2015 = 251 · 8 + 7
            //finding 7 ie 2015 % 8

            long remainder = n % PisanoPeriod(m);

            long previous = 0;
            long current = 1;
            long temp = 0;
            // finding the F(7) % 3
            for (int i = 0; i < remainder; i++)
            {
                temp = (previous + current) % m;
                previous = current;
                current = temp;
            }

            return previous;
        }
    //https://www.shsu.edu/~ldg005/data/mth164/F2.pdf
    }
}