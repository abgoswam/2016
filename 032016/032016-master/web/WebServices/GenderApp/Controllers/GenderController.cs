using System;
using System.Collections.Generic;
using System.Diagnostics;
using System.IO;
using System.Linq;
using System.Net;
using System.Net.Http;
using System.Net.Http.Headers;
using System.Text;
using System.Text.RegularExpressions;
using System.Threading;
using System.Threading.Tasks;
using System.Web.Http;
using GenderApp.Models;
using Newtonsoft.Json;

namespace GenderApp.Controllers
{
    public class StringTable
    {
        public string[] ColumnNames { get; set; }
        public List<List<string>> Values { get; set; }
    }


    public class Value
    {
        public List<string> ColumnNames { get; set; }
        public List<string> ColumnTypes { get; set; }
        public List<List<string>> Values { get; set; }
    }

    public class Output1
    {
        public string type { get; set; }
        public Value value { get; set; }
    }

    public class Results
    {
        public Output1 output1 { get; set; }
    }

    public class RootObject
    {
        public Results Results { get; set; }
    }

    public enum ModelType
    {
        DSSM,
        CDSSM,
    }

    public class GenderController : ApiController
    {
        //public static string maleSynonyms;
        //public static string femaleSynonyms;

        //static GenderController()
        //{
        //    maleSynonyms = "male man men manly boy he masculine father brother buddy dude gentleman paternal person macho manliness manful king prince guy gent";
        //    femaleSynonyms = "female woman women girl she feminine mother sister gal womanly womanish maternal babe chick dame doll honey lady miss damsel maid maiden miss lady girlish queen princess";
        //    Debug.WriteLine("Inside static controller for 'GenderController.'");
        //}

        public IHttpActionResult GetProduct(string username)
        {
            if (string.IsNullOrEmpty(username))
            {
                return BadRequest("username is null or empty.");
            }

            Debug.WriteLine("{0}:{1}:{2}. Inside 'GetProductAsync 1'", (int)AppDomain.GetCurrentThreadId(), Thread.CurrentThread.ManagedThreadId, Thread.CurrentThread.IsBackground);
            var sb = InvokeRequestResponseServiceAsync(username).Result;
            Debug.WriteLine("{0}:{1}:{2}. Inside 'GetProductAsync 2'", (int)AppDomain.GetCurrentThreadId(), Thread.CurrentThread.ManagedThreadId, Thread.CurrentThread.IsBackground);

            try
            {
                RootObject result = JsonConvert.DeserializeObject<RootObject>(sb);
                return Ok(result);
            }
            catch (Exception)
            {
                return BadRequest(sb);
            }
        }

