# -*- coding: utf-8 -*-
"""
Created on Thu Aug 18 15:33:36 2016

@author: agoswami

This python module produces the IPS estimate for a policy, based on the input files.

Usage : python evaluator_ips.py [Observation File] [Scoring File]

The two input files [Observation File] [Scoring File] are described below : 

[Observation File] : 

- File containing 3 comma separated fields :  (action id), (reward), (probability)
- File should not contain header.

Example:
17,0,0.05
10,0,0.05


[Scoring File]

- File containing scored actions.
- Format is same as VW's -p output. The 'best action' selected by the policy is at the 0th index when we split the scored line by a ':'

Example:
13:1,7:0,9:0,8:0,0:0,12:0,16:0,6:0,3:0,15:0,18:0,5:0,11:0,14:0,1:0,2:0,4:0,10:0,17:0

17:1,7:0,9:0,8:0,0:0,12:0,16:0,6:0,3:0,15:0,18:0,5:0,11:0,14:0,1:0,2:0,4:0,10:0,13:0

"""

import sys
import math

if len(sys.argv) != 3:
    print "Error in passing arguments. example : python evaluator_ips.py [Observation File] [Scoring File]"
    sys.exit()

observation_filename = sys.argv[1]
scored_filename = sys.argv[2]
    
with open(observation_filename, 'rb') as f_obs, \
    open(scored_filename, "rb") as f_scored:
    
    obs_linesall            = f_obs.read().splitlines()
    scored_linesall         = f_scored.read().splitlines()
    obs_linesnonempty       = list(filter(lambda x: x.strip(), obs_linesall))
    scoring_linesnonempty   = list(filter(lambda x: x.strip(), scored_linesall))
    
#    validate number of non empty lines is same between observation and scoring
    if len(obs_linesnonempty) != len(scoring_linesnonempty):
        raise ValueError('Invalid number of lines between [Observation File] and [Scoring File].')
        
    total_observations = 0
    matching_observations = 0
    sum_ips = 0.0
    sum_ipssquared = 0.0
    
    for obs, scored in zip(obs_linesnonempty, scoring_linesnonempty):
        total_observations += 1
        
        obs_action, obs_reward, obs_probability = obs.strip().split(',')
        
        if (not obs_action) or (not obs_reward) or (not obs_probability):
            raise ValueError('Incorrect format in [Observation File]. observation line : ' + obs)
        
        if (float(obs_probability) <= 0) or (float(obs_probability) > 1.0):
            raise ValueError('Invalid probability [Observation File]. observation line : ' + obs)
        
        scored_action = scored.split(':')[0]
        if not scored_action:
            raise ValueError('Incorrect format in [Scoring File]. scored_action is empty. ' + 'scoring line : ' + scored)
        
        if scored_action == obs_action:
            matching_observations += 1        
            ips = float(obs_reward) / float(obs_probability)
            sum_ips += ips
            sum_ipssquared += (ips * ips)

#Computing some statistical measures
expectation_ips         = sum_ips / total_observations
expectation_ipssquared  = sum_ipssquared / total_observations
variance_ips            = expectation_ipssquared -  (expectation_ips * expectation_ips)
standarddeviation_ips   = math.sqrt(variance_ips)
standarderror_ips       = standarddeviation_ips / math.sqrt(total_observations)
errormargin_95ci        = (1.96) * standarderror_ips

print "Total Observations : {0}".format(total_observations)
print "Matching Observations : {0}".format(matching_observations)
print "IPS Estimate : {0}".format(expectation_ips)
print "Std Dev : {0}".format(standarddeviation_ips)
print "95% CI : ({0}, {1})".format((expectation_ips - errormargin_95ci), (expectation_ips + errormargin_95ci))
        