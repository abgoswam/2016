using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using System.Configuration;
using System.IO;
using StackExchange.Redis;

namespace insertRedis
{
    class Program
    {
        private static Lazy<ConnectionMultiplexer> lazyConnection = new Lazy<ConnectionMultiplexer>(() =>
        {
            // Replace these values with the values from your Azure Redis Cache instance.
            // For more information, see http://aka.ms/ConnectToTheAzureRedisCache
            string redisCacheName = ConfigurationManager.AppSettings["redisCacheName"];
            string redisCachePassword = ConfigurationManager.AppSettings["redisCachePassword"];
            return ConnectionMultiplexer.Connect(redisCacheName + ",abortConnect=false,ssl=true,password=" + redisCachePassword);
        });

        public static ConnectionMultiplexer Connection
        {
            get
            {
                return lazyConnection.Value;
            }
        }

        static int Mod(int x, int m)
        {
            int r = x % m;
            return r < 0 ? r + m : r;
        }

        private static void Main(string[] args)
        {
            string redisCacheName = ConfigurationManager.AppSettings["redisCacheName"];
            string redisCachePassword = ConfigurationManager.AppSettings["redisCachePassword"];

            if (string.IsNullOrWhiteSpace(redisCacheName) || string.IsNullOrWhiteSpace(redisCachePassword) ||
                redisCacheName.StartsWith("TODO") || redisCachePassword.StartsWith("TODO"))
            {

                Console.WriteLine("Please update your Redis Cache credentials in App.config");
                Console.ReadKey();
                return;
            }

            // 1. Get a reference to your Azure Redis Cache.
            //    Azure Redis Cache instances have a default of 16 databases,
            //    numbered 0-15, with 0 being the default database if none
            //    is specified. These databases share the memory of the cache.
            //    For more information, see http://aka.ms/ConfigureAzureRedisCache  
            Console.WriteLine("1. Get a reference to the redis cache database");
            IDatabase cache = Connection.GetDatabase();


            int N = 20;
            using (
                StreamReader reader =
                    new StreamReader(@"E:\hackerreborn\012016\_resources\kddcup\JoinedLogs_Traintest_Sample1K.tsv"))
            {
                string line;
                line = reader.ReadLine(); // header

                int k = 0;
                while ((line = reader.ReadLine()) != null)
                {
                    //Console.WriteLine(line); // Write to console.

                    Console.WriteLine(k++);

                    var tokens = line.Split('\t');
                    var eid = tokens[0];
                    var cid = tokens[1];
                    var timestamp = long.Parse(tokens[3]);
                    var srcevt = tokens[4];
                    var cat = tokens[5];
                    var obj = tokens[6];

                    var cidHash = Mod(cid.GetHashCode(), N);
                    var srcevtHash = Mod(srcevt.GetHashCode(), N);
                    var catHash = Mod(cat.GetHashCode(), N);
                    var objHash = Mod(obj.GetHashCode(), N);

                    var keyoldesttimestamp = eid + "_oldesttimestamp";
                    var keylatesttimestamp = eid + "_latesttimestamp";
                    var keyfrequency = eid + "_frequency";
                    var keycidhash = eid + "_cidhash_" + cidHash.ToString();
                    var keysrcevthash = eid + "_srcevthash_" + srcevtHash.ToString();
                    var keycathash = eid + "_cathash_" + catHash.ToString();
                    var keyobjhash = eid + "_objhash_" + objHash.ToString();

                    var valoldesttimestamp = cache.StringGet(keyoldesttimestamp);
                    var vallatesttimestamp = cache.StringGet(keylatesttimestamp);

                    //Console.WriteLine("{0},{1},{2},{3},{4}", timestamp, keyoldesttimestamp, keylatesttimestamp, valoldesttimestamp, vallatesttimestamp);

                    //Recency
                    if (string.IsNullOrEmpty(valoldesttimestamp) || string.IsNullOrEmpty(vallatesttimestamp))
                    {
                        cache.StringSet(keyoldesttimestamp, timestamp);
                        cache.StringSet(keylatesttimestamp, timestamp);
                    }
                    else
                    {
                        if (timestamp < (long)valoldesttimestamp)
                        {
                            cache.StringSet(keyoldesttimestamp, timestamp);
                        }
                        else if (timestamp > (long)vallatesttimestamp)
                        {
                            cache.StringSet(keylatesttimestamp, timestamp);
                        }
                    }

                    //Frequency
                    cache.StringIncrement(keyfrequency, 1);

                    //Monetary Value
                    cache.StringIncrement(keycidhash, 1);
                    cache.StringIncrement(keysrcevthash, 1);
                    cache.StringIncrement(keycathash, 1);
                    cache.StringIncrement(keyobjhash, 1);
                }
            }
        }
    }
}
