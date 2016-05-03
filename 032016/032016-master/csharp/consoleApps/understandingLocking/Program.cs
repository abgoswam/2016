using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Linq;
using System.Security.Cryptography.X509Certificates;
using System.Text;
using System.Threading;
using System.Threading.Tasks;

namespace understandingLocking
{
    internal class ForLocking
    {
    }

    internal class ForLockingUsingObject
    {
        public static readonly object LockObject;

        static ForLockingUsingObject()
        {
            LockObject = new object();
        }
    }

    public abstract class BaseClass<T>
    {
        private static T x;
        private static readonly object Padlock = new object();

        internal static class Dummy
        {
        }

        // keeping a public counter
        public static int count = 0;

        public void Foo(T update)
        {
            Console.WriteLine("Inside ' Foo'. typeof baseclass : {0}", typeof(BaseClass<T>));
            
            //lock (Padlock)
            //lock (typeof(ForLocking))
            lock (ForLockingUsingObject.LockObject)
             {
                x = update;

                for (int i = 0; i < 20; i ++)
                {
                    Console.WriteLine("{0}:{1}:{2}.", (int) AppDomain.GetCurrentThreadId(),
                        Thread.CurrentThread.ManagedThreadId, update);
                    Thread.Sleep(TimeSpan.FromSeconds(1));
                }
                count++;
             }
        }
    }

    public sealed class A : BaseClass<string>
    //public sealed class A : BaseClass<int>
    {
    }

    public sealed class B : BaseClass<int>
    {

    }

    class Program
    {
        static void Main(string[] args)
        {
            Thread thread1 = new Thread(new ThreadStart(UseA));
            Thread thread2 = new Thread(new ThreadStart(UseB));

            // Start 1st thread.
            thread1.Start();

            // Starting 2nd thread after 10 seconds.
            Thread.Sleep(TimeSpan.FromSeconds(10));
            thread2.Start();

            thread1.Join();
            thread2.Join();
        }

        static void UseA()
        {
            var objA = new A();

            objA.Foo("some string");
            // objA.Foo(20);

            Console.WriteLine("{0}:{1}. UseA : {2}.",
                (int)AppDomain.GetCurrentThreadId(),
                Thread.CurrentThread.ManagedThreadId,
                A.count);
        }
        static void UseB()
        {
            var objB = new B();
            objB.Foo(10);

            Console.WriteLine("{0}:{1}. UseB : {2}.",
                (int)AppDomain.GetCurrentThreadId(),
                Thread.CurrentThread.ManagedThreadId,
                B.count);
        }
    }
}
