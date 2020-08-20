using System;
using System.Collections.Generic;

namespace reachability
{
    class Program
    {
        static void Main(string[] args)
        {
            var s = new List<string>();
            string l;
            while(!String.IsNullOrWhiteSpace(l = Console.ReadLine()))
            {
                s.Add(l);
            }
            Console.WriteLine(s.Count);
        }

    }
}
