using System;
using System.Collections.Generic;
using System.Linq;
using System.Net;
using System.Text;
using System.Threading.Tasks;

namespace bingApi
{
    class Program
    {
        static void Main(string[] args)
        {
            // This is the query - or you could get it from args.

            string query = "Xbox Live";

            // Create a Bing container.

            string rootUri = "https://api.datamarket.azure.com/Bing/Search";

            var bingContainer = new Bing.BingSearchContainer(new Uri(rootUri));

            // Replace this value with your account key.

            var accountKey = "eJIK+MiK6H4fT87BT103Ws23rs07ZwgAtndMo9l3VB8";

            // Configure bingContainer to use your credentials.

            bingContainer.Credentials = new NetworkCredential(accountKey, accountKey);

            // Build the query.

            var imageQuery = bingContainer.Image(query, null, null, null, null, null, null);

            var imageResults = imageQuery.Execute();

            foreach (var result in imageResults)
            {

                Console.WriteLine(result.Title);

            }
        }
    }
}
