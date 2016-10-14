using System;
using System.Collections.Generic;
using System.Globalization;
using System.Linq;
using System.Security.Cryptography;
using System.Text;
using System.Threading.Tasks;
using System.Web;

namespace CreateSASApp
{
    class Program
    {
        static void Main(string[] args)
        {
            var sasToken = createToken("http://simplexagpmeh.servicebus.windows.net/", "RootManageSharedAccessKey", "QwlP0H6LF/WsT/D3lKzE9Juw66cbYssxWpqMDNDAmPk=");
            Console.WriteLine(sasToken);
        }

        // Create REST request and append the token to ‘Authorization’ header . . . 

        /// <summary> 
        /// Code  for generating of SAS token for authorization with Service Bus 
        /// </summary> 
        /// <param name="resourceUri"></param> 
        /// <param name="keyName"></param> 
        /// <param name="key"></param> 
        /// <returns></returns> 
        private static string createToken(string resourceUri, string keyName, string key)
        {
            TimeSpan sinceEpoch = DateTime.UtcNow - new DateTime(1970, 1, 1);
            var expiry = Convert.ToString((int)sinceEpoch.TotalSeconds + (3600 * 24 * 365)); //EXPIRES in 1h (3600 secs) * 24 * 365 = 365 days 

            string stringToSign = HttpUtility.UrlEncode(resourceUri) + "\n" + expiry;
            HMACSHA256 hmac = new HMACSHA256(Encoding.UTF8.GetBytes(key));

            var signature = Convert.ToBase64String(hmac.ComputeHash(Encoding.UTF8.GetBytes(stringToSign)));
            var sasToken = String.Format(CultureInfo.InvariantCulture,
                "SharedAccessSignature sr={0}&sig={1}&se={2}&skn={3}",
                HttpUtility.UrlEncode(resourceUri), HttpUtility.UrlEncode(signature), expiry, keyName);

            return sasToken;
        }
    }
}
