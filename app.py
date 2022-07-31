#!/usr/bin/env python
from cgi import print_arguments
from flask import Flask, flash, render_template
from datetime import datetime
import ldclient
import sys
import json
from ldclient.config import Config
from flask import Flask, render_template
import re
import os

app = Flask(__name__, static_folder='public', template_folder='views')

# Set sdk_key to your LaunchDarkly SDK key before running
sdk_key = "sdk-90f53fa4-627f-4c7b-b485-06cdd4fc3993"
feature_flag_key = "pricing-tier-3"
ldclient.set_config(Config(sdk_key))
ld_client = ldclient.get() 

def show_message(s):
  print("*** %s" % s)
  print()

# Set feature_flag_key to the feature flag key you want to evaluate


@app.route('/')
def pricing():
    """Displays the pricing page."""
    
    # TODO: Implement the feature flag here
    user = {
      "key": "anon",
      "anonymous": True
    }
    is_tier_3_enabled = ld_client.variation('pricing-tier-3', user, False)
    if is_tier_3_enabled:
      return render_template('tier1.html', is_tier_3_enabled=is_tier_3_enabled)
    else:
      return render_template('tier3.html', is_tier_3_enabled=is_tier_3_enabled)

if __name__ == '__main__':
    app.run()
   

