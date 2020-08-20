using System;
using System.Linq;
using System.Net.Mail;
using System.Collections.Generic;
using System.Runtime.InteropServices.WindowsRuntime;
using System.Runtime.CompilerServices;

namespace SortingAlgorithms
{
    class Program
    {
        public static int count { get; set; }
        static void Main(string[] args)
        {
            Console.WriteLine("Hello World!");
            int[] arr = new int[] {2,1,3,4,5,6,9,8,7};
            
            
            Console.WriteLine("[{0}]", string.Join(", ", MergeSortCount(arr)));
            Console.WriteLine(count);
        }

        public static int[] SelectionSort(int[] array)
        {
            for(int i = 0; i < array.Length; i++)
            {
                int minIndex = i;
                for(int j = i+1; j <array.Length; j++)
                {
                    if (array[j] < array[minIndex])
                    {
                        minIndex = j;
                    }
                }
                int temp = array[i];
                array[i] = array[minIndex];
                array[minIndex] = temp;
            }

            return array;
        }

        public static int[] MergeSort(int [] a)
        {

            if (a.Length == 1)
            {
                return a;
            }

            decimal h = a.Length / 2;
            int m = Decimal.ToInt32(Math.Floor(h));

            int[] B = MergeSort(a.Take(m).ToArray());
            int[] C = MergeSort(a.Skip(m).ToArray());

            int[] A = Merge(B, C).ToArray();
            return A;
        }
        public static int[] MergeSortCount(int[] a)
        {

            if (a.Length == 1)
            {
                return a;
            }

            decimal h = a.Length / 2;
            int m = Decimal.ToInt32(Math.Floor(h));

            int[] B = MergeSortCount(a.Take(m).ToArray());
            int[] C = MergeSortCount(a.Skip(m).ToArray());

            int[] A = Merge(B, C).ToArray();
            //Console.WriteLine(count);
            return A;
        }
        private static List<int> Merge(int[] b, int[] c)
        {
            List<int> D = new List<int>();

            while(b.Length != 0 && c.Length != 0)
            {
                int beta = b[0];
                int chi = c[0];

                if (beta <= chi)
                {
                    D.Add(beta);
                    b = b.Skip(1).ToArray();
                }
                else
                {
                    D.Add(chi);
                    c = c.Skip(1).ToArray();
                    Program.count ++;
                }
            }

            if(b.Length == 0)
            {
                for(int i = 0; i < c.Length; i++)
                {
                    D.Add(c[i]);
                }
            }
            else
            {
                for (int i = 0; i < b.Length; i++)
                {
                    D.Add(b[i]);
                }
            }


            return D;
        }
    }
}
