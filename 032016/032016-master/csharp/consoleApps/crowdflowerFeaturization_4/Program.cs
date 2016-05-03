using System;
using System.Collections.Generic;
using System.Diagnostics;
using System.IO;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace crowdflowerFeaturization_4
{
    class Program
    {
        static void Main(string[] args)
        {
            LaunchCommandLineApp();
        }

        /// <summary>
        /// Launch the legacy application with some options set.
        /// </summary>
        static void LaunchCommandLineApp()
        {
            // For the example
            const string ex1 = "C:\\";
            const string ex2 = "C:\\Dir";


            using (var sr = new StreamReader(@"E:\hackerreborn\032016\_resources\crowdflower4\train_map_scored3_filtered.csv"))
            using (var sw = new StreamWriter(@"E:\hackerreborn\032016\_resources\crowdflower4\train_map_scored4_filtered.csv"))
            {
                // read first line
                var line = sr.ReadLine();

                // write first line
                sw.WriteLine("url,cfTag,judgeRating,binaryLabel,catTop1,catTop2,catTop3,catTop4,catTop5,catAll,caption,a2vScore");

                int i = 0;
                while ((line = sr.ReadLine()) != null)
                {
                    Console.WriteLine(i++);
                    var tokens = line.Split(',');

                    var url             = tokens[0];
                    var cfTag           = tokens[1];
                    var judgeRating     = tokens[2];
                    var binaryLabel     = tokens[3];
                    var catTop1         = tokens[4];
                    var catTop2         = tokens[5];
                    var catTop3         = tokens[6];
                    var catTop4         = tokens[7];
                    var catTop5         = tokens[8];
                    var categoriesAll   = tokens[9];
                    var caption         = tokens[10];

                    // Use ProcessStartInfo class
                    ProcessStartInfo startInfo = new ProcessStartInfo();

                    startInfo.FileName = "F:\\Any2Vec\\bin\\Debug\\Demo.exe";

                    // startInfo.Arguments = "-f j -o \"" + ex1 + "\" -z 1.0 -s y " + ex2;
                    startInfo.Arguments = string.Format("similarity /m F:\\Any2Vec\\Model /i {0} /i \"{1}\"", url, cfTag);

                    startInfo.UseShellExecute = false;

                    startInfo.RedirectStandardOutput = true;

                    // startInfo.CreateNoWindow = false;
                    startInfo.CreateNoWindow = true;
                    
                    // startInfo.WindowStyle = ProcessWindowStyle.Hidden;

                    try
                    {
                        using (Process exeProcess = Process.Start(startInfo))
                        {
                            //exeProcess.WaitForExit();

                            while (!exeProcess.StandardOutput.EndOfStream)
                            {
                                string output = exeProcess.StandardOutput.ReadLine();

                                // do something with 
                                var scoring = output.Split();
                                var a2vScore = scoring[1].Trim();

                                sw.WriteLine("{0},{1},{2},{3},{4},{5},{6},{7},{8},{9},{10},{11}",
                                    url,
                                    cfTag,
                                    judgeRating,
                                    binaryLabel,
                                    catTop1,
                                    catTop2,
                                    catTop3,
                                    catTop4,
                                    catTop5,
                                    categoriesAll,
                                    caption,
                                    a2vScore
                                    );

                                sw.Flush();
                            }
                        }
                    }
                    catch
                    {
                        // Log error.
                    }
                }
            }
        }
    }
}
