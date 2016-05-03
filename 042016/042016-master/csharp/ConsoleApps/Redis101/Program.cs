using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using Newtonsoft.Json;
using StackExchange.Redis;

namespace Redis101
{
    class Employee
    {
        public int Id { get; set; }
        public string Name { get; set; }

        public Employee(int EmployeeId, string Name)
        {
            this.Id = EmployeeId;
            this.Name = Name;
        }
    }

    class Program
    {
        static void Main(string[] args)
        {
            var ConnectionTrialCache =
                ConnectionMultiplexer.Connect("simplexagredistrial.redis.cache.windows.net,abortConnect=false,ssl=true,password=m4JD03/PtZjrZ6rXzQ5wHY44WZHpfj2KzJr+AtMXhi4=");

            // Connection refers to a property that returns a ConnectionMultiplexer
            // as shown in the previous example.
            IDatabase cache = ConnectionTrialCache.GetDatabase();

            //// Perform cache operations using the cache object...
            // Simple put of integral data types into the cache
            cache.StringSet("key1", "value1");
            cache.StringSet("key2", 26);

            // Simple get of data types from the cache
            string key1 = cache.StringGet("key1");
            int key2 = (int)cache.StringGet("key2");

            // Store to cache
            cache.StringSet("e25", JsonConvert.SerializeObject(new Employee(25, "Clayton Gragg")));

            // Retrieve from cache
            Employee e25 = JsonConvert.DeserializeObject<Employee>(cache.StringGet("e25"));
        }
    }
}
