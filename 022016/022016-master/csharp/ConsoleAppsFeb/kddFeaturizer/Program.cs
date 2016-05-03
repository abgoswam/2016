using System;
using System.CodeDom;
using System.Collections.Generic;
using System.IO;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace kddFeaturizer
{
    class Eid
    {
        public long oldestTimestamp { get; set; }
        public long mostRecentTimestamp { get; set; }
        public int frequency { get; set; }

        public int[] cidbins;
        public int[] srcevtbins;
        public int[] catbins;
        public int[] objbins;

        public Eid(int n)
        {
            cidbins = new int[n];
            srcevtbins = new int[n];
            catbins = new int[n];
            objbins = new int[n];
        }
    }


    class Program
    {
        static void Main(string[] args)
        {
            int N = 20;
            var eidFeatures = new Dictionary<string, Eid>();
            
            using (StreamReader reader = new StreamReader(@"E:\hackerreborn\012016\_resources\kddcup\JoinedLogs_Traintest.tsv"))
            {
                string line;
                line = reader.ReadLine(); // header

                int k = 0;
                while ((line = reader.ReadLine()) != null)
                {
                    //Console.WriteLine(line); // Write to console.

                    if (k++%1000000 == 0)
                    {
                        Console.WriteLine(k);
                    }
                    
                    var tokens = line.Split('\t');

                    var eid = tokens[0];
                    var cid = tokens[1];
                    var timestamp = long.Parse(tokens[3]);
                    var srcevt = tokens[4];
                    var cat = tokens[5];
                    var obj = tokens[6];

                    var cidHash = Mod(cid.GetHashCode(), N);
                    var srcevtHash = Mod(srcevt.GetHashCode(), N);
                    var catHash = Mod(cat.GetHashCode(), N);
                    var objHash = Mod(obj.GetHashCode(), N);

                    if (!eidFeatures.ContainsKey(eid))
                    {
                        var nEid = new Eid(N)
                        {
                            oldestTimestamp = timestamp,
                            mostRecentTimestamp = timestamp,
                            frequency = 1,
                        };

                        nEid.cidbins[cidHash] = 1;
                        nEid.srcevtbins[srcevtHash] = 1;
                        nEid.catbins[catHash] = 1;
                        nEid.objbins[objHash] = 1;

                        eidFeatures.Add(eid, nEid);
                    }
                    else
                    {
                        var eEid = eidFeatures[eid];
                        if (timestamp < eidFeatures[eid].oldestTimestamp)
                        {
                            eEid.oldestTimestamp = timestamp;
                        }
                        else if (timestamp > eidFeatures[eid].mostRecentTimestamp)
                        {
                            eEid.mostRecentTimestamp = timestamp;
                        }

                        eEid.frequency++;
                        eEid.cidbins[cidHash]++;
                        eEid.srcevtbins[srcevtHash]++;
                        eEid.catbins[catHash]++;
                        eEid.objbins[objHash]++;
                    }
                }

                using (StreamWriter sw = new StreamWriter("streamingFeaturesCSharp.csv"))
                {
                    var sb = new StringBuilder();
                    sb.Append("eid,oldesttimestamp,mostrecenttimestamp,frequency,");

                    var cidfeatures = new List<string>();
                    var srcevtfeatures = new List<string>();
                    var catfeatures = new List<string>();
                    var objfeatures = new List<string>();
                    for (int i = 0; i < N; i++)
                    {
                        cidfeatures.Add(string.Format("cid{0}", i));
                        srcevtfeatures.Add(string.Format("serevt{0}", i));
                        catfeatures.Add(string.Format("cat{0}", i));
                        objfeatures.Add(string.Format("obj{0}", i));
                    }

                    sb.Append(string.Join(",", cidfeatures)).Append(',')
                            .Append(string.Join(",", srcevtfeatures)).Append(',')
                            .Append(string.Join(",", catfeatures)).Append(',')
                            .Append(string.Join(",", objfeatures));

                    //header
                    sw.WriteLine(sb.ToString());

                    foreach (var kv in eidFeatures)
                    {
                        sb = new StringBuilder();

                        var eid = kv.Key;
                        var features = kv.Value;

                        sb.Append(eid).Append(',');
                        sb.Append(features.oldestTimestamp).Append(',')
                            .Append(features.mostRecentTimestamp).Append(',')
                            .Append(features.frequency).Append(',')
                            .Append(string.Join(",", features.cidbins)).Append(',')
                            .Append(string.Join(",", features.srcevtbins)).Append(',')
                            .Append(string.Join(",", features.catbins)).Append(',')
                            .Append(string.Join(",", features.objbins));


                        sw.WriteLine(sb.ToString());

                    }
                }
            }
        }

        static int Mod(int x, int m)
        {
            int r = x % m;
            return r < 0 ? r + m : r;
        }

    }
}
