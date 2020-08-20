using System;
using System.Collections.Generic;
using System.Linq;

//this functions it just didn't compile on the test server 
//functionality replicated in python in file with same name

namespace trie_matching
{
    class Program
    {
        static void Main(string[] args)
        {
            //int n = int.Parse(Console.ReadLine());
            //List<string> patterns = new List<string>();
            //for (int i = 0; i < n; i++)
            //{
            //    string s = Console.ReadLine();
            //    patterns.Add(s);
            //}

            //var trie = BuildTrie(patterns);

            //for (int i = 0; i < trie.Count; i++)
            //{
            //    foreach (var edge in trie[i])
            //    {
            //        Console.WriteLine("{0}->{1}:{2}", i, edge.Value.ToString(), edge.Key);
            //    }
            //}
            string text = Console.ReadLine();
            int n = int.Parse(Console.ReadLine());
            List<string> patterns = new List<string>();
            for (int i = 0; i < n; i++)
            {
                string s = Console.ReadLine();
                patterns.Add(s);
            }

            List<long> answers = Solve(text, patterns);
            string answersLine = string.Join(" ", answers);
            answersLine = answersLine + "\n";
            Console.WriteLine(answersLine);
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

        static List<long> Solve(string text, List<string> patterns)
        {
            List<long> ans = new List<long>();
            var trie = BuildTrie(patterns);
            var t = text.ToList();
            var count = 0;
            while (t.Count != 0)
            {
                var curr = Match(t, trie);

                if (curr)
                {
                    ans.Add(count);
                    count++;
                }
                else
                {
                    count++;
                }

                t = t.Skip(1).ToList();
            }

            return ans;
        }

        static bool Match(List<char> text, List<Dictionary<char, int>> trie)
        {
            int index = 0;
            char currentSymbol = text[index];
            var currentNode = trie[index];
            var a = 0;
            while (a < text.Count)
            {
                if (currentNode.TryGetValue(currentSymbol, out int v))
                {
                    if (trie[v].Count == 0)
                    {
                        return true;
                    }
                    else
                    {
                        index++;
                        currentSymbol = index == text.Count ? 'A' : text[index];
                        currentNode = trie[v];
                    }
                }
                else
                {
                    return false;
                }
                a++;
            }
            return false;
        }
    }
}