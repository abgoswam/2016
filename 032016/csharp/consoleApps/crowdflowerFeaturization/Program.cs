using System;
using System.Collections.Generic;
using System.IO;
using System.Linq;
using System.Net.Http;
using System.Text;
using System.Threading;
using System.Threading.Tasks;
using System.Web;
using Newtonsoft.Json;

namespace crowdflowerFeaturization
{
    class Program
    {
        static void Main(string[] args)
        {
            MakeRequest().Wait();
        }


        static async Task MakeRequest()
        {
            var client = new HttpClient();
            var queryString = HttpUtility.ParseQueryString(string.Empty);

            // Request headers
            //client.DefaultRequestHeaders.Add("Content-Type", "application/json");
            client.DefaultRequestHeaders.Add("Ocp-Apim-Subscription-Key", "c711dd6e1fcf46fbb986235f08cbac53");

            // Request parameters
            queryString["visualFeatures"] = "All";
            var uri = "https://api.projectoxford.ai/vision/v1/analyses?" + queryString;

            HttpResponseMessage response;
            using (var sw = new StreamWriter(@"E:\hackerreborn\032016\_resources\crowdflower2\train_map_oxfordapi.csv"))
            using (var sr = new StreamReader(@"E:\hackerreborn\032016\_resources\crowdflower2\train_map.txt"))
            {
                string line;
                int k = 0;
                while ((line = sr.ReadLine()) != null)
                {
                    var tokens = line.Split('\t');
                    var url = tokens[0];
                    var localpath = tokens[1];
                    var tag = tokens[2];
                    var judgeRating = tokens[3];

                    Console.WriteLine("{0},{1},{2}", url, tag, judgeRating);

                    // Make request

                    // Method 1.
                    //byte[] byteData = Encoding.UTF8.GetBytes("{\"Url\": \"http://as2.ftcdn.net/jpg/00/03/72/76/220_F_3727624_AA8RwMFdStlFOUCCvqwlxnuk6JP4OmAO.jpg\"}");
                    //using (var content = new ByteArrayContent(byteData))
                    //{
                    //    content.Headers.ContentType = new MediaTypeHeaderValue("application/json");
                    //    response = await client.PostAsync(uri, content);
                    //}

                    // Method 2 : An alternate way to make a request
                    var requestBody = new
                    {
                        Url = url
                    };
                    response = await client.PostAsJsonAsync(uri, requestBody);

                    if (response.IsSuccessStatusCode)
                    {
                        string result = await response.Content.ReadAsStringAsync();
                        Console.WriteLine("Result: {0}", result);

                        RootObject root = JsonConvert.DeserializeObject<RootObject>(result);
                        HashSet<string> categoryWordSet = new HashSet<string>();
                        if (root.categories != null)
                        {
                            foreach (var cat in root.categories)
                            {
                                var catTokens = cat.name.Split('_');
                                foreach (var ct in catTokens)
                                {
                                    categoryWordSet.Add(ct);
                                }
                            }
                        }

                        string categoryWords = null;
                        if (categoryWordSet.Count > 0)
                        {
                            categoryWords = string.Join(" ", categoryWordSet);
                        }
                        Console.WriteLine("categories : {0}", categoryWords);
                        Console.WriteLine("foreground : {0}", root.color.dominantColorForeground);
                        Console.WriteLine("background : {0}", root.color.dominantColorBackground);
                        Console.WriteLine("---------");

                        sw.WriteLine("{0},{1},{2},{3},{4},{5},{6}", 
                            url,
                            localpath,
                            tag,
                            judgeRating,
                            categoryWords,
                            root.color.dominantColorForeground,
                            root.color.dominantColorBackground
                            );

                        sw.Flush();
                        Thread.Sleep(TimeSpan.FromSeconds(1));
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



    public class Category
    {
        public string name { get; set; }
        public double score { get; set; }
    }

    public class Adult
    {
        public bool isAdultContent { get; set; }
        public bool isRacyContent { get; set; }
        public double adultScore { get; set; }
        public double racyScore { get; set; }
    }

    public class Metadata
    {
        public int width { get; set; }
        public int height { get; set; }
        public string format { get; set; }
    }

    public class Color
    {
        public string dominantColorForeground { get; set; }
        public string dominantColorBackground { get; set; }
        public List<string> dominantColors { get; set; }
        public string accentColor { get; set; }
        public bool isBWImg { get; set; }
    }

    public class ImageType
    {
        public int clipArtType { get; set; }
        public int lineDrawingType { get; set; }
    }

    public class RootObject
    {
        public List<Category> categories { get; set; }
        public Adult adult { get; set; }
        public string requestId { get; set; }
        public Metadata metadata { get; set; }
        public List<object> faces { get; set; }
        public Color color { get; set; }
        public ImageType imageType { get; set; }
    }


}
