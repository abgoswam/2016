using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using StackExchange.Redis;

namespace RedisSets
{
    class Program
    {
        static void Main(string[] args)
        {
            var azureConnectionString = string.Format("{0}:{1},ssl=true,password={2}",
            "simplexagredistrial.redis.cache.windows.net",
            6380,
            "m4JD03/PtZjrZ6rXzQ5wHY44WZHpfj2KzJr+AtMXhi4=");

            var connectionMultiplexer = ConnectionMultiplexer.Connect(azureConnectionString);
            var db = connectionMultiplexer.GetDatabase();

            var trialMembers = new List<string>()
            {
                "member1",
                "member2",
                "member3",
                "member1"
            };

            var members = trialMembers.Select(value => (RedisValue)value).ToArray();
            db.SetAdd("uniquemembers", members);
            long x = db.SetLength("uniquemembers");
        }
    }
}
