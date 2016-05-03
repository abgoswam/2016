using System;
using System.Collections.Generic;
using System.Linq;
using System.Security.Permissions;
using System.Text;
using System.Threading.Tasks;
using Newtonsoft.Json;

namespace constructJson
{
    public class Categorical
    {
        public string Name;
        public string Value;
    }

    public class Numerical
    {
        public string Name;
        public double Value;
    }
    public class IpAddr
    {
        public string Name;
        public string Value;
    }
    public class GeoLoc
    {
        public string Name;
        public string Latitude;
        public string Longitude;
    }

    public class Entity
    {
        public string Id;
    }

    public class LogEntry
    {
        public long Unixtimestamp;
        public List<Entity> Entities;
        public List<Categorical> CategoricalEntries;
        public List<Numerical> NumericalEntries;
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
                Entities = new List<Entity>(),
                CategoricalEntries = new List<Categorical>(),
                NumericalEntries = new List<Numerical>(),
                GeoLocations = new List<GeoLoc>(),
            };
            entryKdd.Entities.Add(new Entity() { Id = "eid1" });
            entryKdd.Entities.Add(new Entity() { Id = "math" });
            entryKdd.Entities.Add(new Entity() { Id = "computerscience" });

            entryKdd.CategoricalEntries.Add(new Categorical()
            {
                Name = "course",
                Value = "math",
            });
            entryKdd.CategoricalEntries.Add(new Categorical()
            {
                Name = "major",
                Value = "computerscience",
            });
            entryKdd.NumericalEntries.Add(new Numerical()
            {
                Name = "durationspentinmilliseconds",
                Value = 40,
            });
            entryKdd.GeoLocations.Add(new GeoLoc()
            {
                Name = "location",
                Latitude = "0.34.5N",
                Longitude = "3.456S"
            });

            string entryKDDJson = JsonConvert.SerializeObject(entryKdd);
            Console.WriteLine(entryKDDJson);

            Console.WriteLine("-----------------");

            var entryVMob = new LogEntry()
            {
                Unixtimestamp = 14593556,
                Entities = new List<Entity>(),
                CategoricalEntries = new List<Categorical>(),
                NumericalEntries = new List<Numerical>(),
                IpAddresses = new List<IpAddr>(),
                Text = "ith entry"
            };
            entryVMob.Entities.Add(new Entity() { Id = "5379604408" });
            entryVMob.Entities.Add(new Entity() { Id = "Store1" });
            entryVMob.Entities.Add(new Entity() { Id = "Burger" });

            entryVMob.CategoricalEntries.Add(new Categorical()
            {
                Name = "storeid",
                Value = "Store1",
            });
            entryVMob.CategoricalEntries.Add(new Categorical()
            {
                Name = "couponused",
                Value = "yes",
            });
            entryVMob.CategoricalEntries.Add(new Categorical()
            {
                Name = "itembought",
                Value = "Burger",
            });
            entryVMob.NumericalEntries.Add(new Numerical()
            {
                Name = "numberofunits",
                Value = 5,
            });
            entryVMob.NumericalEntries.Add(new Numerical()
            {
                Name = "totalprice",
                Value = 20,
            });
            entryVMob.IpAddresses.Add(new IpAddr()
            {
                Name = "ipaddress",
                Value = "10.30.40.1",
            });

            string entryVMobJson = JsonConvert.SerializeObject(entryVMob);
            Console.WriteLine(entryVMobJson);

            //string provider1log = "{\"Entityid\":\"eid1\",\"Unixtimestamp\":14593556,\"CategoricalEntries\":[{\"Name\":\"course\",\"Value\":\"math\"},{\"Name\":\"major\",\"Value\":\"computerscience\"}],\"NumericalEntries\":[{\"Name\":\"durationspentinmilliseconds\",\"Value\":40.0}]}";
            //string provider2log = "{\"Entityid\":\"5379604408\",\"Unixtimestamp\":14593556,\"CategoricalEntries\":[{\"Name\":\"storeid\",\"Value\":\"Store1\"},{\"Name\":\"couponused\",\"Value\":\"yes\"},{\"Name\":\"itembought\",\"Value\":\"Burger\"}],\"NumericalEntries\":[{\"Name\":\"numberofunits\",\"Value\":5.0},{\"Name\":\"totalprice\",\"Value\":20.0}],\"IpAddresses\":[{\"Name\":\"ipaddress\",\"Value\":\"10.30.40.1\"}]}";

            string provider1log = "{\"Unixtimestamp\":14593556,\"Entities\":[{\"Id\":\"eid1\"},{\"Id\":\"math\"},{\"Id\":\"computerscience\"}],\"CategoricalEntries\":[{\"Name\":\"course\",\"Value\":\"math\"},{\"Name\":\"major\",\"Value\":\"computerscience\"}],\"NumericalEntries\":[{\"Name\":\"durationspentinmilliseconds\",\"Value\":40.0}],\"GeoLocations\":[{\"Name\":\"location\",\"Latitude\":\"0.34.5N\",\"Longitude\":\"3.456S\"}]}";
            string provider2log = "{\"Unixtimestamp\":14593556,\"Entities\":[{\"Id\":\"5379604408\"},{\"Id\":\"Store1\"},{\"Id\":\"Burger\"}],\"CategoricalEntries\":[{\"Name\":\"storeid\",\"Value\":\"Store1\"},{\"Name\":\"couponused\",\"Value\":\"yes\"},{\"Name\":\"itembought\",\"Value\":\"Burger\"}],\"NumericalEntries\":[{\"Name\":\"numberofunits\",\"Value\":5.0},{\"Name\":\"totalprice\",\"Value\":20.0}],\"IpAddresses\":[{\"Name\":\"ipaddress\",\"Value\":\"10.30.40.1\"}],\"Text\":\"ith entry\"}";

            var provider1LogEntry = JsonConvert.DeserializeObject<LogEntry>(provider1log);
            var provider2LogEntry = JsonConvert.DeserializeObject<LogEntry>(provider2log);
        }
    }
}
