using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using HtmlAgilityPack;

namespace htmlAgilityPack
{
    class Program
    {
        static void Main(string[] args)
        {
            string url = "http://www.4guysfromrolla.com/";

            var webGet = new HtmlWeb();
            var document = webGet.Load(url);

            //Console.WriteLine(document.DocumentNode.InnerHtml);

            // Using XPath
            var metaTags = document.DocumentNode.SelectNodes("//meta");
            if (metaTags != null)
            {
                foreach (var tag in metaTags)
                {
                    if ((tag.Attributes["name"] != null) && (tag.Attributes["content"] != null))
                    {
                        Console.WriteLine("{0}:{1}", tag.Attributes["name"].Value, tag.Attributes["content"].Value);
                    }
                }
            }
            Console.WriteLine("------------------------");

            // Using Linq
            var linksOnPage = from lnks in document.DocumentNode.Descendants()
                              where lnks.Name == "a" &&
                                   lnks.Attributes["href"] != null &&
                                   lnks.InnerText.Trim().Length > 0
                              select new
                              {
                                  Url = lnks.Attributes["href"].Value,
                                  Text = lnks.InnerText
                              };

            Console.WriteLine(linksOnPage.Count());
            Console.WriteLine("------------------------");

            var aTags = document.DocumentNode.Descendants("a");
            var linksOnPage2 = new List<string>();
            foreach (var tag in aTags)
            {
                if ((tag.Attributes["href"] != null) && tag.Attributes["href"].Value.Trim().Length > 0)
                {
                    // Console.WriteLine("{0}", tag.Attributes["href"].Value);
                    linksOnPage2.Add(tag.Attributes["href"].Value);
                }
            }
            Console.WriteLine(linksOnPage2.Count);
            // note how this is similar to the LINQ expression
            // var linksOnPage2 = 
            //      (from tag in aTags 
            //      where (tag.Attributes["href"] != null) && tag.Attributes["href"].Value.Length > 0 
            //      select tag.Attributes["href"].Value).ToList();


        }
    }
}
