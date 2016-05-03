using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace understandingStatic
{
    static class CompanyEmployee
    {
        // public int myNumber; // not allowed
 
        public static void DoSomething()
        {
            /*...*/
            Console.WriteLine("Inside 'DoSomething'");
        }

        public static void DoSomethingElse()
        {
            /*...*/
            Console.WriteLine("Inside 'DoSomethingElse'");
        }
    }
    public class MyBaseC
    {
        public struct MyStruct
        {
            public static int x = 1100;
        }
    }

    public class Increment
    {
        public int GetRandonIncrement()
        {
            var r = new Random();
            return r.Next(10);
        }
    }

    public class Employee4
    {
        public string id;
        public string name;

        public Employee4()
        {
        }

        public Employee4(string name, string id)
        {
            this.name = name;
            this.id = id;
        }

        public static int employeeCounter;

        public static int AddEmployee()
        {
            var incr = new Increment();
            employeeCounter += incr.GetRandonIncrement();
            return employeeCounter;
        }
    }

    class Test
    {
        public static int x = y;
        public static int y = 5;
    }

    class Program
    {
        static void Main(string[] args)
        {
            CompanyEmployee.DoSomething();
            CompanyEmployee.DoSomethingElse();
            Console.WriteLine(MyBaseC.MyStruct.x);

            // -----------------------
            Console.Write("Enter the employee's name: "); string name = Console.ReadLine();
            Console.Write("Enter the employee's ID: "); string id = Console.ReadLine();

            // Create and configure the employee object:
            Employee4 e = new Employee4(name, id);
            Console.Write("Enter the current number of employees: "); string n = Console.ReadLine();
            Employee4.employeeCounter = Int32.Parse(n);
            Employee4.AddEmployee();

            // Display the new information:
            Console.WriteLine("Name: {0}", e.name);
            Console.WriteLine("ID:   {0}", e.id);
            Console.WriteLine("New Number of Employees: {0}", Employee4.employeeCounter);

            // ----------------------
            Console.WriteLine(Test.x);
            Console.WriteLine(Test.y);

            Test.x = 99;
            Console.WriteLine(Test.x);

        }
    }
}
