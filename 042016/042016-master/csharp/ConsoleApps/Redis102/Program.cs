using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using Newtonsoft.Json;
using StackExchange.Redis;

namespace Redis102
{
    class Program
    {
        private static ConnectionMultiplexer connectionMultiplexer;
        private static IDatabase database;

        static void Main(string[] args)
        {
            Configure();

            bool stored = StoreData("MyKey", "my first cache string");
            if (stored)
            {
                var cachedData = GetData("MyKey");

                bool isIt = cachedData == "my first cache string";
            }

            var student1 = new Student()
            {
                FirstName = "abhishek",
                RollNumber = 101,
            };
            stored = Add("101", student1);
            if (stored)
            {
                var gotStudent1 = Get<Student>("101");
            }
        }

        private static void Configure()
        {
            ////use locally redis installation
            //var connectionString = string.Format("{0}:{1}", "127.0.0.1", 6379);

            //use azure redis installation
            var azureConnectionString = string.Format("{0}:{1},ssl=true,password={2}",
                                    "simplexagredistrial.redis.cache.windows.net",
                                    6380,
                                    "m4JD03/PtZjrZ6rXzQ5wHY44WZHpfj2KzJr+AtMXhi4=");

            connectionMultiplexer = ConnectionMultiplexer.Connect(azureConnectionString);
            database = connectionMultiplexer.GetDatabase();
        }

        private static bool StoreData(string key, string value)
        {
            return database.StringSet(key, value);
        }

        private static string GetData(string key)
        {
            return database.StringGet(key);
        }

        private static void DeleteData(string key)
        {
            database.KeyDelete(key);
        }

        //public bool Add<T>(string key, T value, DateTimeOffset expiresAt) where T : class
        public static bool Add<T>(string key, T value) where T : class
        {
            var serializedObject = JsonConvert.SerializeObject(value);
            //var expiration = expiresAt.Subtract(DateTimeOffset.Now);

            // return database.StringSet(key, serializedObject, expiration);
            return database.StringSet(key, serializedObject);
        }

        public static T Get<T>(string key) where T : class
        {
            var serializedObject = database.StringGet(key);
            return JsonConvert.DeserializeObject<T>(serializedObject);
        }
    }
}
