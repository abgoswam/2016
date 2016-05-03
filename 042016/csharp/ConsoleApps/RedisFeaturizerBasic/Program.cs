using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using StackExchange.Redis;

namespace RedisFeaturizerBasic
{
    class Program
    {
        static void Main(string[] args)
        {
            string entityid = "UserX";

            var azureConnectionString = string.Format("{0}:{1},ssl=true,password={2}",
                        "simplexagredistrial.redis.cache.windows.net",
                        6380,
                        "m4JD03/PtZjrZ6rXzQ5wHY44WZHpfj2KzJr+AtMXhi4=");

            var connectionMultiplexer = ConnectionMultiplexer.Connect(azureConnectionString);
            var db = connectionMultiplexer.GetDatabase();

            /*
             * Keys that are used in Redis.
             */

            // Keys : Recency
            var keyRecencyMin = string.Format("{0}_RecencyMin", entityid);
            var keyRecencyMax = string.Format("{0}_RecencyMax", entityid);

            // Keys : Frequency
            var keyFrequencyCount = string.Format("{0}_FrequencyCount", entityid);

            // Keys : Monetary Value
            var keyMonetaryValue = string.Format("{0}_MonetaryValue", entityid);

            // Keys : Unique hours, days, weeks
            var keyUniqueHours = string.Format("{0}_UniqueHours", entityid);
            var keyUniqueDays = string.Format("{0}_UniqueDays", entityid);
            var keyUniqueWeeks = string.Format("{0}_UniqueWeeks", entityid); 

            /*
             * Feature updates.
             */
            // Features : Recency
            long timestamp = 211114110;

            long valRecencyMin = (long) db.StringGet(keyRecencyMin);
            long valRecencyMax = (long) db.StringGet(keyRecencyMax);
            if (valRecencyMin ==0 || valRecencyMax == 0)
            {
                db.StringSet(keyRecencyMin, timestamp);
                db.StringSet(keyRecencyMax, timestamp);
            }
            else
            {
                if (timestamp < valRecencyMin)
                {
                    db.StringSet(keyRecencyMin, timestamp);
                }
                else if (timestamp > valRecencyMax)
                {
                    db.StringSet(keyRecencyMax, timestamp);
                }
            }

            // Features : Frequency
            db.StringIncrement(keyFrequencyCount);

            // Features : Monetary Value
            double monetaryValue = 0.25;
            db.StringIncrement(keyMonetaryValue, monetaryValue);

            // Features : unique days, weeks, months
            int valUniqueHour   = (int) timestamp /3600;
            int valUniqueDay    = valUniqueHour / 24;
            int valUniqueWeek  = valUniqueDay / 7;
            db.SetAdd(keyUniqueHours, valUniqueHour);
            db.SetAdd(keyUniqueDays, valUniqueDay);
            db.SetAdd(keyUniqueWeeks, valUniqueWeek);
        }
    }
}
