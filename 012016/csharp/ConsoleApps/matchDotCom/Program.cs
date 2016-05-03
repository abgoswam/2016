using System;
using System.Collections.Generic;
using System.IO;
using System.Linq;
using System.Net;
using System.Net.Http;
using System.Net.Http.Headers;
using System.Text;
using System.Threading.Tasks;
using HtmlAgilityPack;
using Newtonsoft.Json;

namespace googleScraping
{
    public class Result
    {
        public string GsearchResultClass { get; set; }
        public string unescapedUrl { get; set; }
        public string url { get; set; }
        public string visibleUrl { get; set; }
        public string cacheUrl { get; set; }
        public string title { get; set; }
        public string titleNoFormatting { get; set; }
        public string content { get; set; }
    }

    public class Page
    {
        public string start { get; set; }
        public int label { get; set; }
    }

    public class Cursor
    {
        public string resultCount { get; set; }
        public List<Page> pages { get; set; }
        public string estimatedResultCount { get; set; }
        public int currentPageIndex { get; set; }
        public string moreResultsUrl { get; set; }
        public string searchResultTime { get; set; }
    }

    public class ResponseData
    {
        public List<Result> results { get; set; }
        public Cursor cursor { get; set; }
    }

    public class RootObject
    {
        public ResponseData responseData { get; set; }
        public object responseDetails { get; set; }
        public int responseStatus { get; set; }
    }

    internal class Program
    {
        private static void Main(string[] args)
        {
            // Using technique 1
            // RunAsync().Wait();


            // Using technique 2
            //HttpClient http = new HttpClient();

            //var response = http.GetByteArrayAsync("https://www.google.com/search?q=inurl:profile+inurl:about+site:match.com&num=100&start=1").Result;
            //String source = Encoding.GetEncoding("utf-8").GetString(response, 0, response.Length - 1);
            //source = WebUtility.HtmlDecode(source);
            //using (var sw = new StreamWriter("output3.txt"))
            //{
            //    sw.WriteLine(source);
            //}


            // Using technique 3
            //var request = (HttpWebRequest)WebRequest.Create("https://www.google.com/search?q=inurl:profile+inurl:about+site:match.com&num=100&start=1");
            //var response = (HttpWebResponse)request.GetResponse();

            //var responseText = (new StreamReader(response.GetResponseStream())).ReadToEnd();
            //using (var sw = new StreamWriter("output4.txt"))
            //{
            //    sw.WriteLine(responseText);
            //}


            // Using HtmlAgilityPack
            //string url = "https://www.google.com/search?q=inurl:profile+inurl:about+site:match.com&num=100&start=1";
            //var webGet = new HtmlWeb();
            //var document = webGet.Load(url);
            //using (var sw = new StreamWriter("output2.txt"))
            //{
            //    sw.WriteLine(document.DocumentNode.InnerHtml);
            //}

            for (int r = 0; r < 200; r++)
            {
                //var startval = 4*(r+1) ;
                //var query = string.Format("inurl:profile+inurl:about+site:match.com&start={0}", startval);
                //var url = "http://ajax.googleapis.com/ajax/services/search/web?v=1.0&q=" + query;
                //var parsedGoogleUrls = ParseGoogleJson(url);


                var startval = 1000 * r + 1;
                var queryUrl = string.Format("https://www.google.com/search?q=inurl:profile+inurl:about+site:match.com&num=1000&start={0}", startval);
                
                Console.WriteLine("r={0}", r);
                Console.WriteLine(queryUrl);


                var parsedGoogleUrls = ParseGoogleSerp(queryUrl);
                if (parsedGoogleUrls.Count < 1)
                {
                    Console.WriteLine("No results.");
                    break;
                }

                var webGet = new HtmlWeb();
                foreach (var parsedUrl in parsedGoogleUrls)
                {
                    // Console.WriteLine(parsedUrl);
                    var document = webGet.Load(parsedUrl);
                    var root = document.DocumentNode;

                    using (StreamWriter sw = File.AppendText("matchdotcomUserInfo.csv"))
                    {
                        try
                        {
                            if (root != null)
                            {
                                var divnodeBasics = root.SelectSingleNode("//div[contains(@class,'basics')]");
                                if (divnodeBasics != null)
                                {
                                    var h2Node = divnodeBasics.Descendants("h2").Single();
                                    var pNode = divnodeBasics.Descendants("p").First();

                                    if (h2Node != null && pNode != null)
                                    {
                                        var username = h2Node.InnerText.Trim();
                                        var pInnerTokens = pNode.InnerText.Trim().Split('|');

                                        var age_gender = pInnerTokens[0].Trim().Split();
                                        var age = age_gender[0].Trim();
                                        var gender = age_gender[3].Trim();

                                        var location = pInnerTokens[1].Trim().Split(',');
                                        var city = location[0].Trim();
                                        var state = location[1].Trim();

                                        if (!string.IsNullOrEmpty(username) && !string.IsNullOrEmpty(age) &&
                                            !string.IsNullOrEmpty(gender) && !string.IsNullOrEmpty(city) &&
                                            !string.IsNullOrEmpty(state))
                                        {

                                            int _age;
                                            if (!int.TryParse(age, out _age)) continue;

                                            var _g = gender.Contains("woman") ? 'F' : 'M';

                                            sw.WriteLine("{0},{1},{2},{3},{4}", username, _g, _age, city, state);
                                        }
                                    }
                                }
                            }
                        }
                        catch (Exception e)
                        {
                            Console.WriteLine("Exception : {0} : {1}", e.InnerException, e.Message);
                        }
                    }
                }
            }
        }

