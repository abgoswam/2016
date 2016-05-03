using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using System.Threading;

namespace understandingThreading
{
    class Program
    {
        static bool done;
        static readonly object locker = new object();

        static void Main()
        {
            new Thread(Go).Start();
            Go();
        }

        // Note that Go is now an instance method
        static void Go()
        {
            lock (locker)
            {
                if (!done)
                {
                    Console.WriteLine("Done");
                    done = true;
                }
            }
        }

        ///// <summary>
        ///// Trial 1
        ///// </summary>
        ///// <param name="args"></param>
        //static void Main(string[] args)
        //{
        //    Thread t = new Thread(WriteY);          // Kick off a new thread
        //    t.Start();                               // running WriteY()

        //    // Simultaneously, do something on the main thread.
        //    for (int i = 0; i < 1000; i++)
        //    {
        //        Console.WriteLine("{0}:{1}:{2}. Inside 'main'", (int)AppDomain.GetCurrentThreadId(), Thread.CurrentThread.ManagedThreadId, Thread.CurrentThread.IsBackground);
        //    }
        //}

        //static void WriteY()
        //{
        //    for (int i = 0; i < 1000; i++)
        //    {
        //        Console.WriteLine("{0}:{1}:{2}. Inside 'WriteY'", (int)AppDomain.GetCurrentThreadId(), Thread.CurrentThread.ManagedThreadId, Thread.CurrentThread.IsBackground);
        //    }
        //}
    }
}
