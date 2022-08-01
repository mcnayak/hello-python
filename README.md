# LaunchDarkly sample Python application

We've built a console application that demonstrates how LaunchDarkly's SDK works.

Below, you'll find the basic build procedure. For more comprehensive instructions, you can visit your [Quickstart page](https://app.launchdarkly.com/quickstart#/) or the [Python SDK reference guide](https://docs.launchdarkly.com/sdk/server-side/python).

This demo requires Python version 3.5 or higher.

## Build instructions

1. Install the LaunchDarkly Python SDK by running `pip install -r requirements.txt`

2. Edit `test.py` and set the value of `sdk_key` to your LaunchDarkly SDK key. If there is an existing boolean feature flag in your LaunchDarkly project that you want to evaluate, set `feature_flag_key` to the flag key.

```python
sdk_key = "sdk-90f53fa4-627f-4c7b-b485-06cdd4fc3993"

feature_flag_key = "my-flag"
```

3. Run `python test.py` with user key, name as json from the command line.

```
   python test.py '{"key": "example-user-key", "name": "Sandy"}' - 
```

should return true based on segment flag, any other name and key combination should return false


4. Run app.py , if the pricing-tier-3 flag is true then http://localhost:5000 should show tier3.html ,  else it should show tier1.html
```
   python app.py 
``` 