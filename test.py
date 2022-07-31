#!/usr/bin/env python
from cgi import print_arguments
import ldclient
import sys
import json
from ldclient.config import Config

# print command line

# Set sdk_key to your LaunchDarkly SDK key before running
sdk_key = "sdk-90f53fa4-627f-4c7b-b485-06cdd4fc3993"

# Set feature_flag_key to the feature flag key you want to evaluate
feature_flag_key = "segment"

def show_message(s):
  print("*** %s" % s)
  print()

if __name__ == "__main__":
  if not sdk_key:
    show_message("Please edit test.py to set sdk_key to your LaunchDarkly SDK key first")
    exit()

  ldclient.set_config(Config(sdk_key))

  # The SDK starts up the first time ldclient.get() is called
  if ldclient.get().is_initialized():
    show_message("SDK successfully initialized!")
  else:
    show_message("SDK failed to initialize")
    exit()

  # Set up the user properties. This user should appear on your LaunchDarkly users dashboard
  # soon after you run the demo.
  
  user = json.loads(sys.argv[1])
  
  flag_value = ldclient.get().variation(feature_flag_key, user, False)

  show_message("Feature flag '%s' is %s for this user" % (feature_flag_key, flag_value))

  # Here we ensure that the SDK shuts down cleanly and has a chance to deliver analytics
  # events to LaunchDarkly before the program exits. If analytics events are not delivered,
  # the user properties and flag usage statistics will not appear on your dashboard. In a
  # normal long-running application, the SDK would continue running and events would be
  # delivered automatically in the background.
  ldclient.get().close()
