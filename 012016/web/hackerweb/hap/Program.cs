using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Text.RegularExpressions;
using System.Threading.Tasks;
using HtmlAgilityPack;

namespace hap
{
    class Program
    {
        static void Main(string[] args)
        {
            var html = new HtmlDocument();
            html.Load(@"F:\aghackerreborn\012016\web\hackerweb\basichtml\index.html"); // load a file

            var root = html.DocumentNode;

            var nodes = root.Descendants();
            var totalNodes = nodes.Count();
            
            var italics = root.Descendants("i");
            //Console.WriteLine(italics.In);
            
            var p = root.Descendants().Single(n => n.GetAttributeValue("class", "").Equals("module-profile-recognition")).Descendants("p").Single();
            var content = p.InnerText;

            var points = Regex.Match(content, @"\d+").Value;
            Console.WriteLine(points);
        }
    }
}
