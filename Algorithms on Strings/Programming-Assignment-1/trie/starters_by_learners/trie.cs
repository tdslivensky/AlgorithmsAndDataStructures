using System;
using System.Collections.Generic;
using System.Linq;

namespace trie
{
    class Program
    {
        static void Main(string[] args)
        {
            int n = int.Parse(Console.ReadLine());
            List<string> patterns = new List<string>();
            for (int i = 0; i < n; i++)
            {
                string s = Console.ReadLine();
                patterns.Add(s);
            }

            var trie = BuildTrie(patterns);

            for (int i = 0; i < trie.Count; i++)
            {
                foreach (var edge in trie[i])
                {
                    Console.WriteLine("{0}->{1}:{2}", i, edge.Value.ToString(), edge.Key);
                }
            }
        }

        static List<Dictionary<char, int>> BuildTrie(List<string> patterns)
        {
            var trie = new List<Dictionary<char, int>>();
            var currentNode = new Dictionary<char, int>();
            trie.Add(new Dictionary<char, int>());
            var count = 0;
            foreach (string p in patterns)
            {
                var index = 0;
                currentNode = trie[0];
                for (int i = 0; i < p.Length; i++)
                {
                    var currentSymbol = p[i];
                    int v;
                    if (currentNode.TryGetValue(currentSymbol, out v))
                    {
                        currentNode = trie[v];
                        index = v;
                    }
                    else
                    {
                        var add = new Dictionary<char, int>();
                        count++;
                        trie.Add(add);
                        trie[index].Add(currentSymbol, count);
                        index = count;
                        currentNode = trie[count];

                    }
                }
            }

            return trie;
        }
    }
}