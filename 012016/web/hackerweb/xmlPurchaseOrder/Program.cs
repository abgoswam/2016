using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using System.Xml.Linq;

namespace xmlPurchaseOrder
{
    class Program
    {
        static void Main(string[] args)
        {
            XDocument purchaseOrder = XDocument.Load(@"F:\aghackerreborn\012016\resources\PurchaseOrder.xml");

            // Trying to get the part numbers from this document.
            IEnumerable<string> partNos =
                from item in purchaseOrder.Descendants("Item") 
                select (string) item.Attribute("PartNumber");

            Console.WriteLine("Part Numbers:");
            foreach (var item in partNos)
            {
                Console.WriteLine(item);
            }

            // As another example, you might want a list, sorted by part number, of the items with a value greater than $100. 
            // To obtain this information, you could run the following query:

            IEnumerable<XElement> partNosFiltered =
                from item in purchaseOrder.Descendants("Item")
                where (int)item.Element("Quantity") * (decimal)item.Element("USPrice") > 100
                orderby (string)item.Element("PartNumber")
                select item;

            purchaseOrder.Element("PurchaseOrder").Add(new XElement("NewChild", "new content"));


            XElement contacts =
                new XElement("Contacts",
                    new XElement("Contact",
                        new XElement("Name", "Patrick Hines"),
                        new XElement("Phone", "206-555-0144", new XAttribute("Type", "Home")),
                        new XElement("phone", "425-555-0145", new XAttribute("Type", "Work")),
                        new XElement("Address",
                            new XElement("Street1", "123 Main St"),
                            new XElement("City", "Mercer Island"),
                            new XElement("State", "WA"),
                            new XElement("Postal", "68042")
                        )
                    )
                );
            purchaseOrder.Element("PurchaseOrder").Add(contacts);

            Console.WriteLine(purchaseOrder);
            purchaseOrder.Save(@"F:\aghackerreborn\012016\resources\PurchaseOrderModified.xml");
        }
    }
}
