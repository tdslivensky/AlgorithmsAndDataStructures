using System;
using System.Collections.Generic;

namespace MoneyChange
{
    class Program
    {
        static void Main(string[] args)
        {
            var input = Console.ReadLine();
            var tokens = input.Split(' ');
            var a = int.Parse(tokens[0]);
            //var b = int.Parse(tokens[1]);
            Console.WriteLine(MoneyChange(a));
        }

        public static int MoneyChange(int n)
        {
            List<int> change = new List<int> {10,5,1};
            int RemainingValue = n;
            int ListIndex = 0;
            int count = 0;

            while (RemainingValue != 0)
            {
                // progress to next change item
                if(RemainingValue < change[ListIndex])
                {
                    ListIndex++;
                }
                else{
            // subtract the change and keep evauluating
                    RemainingValue -= change[ListIndex];
                    count++;
                }
            } 
            return count;
        }
    }
}