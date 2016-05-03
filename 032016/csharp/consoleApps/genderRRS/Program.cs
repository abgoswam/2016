// This code requires the Nuget package Microsoft.AspNet.WebApi.Client to be installed.
// Instructions for doing this in Visual Studio:
// Tools -> Nuget Package Manager -> Package Manager Console
// Install-Package Microsoft.AspNet.WebApi.Client

using System;
using System.Collections.Generic;
using System.IO;
using System.Net.Http;
using System.Net.Http.Formatting;
using System.Net.Http.Headers;
using System.Text;
using System.Threading;
using System.Threading.Tasks;

namespace CallRequestResponseService
{

    public class StringTable
    {
        public string[] ColumnNames { get; set; }
        public List<List<string>> Values { get; set; }
    }

    class Program
    {
        static void Main(string[] args)
        {
            Console.WriteLine("{0}:{1}:{2}. Inside 'Main 1'", (int)AppDomain.GetCurrentThreadId(), Thread.CurrentThread.ManagedThreadId, Thread.CurrentThread.IsBackground);
            InvokeRequestResponseService().Wait();

            for (int i = 0; i < 1000; i++)
            {
                Console.WriteLine("{0}:{1}:{2}. Inside 'Main 1'", (int)AppDomain.GetCurrentThreadId(), Thread.CurrentThread.ManagedThreadId, Thread.CurrentThread.IsBackground);
                Thread.Sleep(100);
            }

            Console.WriteLine("Done");
        }

        static async Task InvokeRequestResponseService()
        {
            var myvalues = new List<List<string>>();
            myvalues.Add(new List<string>(){ "value", "value", "0", "value", "value", "value", "value", "value", "value", "value", "value", "value", "value", "value", "0", "0", "0", "0", "0", "0", "0", "0", "0", "0", "0", "0", "0", "0", "0", "0", "0", "0", "0", "0", "0", "0", "0", "0", "0", "0", "0", "0", "0", "0", "0", "0", "0", "0", "0", "0", "0", "0", "0", "0", "0", "0", "0", "0", "0", "0", "0", "0", "0", "0", "0", "0", "0" });  
            myvalues.Add(new List<string>(){ "Aaron","M","31","seattle","us","[30-35)","a  on","ron aro aar","aar","ron","A a r o n","aa","n","na","2","1","0","0.0248464830219746","-0.0577240101993084","-0.0328260958194733","-0.021992476657033","5","3","2","0","0","1","4","2","2","0","2","0","0","0","0","0","0","0","0","0","0","0","0","1","1","0","0","1","0","0","0","0","0","0","0","0","0","0","0","0","0","0","0","0","0","0" });

            using (var client = new HttpClient())
            {
                var scoreRequest = new
                {

                    Inputs = new Dictionary<string, StringTable>() { 
                        { 
                            "input1", 
                            new StringTable() 
                            {
                                ColumnNames = new string[] {"username", "gender", "age", "city", "state", "ageGroup", "usernameTokenizedWordsEn", "usernameTokenizedDssmVocab", "startTriChar", "endTriChar", "usernameSpaceSep", "maxVowelGroupString", "maxConsonantlGroupString", "maxDigitsGroupString", "maxVowelGroupStringLength", "maxConsonantGroupStringLength", "maxDigitsGroupStringLength", "maleDssmScoreUsernameOnly", "femaleDssmScoreUsernameOnly", "maleDssmScoreUsernameTokenizedWordsEn", "femaleDssmScoreUsernameTokenizedWordsEn", "usernameLength", "numVowels", "numConsonants", "numDigits", "numSpecialChars", "numCapitalLetters", "numSmallLetters", "numVowelGroups", "numConsonantGroups", "numDigitGroups", "a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z", "0", "1", "2", "3", "4", "5", "6", "7", "8", "9"},
                                Values = myvalues
                            }
                        },
                    },
                    GlobalParameters = new Dictionary<string, string>()
                    {
                    }
                };
                const string apiKey = "zDXyyg/KRMXawPo8XFOYqG07sE8AXzF1hPO28SvHvQkp/INd61VqgGscWxYFZG1RsCKtSqxbw4KIJ67pkujyZQ=="; // Replace this with the API key for the web service
                client.DefaultRequestHeaders.Authorization = new AuthenticationHeaderValue("Bearer", apiKey);

                client.BaseAddress = new Uri("https://ussouthcentral.services.azureml.net/workspaces/fbf1189ec43c495cae67a185a84e296d/services/a03879cbe1504ea9b39dfc1589f2e5b1/execute?api-version=2.0&details=true");

                // WARNING: The 'await' statement below can result in a deadlock if you are calling this code from the UI thread of an ASP.Net application.
                // One way to address this would be to call ConfigureAwait(false) so that the execution does not attempt to resume on the original context.
                // For instance, replace code such as:
                //      result = await DoSomeTask()
                // with the following:
                //      result = await DoSomeTask().ConfigureAwait(false)

                Console.WriteLine("{0}:{1}:{2}. Inside 'InvokeRequestResponseService 1'", (int)AppDomain.GetCurrentThreadId(), Thread.CurrentThread.ManagedThreadId, Thread.CurrentThread.IsBackground);
                var mytask = client.PostAsJsonAsync("", scoreRequest);
                Console.WriteLine("{0}:{1}:{2}. Inside 'InvokeRequestResponseService 2'", (int)AppDomain.GetCurrentThreadId(), Thread.CurrentThread.ManagedThreadId, Thread.CurrentThread.IsBackground);
                HttpResponseMessage response = await mytask;
                Console.WriteLine("{0}:{1}:{2}. Inside 'InvokeRequestResponseService 2.2'", (int)AppDomain.GetCurrentThreadId(), Thread.CurrentThread.ManagedThreadId, Thread.CurrentThread.IsBackground);

                if (response.IsSuccessStatusCode)
                {
                    Console.WriteLine("{0}:{1}:{2}. Inside 'InvokeRequestResponseService 3'", (int)AppDomain.GetCurrentThreadId(), Thread.CurrentThread.ManagedThreadId, Thread.CurrentThread.IsBackground);
                    string result = await response.Content.ReadAsStringAsync();
                    Console.WriteLine("{0}:{1}:{2}. Inside 'InvokeRequestResponseService 4'", (int)AppDomain.GetCurrentThreadId(), Thread.CurrentThread.ManagedThreadId, Thread.CurrentThread.IsBackground);

                    Console.WriteLine("Result: {0}", result);
                    Console.WriteLine("{0}:{1}:{2}. Inside 'InvokeRequestResponseService 5'", (int)AppDomain.GetCurrentThreadId(), Thread.CurrentThread.ManagedThreadId, Thread.CurrentThread.IsBackground);
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
