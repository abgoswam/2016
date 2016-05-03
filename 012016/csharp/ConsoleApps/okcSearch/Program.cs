using System;
using System.Collections.Generic;
using System.Linq;
using System.Net.Http;
using System.Net.Http.Headers;
using System.Text;
using System.Threading.Tasks;
using HtmlAgilityPack;
using System.IO;
using System.Threading;

namespace okcSearch
{
    class Program
    {
        static void Main(string[] args)
        {
            RunAsync().Wait();
            Console.WriteLine("DONE");
        }

        private static async Task RunAsync()
        {
            using (var client = new HttpClient())
            {
                client.BaseAddress = new Uri("http://www.okcupid.com/");
                client.DefaultRequestHeaders.Accept.Clear();
                client.DefaultRequestHeaders.Accept.Add(new MediaTypeWithQualityHeaderValue("application/json"));

                // 32: F
                // 16: M
                var genderCodes = new List<int>() { 32, 16 };
                for (var agecode = 18; agecode < 81; agecode++)
                {
                    foreach (var gcode in genderCodes)
                    {

                        var filterStr =
                            string.Format(
                                "match?filter1=0,{0}&filter2=2,{1},{2}&filter3=1,1&locid=0&timekey=1&fromWhoOnline=0&mygender=&update_prefs=1&sort_type=0&sa=1&count=1000",
                                gcode, agecode, agecode);

                        Console.WriteLine(filterStr);
                        HttpResponseMessage response = await client.GetAsync(filterStr);

                        if (response.IsSuccessStatusCode)
                        {
                            string result = await response.Content.ReadAsStringAsync();
                            //Console.WriteLine("Result: {0}", result);

                            var html = new HtmlDocument();

                            // Load the string already retrieved by the HttpClient.
                            html.LoadHtml(result);
                            var root = html.DocumentNode;

                            using (StreamWriter sw = File.AppendText("okcupidUserInfo.csv"))
                            {
                                try
                                {

                                    if (root != null)
                                    {
                                        var divnodesProfileinfo = root.SelectNodes("//div[contains(@class,'profile_info')]");
                                        if (divnodesProfileinfo != null)
                                        {
                                            foreach (var div in divnodesProfileinfo)
                                            {
                                                //Console.WriteLine("InnerHtml : {0}", div.InnerHtml);

                                                var nameNode = 
                                                    div.Descendants()
                                                        .Single(n => n.GetAttributeValue("class", "").Equals("name"));
                                                //Console.WriteLine("nameNode : {0}", nameNode.InnerText);

                                                var ageNode =
                                                    div.Descendants()
                                                        .Single(n => n.GetAttributeValue("class", "").Equals("age"));
                                                //Console.WriteLine("ageNode : {0}", ageNode.InnerText);

                                                var locationNode =
                                                    div.Descendants()
                                                        .Single(n => n.GetAttributeValue("class", "").Equals("location"));
                                                //Console.WriteLine("locationNode : {0}", locationNode.InnerText);


                                                var username = nameNode.InnerText.Trim().Replace(",", "");
                                                var gender = gcode == 32 ? 'F' : 'M';
                                                var age = ageNode.InnerText.Trim().Replace(",", "");
                                                var tokens = locationNode.InnerText.Split(',');

                                                if (tokens.Length != 2)
                                                    continue;

                                                var city = tokens[0].Trim().Replace(",", "");
                                                var state = tokens[1].Trim().Replace(",", "");

                                                sw.WriteLine("{0},{1},{2},{3},{4}", username, gender, age, city, state);

                                                //Console.WriteLine("{0},{1},{2},{3},{4}", username, gender, age, city, state);
                                                //Console.WriteLine("------------");
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
                        else
                        {
                            Console.WriteLine(string.Format("The request failed with status code: {0}",
                                response.StatusCode));

                            // Print the headers - they include the requert ID and the timestamp, which are useful for debugging the failure
                            Console.WriteLine(response.Headers.ToString());

                            string responseContent = await response.Content.ReadAsStringAsync();
                            Console.WriteLine(responseContent);
                        }

                        Thread.Sleep(TimeSpan.FromSeconds(1));
                    }
                }
            }
        }
    }
}
