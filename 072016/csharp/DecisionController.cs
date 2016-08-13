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

namespace EventFeaturizer.Controllers
{
    public class DecisionController : ApiController
    {
        public async Task<IHttpActionResult> GetDecision()
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
                foreach (var f in features)
                {
                    // build the input for decision service with: 
                    // f["action"]
                    // f["features"]["count"]
                    // f["features"]["sum"]
                    // calculate RPC and other ratio features here, or add them inside GetFeaturesAsync())
                }

                // Prepare the context to send to MWT Decision Service.
                var decisionInfo = JsonConvert.DeserializeObject<TRDecisionBody>(trPilot3DecisionBody);
                var multiActions = new List<Multi>();
                Random r = new Random();

                // Prepare the action-dependent features to pass in the context
                foreach (var eligible_action in decisionInfo.eligible_actions)
                {
                    multiActions.Add(new Multi()
                    {
                        Name = eligible_action,
                        RPC = r.NextDouble(),
                    });
                }
                var decisionContext = new DecisionContext()
                {
                    // shared features.
                    camp_id         = decisionInfo.camp_id,
                    on_wifi         = decisionInfo.on_wifi,
                    device_type     = decisionInfo.device_type,
                    display_size    = decisionInfo.display_size,
                    resolution      = decisionInfo.resolution,
                    data_speed      = decisionInfo.data_speed,
                    carrier         = decisionInfo.carrier,
                    country_code    = decisionInfo.country_code,
                    click_isp       = decisionInfo.click_isp,

                    // action-dependent features
                    _multi = multiActions
                };

                // Posting context to MWT Decision Service.
                string baseUrl = "https://mc-52piqtlyyp2sweggyhpqzzt5o2.azurewebsites.net";
                string uri = string.Format(CultureInfo.InvariantCulture, "{0}/API/Ranker", baseUrl);

                var httpClient = new HttpClient();
                httpClient.DefaultRequestHeaders.Add("auth", "evel6qo3vcm5y");
                var response = await httpClient.PostAsJsonAsync(uri, decisionContext).ConfigureAwait(false);

                if (response.IsSuccessStatusCode)
                {
                    // Update DocDB with response from the MWT Decision Service.
                    string result = await response.Content.ReadAsStringAsync();
                    var decisionResponse = JsonConvert.DeserializeObject<DecisionResponse>(result);

                    int bestAction = decisionResponse.Actions[0];
                    string event_id = decisionResponse.EventId;
                    await FeaturizerLibrary.DocDb.Featurizer.SaveContextAsync(trPilot3DecisionBody, bestAction.ToString(), event_id).ConfigureAwait(false);
                }

                return ResponseMessage(response);
            }
            catch(Exception e)
            {
                ErrorResponse errMsg = new ErrorResponse()
                {
                    Message = "Exception",
                    MessageDetail = e.Message
                };

                HttpResponseMessage rsp = Request.CreateResponse(HttpStatusCode.BadRequest, errMsg);
                return ResponseMessage(rsp);
            }
        }
    }
}
