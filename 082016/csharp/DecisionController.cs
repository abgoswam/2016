using System;
using System.Collections.Generic;
using System.Linq;
using System.Net;
using System.Text;
using System.Net.Http;
using System.Web.Http;
using System.Diagnostics;
using System.Threading.Tasks;
using Newtonsoft.Json;
using EventFeaturizer.Models;
using System.Globalization;
using Newtonsoft.Json.Linq;
using System.Net.Http.Formatting;

namespace EventFeaturizer.Controllers
{
    public class DecisionController : ApiController
    {
        public async Task<IHttpActionResult> PostDecision()
        {
            try
            {
                var authtoken = Request.Headers.SingleOrDefault(x => x.Key == "AuthorizationKey").Value.First();
                if (authtoken != "997e3f65-c772-4345-871d-249e178faef3")
                {
                    throw new UnauthorizedAccessException("Invalid AuthorizationKey");
                }

                var trPilot3DecisionBody = await Request.Content.ReadAsStringAsync().ConfigureAwait(false);

                // Get the ADFs from DocDB
                var features = await FeaturizerLibrary.DocDb.Featurizer.GetFeaturesAsync(trPilot3DecisionBody).ConfigureAwait(false);
                // convert features to dictionary for O(1) lookup of actions
                var adf = features.ToDictionary(f => f["action"].Value<string>(), f => f["features"]);

                // De-serialize JSON body in POST message.
                var decisionInfo = JsonConvert.DeserializeObject<TRDecisionBody>(trPilot3DecisionBody);

                HttpResponseMessage response = null;
                if ("rr" == decisionInfo.bucket.ToLower())
                {
                    var rnd = new Random();
                    var randomActionIndexList = Enumerable.Range(1, decisionInfo.eligible_actions.Count).OrderBy(item => rnd.Next()).ToList();

                    DecisionResponse randomDecisionResponse = new DecisionResponse()
                    {
                        EventId = Guid.NewGuid().ToString(),
                        Actions = randomActionIndexList,
                        ModelTime = DateTime.Now
                    };

                    var formatter = new JsonMediaTypeFormatter();
                    formatter.SerializerSettings.DateFormatHandling = DateFormatHandling.MicrosoftDateFormat;

                    response = Request.CreateResponse(HttpStatusCode.OK, randomDecisionResponse, formatter);
                }
                else if ("ex" == decisionInfo.bucket.ToLower())
                {
                    var multiActions = new List<Multi>();

                    // Prepare the action-dependent features to pass in the context
                    foreach (var eligible_action in decisionInfo.eligible_actions)
                    {
                        // default rpc for action that don't have features, based on smoothing parameters
                        var rpc = 0.0001f;
                        if (adf.ContainsKey(eligible_action))
                        {
                            rpc = adf[eligible_action]["rpc"].Value<float>();
                        }
                        else
                        {
                            // TODO: add server logging here, because this could mask underlying problems with docdb layer
                            // backlog: https://simplex-ads.visualstudio.com/User%20Modeling/_workitems?id=46
                        }

                        multiActions.Add(new Multi()
                        {
                            Name = eligible_action,
                            RPC = rpc,
                        });
                    }
                    var decisionContext = new DecisionContext()
                    {
                        // shared features.
                        camp_id = decisionInfo.camp_id,
                        on_wifi = decisionInfo.on_wifi,
                        device_type = decisionInfo.device_type,
                        display_size = decisionInfo.display_size,
                        resolution = decisionInfo.resolution,
                        data_speed = decisionInfo.data_speed,
                        carrier = decisionInfo.carrier,
                        country_code = decisionInfo.country_code,
                        click_isp = decisionInfo.click_isp,

                        // action-dependent features
                        _multi = multiActions
                    };

                    // Posting context to MWT Decision Service.
                    string baseUrl = "https://mc-7fldrt53lqfquvdmmudwbhyscg.azurewebsites.net";

                    string uri = string.Format(CultureInfo.InvariantCulture, "{0}/API/Ranker", baseUrl);

                    var httpClient = new HttpClient();
                    httpClient.DefaultRequestHeaders.Add("auth", "5vvzjbwmnpbmc");
                    response = await httpClient.PostAsJsonAsync(uri, decisionContext).ConfigureAwait(false);

                    if (response.IsSuccessStatusCode)
                    {
                        // Update DocDB with response from the MWT Decision Service.
                        string result = await response.Content.ReadAsStringAsync();
                        var decisionResponse = JsonConvert.DeserializeObject<DecisionResponse>(result);

                        int bestAction = decisionResponse.Actions[0];
                        string event_id = decisionResponse.EventId;
                        await FeaturizerLibrary.DocDb.Featurizer.PostDecisionAsync(trPilot3DecisionBody, bestAction.ToString(), event_id).ConfigureAwait(false);
                    }
                }
                else
                {
                    throw new InvalidOperationException("Invalid parameter value (bucket).");
                }

                return ResponseMessage(response);
            }
            catch (Exception e)
            {
                ErrorResponse errMsg = new ErrorResponse()
                {
                    Message = "Exception",
                    MessageDetail = e.Message,
                    StackTrace = e.StackTrace
                };

                HttpResponseMessage rsp = Request.CreateResponse(HttpStatusCode.BadRequest, errMsg);
                return ResponseMessage(rsp);
            }
        }
    }
}
