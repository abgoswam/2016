using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace understandingGenerics
{
    // type parameter T in angle brackets
    public class GenericList<T>
    {
        // The nested class is also generic on T.
        private class Node
        {
            // T used in non-generic constructor.
            public Node(T t)
            {
                next = null;
                data = t;
            }

            private Node next;
            public Node Next
            {
                get { return next; }
                set { next = value; }
            }

            // T as private member data type.
            private T data;

            // T as return type of property.
            public T Data
            {
                get { return data; }
                set { data = value; }
            }
        }

        private Node head;

        // constructor
        public GenericList()
        {
            head = null;
        }

        // T as method parameter type:
        public void AddHead(T t)
        {
            Node n = new Node(t);
            n.Next = head;
            head = n;
        }

        public IEnumerator<T> GetEnumerator()
        {
            Node current = head;

            while (current != null)
            {
                yield return current.Data;
                current = current.Next;
            }
        }
    }

    class TestGenericList
    {
        static void Main()
        {
            // int is the type argument
            GenericList<char> list = new GenericList<char>();

            for (char x = 'a'; x <= 'z'; x++)
            {
                list.AddHead(x);
            }

            foreach (char i in list)
            {
                System.Console.Write(i + " ");
            }
            System.Console.WriteLine("\nDone");
        }
    }

    ////Example #1
    //public class GenericList<T>
    //{
    //    void Add(T input) { }
    //}

    //class Program
    //{
    //    private class ExampleClass { }

    //    static void Main(string[] args)
    //    {
    //        // Declare a list of type int.
    //        GenericList<int> list1 = new GenericList<int>();

    //        // Declare a list of type string.
    //        GenericList<string> list2 = new GenericList<string>();

    //        // Declare a list of type ExampleClass.
    //        GenericList<ExampleClass> list3 = new GenericList<ExampleClass>();
    //    }
    //}
}
