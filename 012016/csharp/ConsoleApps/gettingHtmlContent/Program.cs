using System;
using System.IO;
using System.Net;
using System.Text;
using System.Net.Http;
using System.Net.Http.Headers;
using System.Threading.Tasks;

namespace gettingHtmlContent
{
    class Program
    {
        static void Main(string[] args)
        {
            ParseGoogle();
            GetOkCupidProfile();
            DotNetPearls();
        }

        public static void ParseGoogle()
        {
            var query = "inurl:profile inurl:about site:match.com";
            query = query.Replace(" ", "+");
            var url = "http://www.google.com/search?q=" + query;

            var content1 = GetContent1(url);
            using (StreamWriter writer = new StreamWriter("content1.txt"))
            {
                writer.Write(content1);
            }
        }

        public static void GetOkCupidProfile()
        {
            var content2 = GetContent2();
            using (StreamWriter writer = new StreamWriter("content2.txt"))
            {
                writer.Write(content2);
            }
        }

        public static void DotNetPearls()
        {
            //var url = "http://www.dotnetperls.com/streamwriter";

            var query = "inurl:profile inurl:about site:match.com";
            query = query.Replace(" ", "+");
            var url = "http://www.google.com/search?q=" + query;

            url = "http://www.strchr.com/hash_functions";
            var content3 = GetContent3(url);
            using (StreamWriter writer = new StreamWriter("content3.txt"))
            {
                writer.Write(content3);
            }
        }

        private static string GetContent3(string url)
        {
            var request = (HttpWebRequest)WebRequest.Create(url);
            var response = (HttpWebResponse)request.GetResponse();

            var responseText = (new StreamReader(response.GetResponseStream())).ReadToEnd();
            return responseText;
        }

        private static string GetContent1(string url)
        {
            HttpClient http = new HttpClient();

            var response = http.GetByteArrayAsync(url).Result;
            String source = Encoding.GetEncoding("utf-8").GetString(response, 0, response.Length - 1);

            source = WebUtility.HtmlDecode(source);
            return source;
        }

        private static string GetContent2()
        {
            return RunAsync().Result;
        }

        static async Task<string> RunAsync()
        {
            string result = null;
            using (var client = new HttpClient())
            {
                client.BaseAddress = new Uri("http://www.okcupid.com/");
                client.DefaultRequestHeaders.Accept.Clear();
                client.DefaultRequestHeaders.Accept.Add(new MediaTypeWithQualityHeaderValue("application/json"));

                HttpResponseMessage response = await client.GetAsync("profile/iLikeYourMelody?cf=home_matches,profile_quickview&subject_id=18247187647605098355&picid=12119248317877708039");
                if (response.IsSuccessStatusCode)
                {
                    result = await response.Content.ReadAsStringAsync();
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

            return result;
        }
    }
}
