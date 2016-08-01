using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace multidimensionalarrays
{
    class Program
    {
        static void Main(string[] args)
        {
            // One-Dimensional Array
            // https://msdn.microsoft.com/en-us/library/0a7fscd0.aspx

            // Method 1: No initialization
            int[] array = new int[5]; //This array contains the elements from array[0] to array[4]. The new operator is used to create the array and initialize the array elements to their default values.In this example, all the array elements are initialized to zero.
            foreach(var item in array)
            {
                Console.WriteLine(item);
            }

            // Method 2: With initialization
            int[] array1 = new int[] { 1, 3, 5, 7, 9 };
            foreach (var item in array1)
            {
                Console.WriteLine(item);
            }

            // Method 3: Initialization with shortcut.
            string[] weekDays2 = { "Sun", "Mon", "Tue", "Wed", "Thu", "Fri", "Sat" };
            foreach(var item in weekDays2)
            {
                Console.WriteLine(item);
            }

            // Two-dimensional array.
            // https://msdn.microsoft.com/en-us/library/2yd9wwz4.aspx

            int[,] array2D = new int[,] { { 1, 2 }, { 3, 4 }, { 5, 6 }, { 7, 8 } };
            // The same array with dimensions specified.
            int[,] array2Da = new int[4, 2] { { 1, 2 }, { 3, 4 }, { 5, 6 }, { 7, 8 } };

            // A similar array with string elements.
            string[,] array2Db = new string[3, 2] { { "one", "two" }, { "three", "four" },
                                        { "five", "six" } };

            // http://stackoverflow.com/questions/7202515/difference-between-array-getlength0-and-array-getupperbound0
            for (var i = 0; i < array2Da.GetLength(0); i++)
            {
                for (var j = 0; j < array2Da.GetLength(1); j++)
                {
                    Console.Write("{0} ", array2Da[i, j]);
                }
                Console.WriteLine();
            }
        }
    }
}