        private static List<string> ParseGoogleSerp(string url)
        {
            var webGet = new HtmlWeb();
            var document = webGet.Load(url);
            var root = document.DocumentNode;

            var aTags = root.Descendants("a");
            var googleUrls = new List<string>();
            foreach (var tag in aTags)
            {
                if ((tag.Attributes["href"] != null) && tag.Attributes["href"].Value.Trim().Length > 0)
                {
                    // Console.WriteLine("{0}", tag.Attributes["href"].Value);

                    var _s = tag.Attributes["href"].Value.Trim();
                    if (_s.ToLower().StartsWith("/url?q=http://www.match.com/profile/display/about") ||
                        _s.ToLower().StartsWith("/url?q=https://www.match.com/profile/display/about"))
                    {

                        var linkChunk = _s.Split(';')[0];
                        var linkUrl = linkChunk.Split('=')[1].Trim().Replace("&amp", "");
                        googleUrls.Add(linkUrl);
                    }
                }
            }

            var parsedGoogleUrls = new List<string>();
            foreach (var gurl in googleUrls)
            {
                parsedGoogleUrls.Add(gurl.Replace("%3D", "=").Replace("%3F", "?").Replace("%26", "&"));
            }
            return parsedGoogleUrls;
        }

        private static List<string> ParseGoogleJson(string url)
        {
            var request = (HttpWebRequest)WebRequest.Create(url);
            var response = (HttpWebResponse)request.GetResponse();
            var responseText = (new StreamReader(response.GetResponseStream())).ReadToEnd();

            var rootResponse = JsonConvert.DeserializeObject<RootObject>(responseText);
            var googleUrls = rootResponse.responseData.results.Select(result => result.url).ToList();

            var parsedGoogleUrls = new List<string>();
            foreach (var gurl in googleUrls)
            {
                parsedGoogleUrls.Add(gurl.Replace("%3D", "=").Replace("%3F", "?").Replace("%26", "&"));
            }
            return parsedGoogleUrls;
        }

        private static async Task RunAsync()
        {
            using (var client = new HttpClient())
            {
                client.BaseAddress = new Uri("https://www.google.com/");
                client.DefaultRequestHeaders.Accept.Clear();
                client.DefaultRequestHeaders.Accept.Add(new MediaTypeWithQualityHeaderValue("application/json"));

                for (int r = 0; r < 1; r++)
                {
                    var startval = 100*r + 1;
                    var query = string.Format("search?q=inurl:profile+inurl:about+site:match.com&num=100&start={0}", startval);
                    HttpResponseMessage response = await client.GetAsync(query);

                    if (response.IsSuccessStatusCode)
                    {
                        string result = await response.Content.ReadAsStringAsync();
                        Console.WriteLine("Result: {0}", result);

                        using (var sw = new StreamWriter("output.txt"))
                        {
                            sw.WriteLine(result);
                        }

                        var html = new HtmlDocument();
                        html.LoadHtml(result);

                        // Using XPath
                        var aTags = html.DocumentNode.SelectNodes("//a");
                        if (aTags != null)
                        {
                            int i = 0;
                            foreach (var tag in aTags)
                            {
                                if ((tag.Attributes["href"] != null) &&
                                    (tag.Attributes["href"].Value.ToLower()
                                        .Contains("www.match.com/profile/display/about/?uid=")))
                                {
                                    Console.WriteLine(i++);
                                    Console.WriteLine("{0}", tag.Attributes["href"].Value);
                                    Console.WriteLine("{0}", tag.InnerText);
                                    Console.WriteLine("------------------------");
                                }
                            }
                        }
                        Console.WriteLine("------------------------");

                    }
                    else
                    {
                        Console.WriteLine(string.Format("The request failed with status code: {0}", response.StatusCode));

                        // Print the headers - they include the requert ID and the timestamp, which are useful for debugging the failure
                        Console.WriteLine(response.Headers.ToString());

                        string responseContent = await response.Content.ReadAsStringAsync();
                        Console.WriteLine(responseContent);
                    }
                }
            }
        }
    }
}

