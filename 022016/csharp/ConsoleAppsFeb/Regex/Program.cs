using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Text.RegularExpressions;
using System.Threading.Tasks;

namespace Regex
{
    class Program
    {
        static void Main(string[] args)
        {
            //var regex = new System.Text.RegularExpressions.Regex(@"\d+");
            var regex = new System.Text.RegularExpressions.Regex(@"[0-9]+");

            foreach (Match match in regex.Matches("Dot 5 Perls 4566"))
            {
                Console.WriteLine("{0}:{1}", match.Value, match.Index);
            }

            // ----------------------------------------
            var username = "abhishek";
            var matches = System.Text.RegularExpressions.Regex.Matches(username, @"[aeiou]", RegexOptions.IgnoreCase);
            foreach (Match m in matches)
            {
                Console.WriteLine("{0}", m.Value);
            }

            // ----------------------------------------
            // The following example uses the Matches(String) method to identify any words in a sentence that end in "es"
            string pattern = @"\b\w+es\b";
            System.Text.RegularExpressions.Regex rgx = new System.Text.RegularExpressions.Regex(pattern);
            string sentence = "Who writes these notes?";

            foreach (Match match in rgx.Matches(sentence))
                Console.WriteLine("Found '{0}' at position {1}", match.Value, match.Index);

            // -------------------
            username = "abhishek";
            matches = Regex. .Matches(username, @"[aeiou]", RegexOptions.IgnoreCase);



        }
    }
}