        static async Task<string> InvokeRequestResponseServiceAsync(string username)
        {
            // Tokenize username into words in English language
            var usernameTokenizedWordsEnList = WebApiConfig.wordsEn.Where(word => username.ToLower().Contains(word)).ToList();
            string usernameTokenizedWordsEn = string.Join(" ", usernameTokenizedWordsEnList);

            // DSSM Scores
            double maleDssmScoreUsernameOnly = DssmScoring(WebApiConfig.src_dssm, WebApiConfig.tgt_dssm, username, WebApiConfig.maleSynonyms);
            double femaleDssmScoreUsernameOnly = DssmScoring(WebApiConfig.src_dssm, WebApiConfig.tgt_dssm, username, WebApiConfig.femaleSynonyms);
            double maleDssmScoreUsernameTokenizedWordsEn = DssmScoring(WebApiConfig.src_dssm, WebApiConfig.tgt_dssm, usernameTokenizedWordsEn, WebApiConfig.maleSynonyms);
            double femaleDssmScoreUsernameTokenizedWordsEn = DssmScoring(WebApiConfig.src_dssm, WebApiConfig.tgt_dssm, usernameTokenizedWordsEn, WebApiConfig.femaleSynonyms);

            // Tokenize username into words in DSSM Vocab
            var usernameTokenizedDssmVocabList = WebApiConfig.dssmVocab.Where(word => username.ToLower().Contains(word)).ToList();
            string usernameTokenizedDssmVocab = string.Join(" ", usernameTokenizedDssmVocabList);

            // ------------------------------
            var vowels = Regex.Matches(username, @"[aeiou]", RegexOptions.IgnoreCase);
            var consonants = Regex.Matches(username, @"[^aeiou\d\W]", RegexOptions.IgnoreCase);
            var digits = Regex.Matches(username, @"\d", RegexOptions.IgnoreCase);
            var specialcharacters = Regex.Matches(username, @"\W");
            var capitalletters = Regex.Matches(username, @"[A-Z]");
            var smallletters = Regex.Matches(username, @"[a-z]");

            // -----------------------------------
            var vowelGroups = Regex.Matches(username, @"[aeiou]+", RegexOptions.IgnoreCase);
            var consonantGroups = Regex.Matches(username, @"[^aeiou0-9\W]+", RegexOptions.IgnoreCase);
            var digitsGroups = Regex.Matches(username, @"\d+", RegexOptions.IgnoreCase);

            string maxVowelGroupString = "na";
            int maxVowelGroupStringLength = 0;
            foreach (Match match in vowelGroups)
            {
                if (match.Value.Length >= maxVowelGroupStringLength)
                {
                    maxVowelGroupString = match.Value.ToLower();
                    maxVowelGroupStringLength = maxVowelGroupString.Length;
                }
            }

            string maxConsonantlGroupString = "na";
            int maxConsonantGroupStringLength = 0;
            foreach (Match match in consonantGroups)
            {
                if (match.Value.Length >= maxConsonantGroupStringLength)
                {
                    maxConsonantlGroupString = match.Value.ToLower();
                    maxConsonantGroupStringLength = maxConsonantlGroupString.Length;
                }
            }

            string maxDigitsGroupString = "na";
            int maxDigitsGroupStringLength = 0;
            foreach (Match match in digitsGroups)
            {
                if (match.Value.Length >= maxDigitsGroupStringLength)
                {
                    maxDigitsGroupString = match.Value.ToLower();
                    maxDigitsGroupStringLength = maxDigitsGroupString.Length;
                }
            }

            // -------------------------------
            string pattern = @"[\W\d]";
            Regex rgx = new Regex(pattern);
            string replacedUsername = rgx.Replace(username, "");

            var starttricharmatch = Regex.Match(replacedUsername, @"^.{3}", RegexOptions.IgnoreCase);
            var endtricharmatch = Regex.Match(replacedUsername, @".{3}$", RegexOptions.IgnoreCase);

            // -------------------------------

            var featuresPart1 = new List<string>()
            {
                username,
                "dummygender",
                "0",
                "dummycity",
                "dummystate",
                "dummyagegroup",
                usernameTokenizedWordsEn,
                usernameTokenizedDssmVocab,
                starttricharmatch.Value.ToLower(),
                endtricharmatch.Value.ToLower(),
                string.Join(" ", username.ToLower().ToCharArray()),
                maxVowelGroupString,
                maxConsonantlGroupString,
                maxDigitsGroupString,
                maxVowelGroupStringLength.ToString(),
                maxConsonantGroupStringLength.ToString(),
                maxDigitsGroupStringLength.ToString(),
                maleDssmScoreUsernameOnly.ToString(),
                femaleDssmScoreUsernameOnly.ToString(),
                maleDssmScoreUsernameTokenizedWordsEn.ToString(),
                femaleDssmScoreUsernameTokenizedWordsEn.ToString(),
                username.Length.ToString(),
                vowels.Count.ToString(),
                consonants.Count.ToString(),
                digits.Count.ToString(),
                specialcharacters.Count.ToString(),
                capitalletters.Count.ToString(),
                smallletters.Count.ToString(),
                vowelGroups.Count.ToString(),
                consonantGroups.Count.ToString(),
                digitsGroups.Count.ToString()
            };

            var asciiList = new List<char>();
            for (char c = 'a'; c <= 'z'; c++)
            {
                asciiList.Add(c);
            }
            for (char c = '0'; c <= '9'; c++)
            {
                asciiList.Add(c);
            }
            var asciiHist = asciiList.ToDictionary(c => c, c => 0);
            foreach (char c in username.ToLower())
            {
                if (asciiHist.ContainsKey(c))
                {
                    asciiHist[c]++;
                }
            }

            List<string> featuresPart2 = asciiList.Select(c => asciiHist[c].ToString()).ToList();
            var features = featuresPart1.Concat(featuresPart2).ToList();

            using (var client = new HttpClient())
            {
                var featureValues = new List<List<string>> {features};

                var scoreRequest = new
                {

                    Inputs = new Dictionary<string, StringTable>() { 
                        { 
                            "input1", 
                            new StringTable() 
                            {
                                ColumnNames = new string[] {"username", "gender", "age", "city", "state", "ageGroup", "usernameTokenizedWordsEn", "usernameTokenizedDssmVocab", "startTriChar", "endTriChar", "usernameSpaceSep", "maxVowelGroupString", "maxConsonantlGroupString", "maxDigitsGroupString", "maxVowelGroupStringLength", "maxConsonantGroupStringLength", "maxDigitsGroupStringLength", "maleDssmScoreUsernameOnly", "femaleDssmScoreUsernameOnly", "maleDssmScoreUsernameTokenizedWordsEn", "femaleDssmScoreUsernameTokenizedWordsEn", "usernameLength", "numVowels", "numConsonants", "numDigits", "numSpecialChars", "numCapitalLetters", "numSmallLetters", "numVowelGroups", "numConsonantGroups", "numDigitGroups", "a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z", "0", "1", "2", "3", "4", "5", "6", "7", "8", "9"},
                                Values = featureValues
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

                Debug.WriteLine("{0}:{1}:{2}. Inside 'InvokeRequestResponseService 1'", (int)AppDomain.GetCurrentThreadId(), Thread.CurrentThread.ManagedThreadId, Thread.CurrentThread.IsBackground);
                var mytask = client.PostAsJsonAsync("", scoreRequest);
                
                Debug.WriteLine("{0}:{1}:{2}. Inside 'InvokeRequestResponseService 2'", (int)AppDomain.GetCurrentThreadId(), Thread.CurrentThread.ManagedThreadId, Thread.CurrentThread.IsBackground);
                HttpResponseMessage response = await mytask.ConfigureAwait(false);
                
                // HttpResponseMessage response = await client.PostAsJsonAsync("", scoreRequest).ConfigureAwait(false);


                var sb = new StringBuilder();
                if (response.IsSuccessStatusCode)
                {
                    Debug.WriteLine("{0}:{1}:{2}. Inside 'InvokeRequestResponseService 3'", (int)AppDomain.GetCurrentThreadId(), Thread.CurrentThread.ManagedThreadId, Thread.CurrentThread.IsBackground);
                    string result = await response.Content.ReadAsStringAsync();
                    
                    Debug.WriteLine("{0}:{1}:{2}. Inside 'InvokeRequestResponseService 4'", (int)AppDomain.GetCurrentThreadId(), Thread.CurrentThread.ManagedThreadId, Thread.CurrentThread.IsBackground);
                    
                    // string result = await response.Content.ReadAsStringAsync().ConfigureAwait(false);
                    Console.WriteLine("Result: {0}", result);
                    
                    Debug.WriteLine("{0}:{1}:{2}. Inside 'InvokeRequestResponseService 5'", (int)AppDomain.GetCurrentThreadId(), Thread.CurrentThread.ManagedThreadId, Thread.CurrentThread.IsBackground);
                    sb.Append(result);
                }
                else
                {
                    Console.WriteLine(string.Format("The request failed with status code: {0}", response.StatusCode));

                    // Print the headers - they include the requert ID and the timestamp, which are useful for debugging the failure
                    Console.WriteLine(response.Headers.ToString());
                    sb.Append(response.Headers.ToString());

                    string responseContent = await response.Content.ReadAsStringAsync().ConfigureAwait(false);
                    Console.WriteLine(responseContent);
                    sb.Append(responseContent);
                }

                return sb.ToString();
            }
        }

        static double DssmScoring(DNN srcDssm, DNN tgtDssm, string srcstr, string tgtstr)
        {
            List<float> srcvec = null;
            srcvec = srcDssm.Forward(srcstr);

            List<float> tgtvec = null;
            tgtvec = tgtDssm.Forward(tgtstr);

            double cosscr = 0.0;
            if (srcvec != null && tgtvec != null)
                cosscr = BasicMathlib.Cos_Similarity(srcvec, tgtvec);

            return cosscr;
        }
    }
}
