using System;
using System.Collections.Generic;
using System.Diagnostics;
using System.IO;
using System.Linq;
using System.Net.Http;
using System.Web.Http;
using GenderApp.Controllers;
using Microsoft.Owin.Security.OAuth;
using Newtonsoft.Json.Serialization;

namespace GenderApp
{
    public static class WebApiConfig
    {
        public static List<string> wordsEn;
        public static List<string> dssmVocab;
        public static DNN src_dssm;
        public static DNN tgt_dssm;
        public static string maleSynonyms;
        public static string femaleSynonyms;

        public static void Register(HttpConfiguration config)
        {
            // Web API configuration and services
            // Configure Web API to use only bearer token authentication.
            config.SuppressDefaultHostAuthentication();
            config.Filters.Add(new HostAuthenticationFilter(OAuthDefaults.AuthenticationType));

            // Web API routes
            config.MapHttpAttributeRoutes();

            config.Routes.MapHttpRoute(
                name: "DefaultApi",
                routeTemplate: "api/{controller}/{id}",
                defaults: new { id = RouteParameter.Optional }
            );

            wordsEn = new List<string>();
            dssmVocab = new List<string>();

            using (var reader = new StreamReader(System.Web.HttpContext.Current.Server.MapPath("~/App_Data/wordsEn.txt")))
            {
                string line;
                while ((line = reader.ReadLine()) != null)
                {
                    wordsEn.Add(line.Trim());
                }
            }

            using (var reader = new StreamReader(System.Web.HttpContext.Current.Server.MapPath("~/App_Data/vocab")))
            {
                string line;
                while ((line = reader.ReadLine()) != null)
                {
                    var tokens = line.Split();
                    dssmVocab.Add(tokens[0]);
                }
            }

            int inSrcMaxRetainedSeqLength = 1;
            src_dssm = new DNN(
                System.Web.HttpContext.Current.Server.MapPath("~/App_Data/smodel"),
                ModelType.DSSM,
                System.Web.HttpContext.Current.Server.MapPath("~/App_Data/vocab"),
                inSrcMaxRetainedSeqLength);

            int inTgtMaxRetainedSeqLength = 1;
            tgt_dssm = new DNN(
                System.Web.HttpContext.Current.Server.MapPath("~/App_Data/tmodel"),
                ModelType.DSSM,
                System.Web.HttpContext.Current.Server.MapPath("~/App_Data/vocab"),
                inTgtMaxRetainedSeqLength);

            maleSynonyms = "male man men manly boy he masculine father brother buddy dude gentleman paternal person macho manliness manful king prince guy gent";
            femaleSynonyms = "female woman women girl she feminine mother sister gal womanly womanish maternal babe chick dame doll honey lady miss damsel maid maiden miss lady girlish queen princess";

            Debug.WriteLine("App Initialized.");
        }
    }
}
