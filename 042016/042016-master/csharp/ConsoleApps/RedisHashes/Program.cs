using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using StackExchange.Redis;

namespace RedisHashes
{
    public class MyObject
    {
        public long Id { get; set; }
        public string Name { get; set; }
        public Address ObjectAdress { get; set; }
    }
    public class Address
    {
        public string StreetAddress { get; set; }
        public string ZipCode { get; set; }
    }

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

            var storedObject = new MyObject();
            storedObject.Id = db.StringIncrement("UniqueUserId"); // Fetch unique id for object
            storedObject.Name = "Test Object";
            storedObject.ObjectAdress = new Address() { StreetAddress = "Test Avenue 2", ZipCode = "00100" };

            // Store object
            var propertyList = ConvertToHashEntryList(storedObject); 
            db.HashSet("user:" + storedObject.Id, propertyList.ToArray());

            // Fetch object
            var readObject = new MyObject();
            readObject.ObjectAdress = new Address();
            var hashEntries = db.HashGetAll("user:" + storedObject.Id);

            // Map HashEntries into object
            // For simplicity I just manually read values from collection with matching names
            readObject.Id = (long)hashEntries.Where(entry => entry.Name == "Id").First().Value;
            readObject.Name = hashEntries.Where(entry => entry.Name == "Name").First().Value;
            readObject.ObjectAdress.StreetAddress = hashEntries.Where(entry => entry.Name == "StreetAddress").First().Value;
            readObject.ObjectAdress.ZipCode = hashEntries.Where(entry => entry.Name == "ZipCode").First().Value;

            db.HashSet("user:1", new[] { new HashEntry("ZipCode", "00200") });
        }

        /// <summary>
        /// Example method for converting instance into hashentry list with reflection
        /// Use library (like FastMember) for this kind of mapping
        /// </summary>
        /// <param name="instance"></param>
        /// <returns></returns>
        private static List<HashEntry> ConvertToHashEntryList(object instance)
        {
            var propertiesInHashEntryList = new List<HashEntry>();
            foreach (var property in instance.GetType().GetProperties())
            {
                if (!property.Name.Equals("ObjectAdress"))
                {
                    // This is just for an example
                    propertiesInHashEntryList.Add(new HashEntry(property.Name, instance.GetType().GetProperty(property.Name).GetValue(instance).ToString()));
                }
                else
                {
                    var subPropertyList = ConvertToHashEntryList(instance.GetType().GetProperty(property.Name).GetValue(instance));
                    propertiesInHashEntryList.AddRange(subPropertyList);
                }
            }
            return propertiesInHashEntryList;
        } 

    }
}
