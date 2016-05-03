using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using Newtonsoft.Json;

namespace constructJson2
{
    public class IpAddr
    {
        public string Address;
    }
    public class GeoLoc
    {
        public string Latitude;
        public string Longitude;
    }

    public class LogEntry
    {
        public long Unixtimestamp;
        public double Value;
        public Dictionary<string, string> Entities;
        public Dictionary<string, string> CategoricalEntries;
        public Dictionary<string, double> NumericalEntries;
        public List<IpAddr> IpAddresses;
        public List<GeoLoc> GeoLocations;
        public string Text;
    }

    class Program
    {
        static void Main(string[] args)
        {
            var entryKdd = new LogEntry()
            {
                Unixtimestamp = 14593556,
                Value = 100,
                Entities = new Dictionary<string, string>(),
                CategoricalEntries = new Dictionary<string, string>(),
                NumericalEntries = new Dictionary<string, double>(),
                GeoLocations = new List<GeoLoc>(),
            };
            
            entryKdd.Entities["userid"] = "eid1";
            entryKdd.Entities["courseid"] = "math";
            entryKdd.Entities["majorid"] = "computerscience";

            entryKdd.CategoricalEntries["course"] = "math";
            entryKdd.CategoricalEntries["major"] = "computerscience";

            entryKdd.NumericalEntries["durationspentinmilliseconds"] = 40;
            
            entryKdd.GeoLocations.Add(new GeoLoc()
            {
                Latitude = "0.34.5N",
                Longitude = "3.456S"
            });

            string entryKddJson = JsonConvert.SerializeObject(entryKdd);
            Console.WriteLine(entryKddJson);

            string log =
                "{\"Unixtimestamp\":14593556,\"Value\":100.0,\"Entities\":{\"userid\":\"eid1\",\"courseid\":\"math\",\"majorid\":\"computerscience\"},\"CategoricalEntries\":{\"course\":\"math\",\"major\":\"computerscience\"},\"NumericalEntries\":{\"durationspentinmilliseconds\":40.0},\"GeoLocations\":[{\"Latitude\":\"0.34.5N\",\"Longitude\":\"3.456S\"}]}";

            var logEntry = JsonConvert.DeserializeObject<LogEntry>(log);
            Console.WriteLine("-----------------");

            var entryVMob = new LogEntry()
            {
                Unixtimestamp = 14593556,
                Value = 30.5,
                Entities = new Dictionary<string, string>(),
                CategoricalEntries = new Dictionary<string, string>(),
                NumericalEntries = new Dictionary<string, double>(),
                IpAddresses = new List<IpAddr>(),
                Text = "ith entry"
            };


            entryVMob.Entities["userid"] = "5379604408";
            entryVMob.Entities["storeid"] = "Store1";
            entryVMob.Entities["itemid"] = "Burger";

            entryVMob.CategoricalEntries["storeid"] = "Store1";
            entryVMob.CategoricalEntries["couponused"] = "yes";
            entryVMob.CategoricalEntries["itembought"] = "Burger";

            entryVMob.NumericalEntries["numberofunits"] = 5;
            entryVMob.NumericalEntries["totalprice"] = 20;

            entryVMob.IpAddresses.Add(new IpAddr()
            {
                Address = "10.30.40.1",
            });

            string entryVMobJson = JsonConvert.SerializeObject(entryVMob);
            Console.WriteLine(entryVMobJson);

            string log2 = 
                "{\"Unixtimestamp\":14593556,\"Value\":30.5,\"Entities\":{\"userid\":\"5379604408\",\"storeid\":\"Store1\",\"itemid\":\"Burger\"},\"CategoricalEntries\":{\"storeid\":\"Store1\",\"couponused\":\"yes\",\"itembought\":\"Burger\"},\"NumericalEntries\":{\"numberofunits\":5.0,\"totalprice\":20.0},\"IpAddresses\":[{\"Address\":\"10.30.40.1\"}],\"Text\":\"ith entry\"}";
            var logEntry2 = JsonConvert.DeserializeObject<LogEntry>(log2);
            Console.WriteLine("-----------------");
        }
    }
}
