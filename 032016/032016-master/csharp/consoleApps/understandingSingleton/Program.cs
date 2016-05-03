using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading;
using System.Threading.Tasks;

namespace understandingSingleton
{
    class Program
    {
        static void Main(string[] args)
        {
            Thread thread1 = new Thread(new ThreadStart(Go));
            Thread thread2 = new Thread(new ThreadStart(Go));
            
            thread1.Start();
            Thread.Sleep(20);
            thread2.Start();
            
            thread1.Join();
            thread2.Join();
        }

        static void Go()
        {
            var uniqR = Singleton.Instance.GetStartTime();

            Console.WriteLine("{0}:{1}. Unique Random : {2}", 
                (int)AppDomain.GetCurrentThreadId(), 
                Thread.CurrentThread.ManagedThreadId,
                uniqR.ToString("MM/dd/yyyy hh:mm:ss.fff tt"));
        }
    }

    // Bad code! Do not use!
    // The sealed keyword enables you to prevent the inheritance of a class or certain class members that were previously marked virtual.
    public sealed class Singleton
    {
        private static Singleton instance = null;
        private static readonly object padlock = new object();

        private DateTime startTime;

        private Singleton()
        {
            startTime = DateTime.Now;
            var _r = new Random();
            var uniq = _r.Next();

            Console.WriteLine("{0}:{1}. Inside Singleton : {2}. {3}", 
                (int)AppDomain.GetCurrentThreadId(), 
                Thread.CurrentThread.ManagedThreadId,
                startTime.ToString("MM/dd/yyyy hh:mm:ss.fff tt"), uniq);
        }

        public static Singleton Instance
        {
            get
            {
                lock (padlock)
                {
                    if (instance == null)
                    {
                        var s = new Singleton();
                        Thread.Sleep(1000);
                        instance = s;
                    }
                    return instance;
                }
            }
        }

        public DateTime GetStartTime()
        {
            return startTime;
        }
    }

    //public sealed class Singleton
    //{
    //    private static Singleton instance = null;
    //    private static readonly object padlock = new object();

    //    Singleton()
    //    {
    //    }

    //    public static Singleton Instance
    //    {
    //        get
    //        {
    //            lock (padlock)
    //            {
    //                if (instance == null)
    //                {
    //                    instance = new Singleton();
    //                }
    //                return instance;
    //            }
    //        }
    //    }
    //}


}
