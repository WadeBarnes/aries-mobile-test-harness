# -----------------------------------------------------------
# Behave environtment file used to hold test hooks to do
# Setup and Tear Downs at different levels
# For more info see:
# https://behave.readthedocs.io/en/latest/tutorial.html#environmental-controls
#  
# -----------------------------------------------------------
from appium import webdriver
#from browserstack.local import Local
from sauceclient import SauceClient
from decouple import config
import os, json

config_file_path = os.path.join(os.path.dirname(__file__), '..', "sl_config.json")
print("Path to the config file = %s" % (config_file_path))
with open(config_file_path) as config_file:
    CONFIG = json.load(config_file)

# Take user credentials from environment variables if they are defined
#if 'BROWSERSTACK_USERNAME' in os.environ: CONFIG['capabilities']['browserstack.user'] = os.environ['BROWSERSTACK_USERNAME'] 
#if 'BROWSERSTACK_ACCESS_KEY' in os.environ: CONFIG['capabilities']['browserstack.key'] = os.environ['BROWSERSTACK_ACCESS_KEY']

# Take user credentials from environment variables if they are defined
if 'SAUCE_USERNAME' in os.environ: username = os.environ['SAUCE_USERNAME'] 
if 'SAUCE_ACCESS_KEY' in os.environ: access_key = os.environ['SAUCE_ACCESS_KEY']
url = 'http://%s:%s@ondemand.saucelabs.com:80/wd/hub' % (username, access_key)
region = config('SL_REGION')
url = 'http://%s:%s@ondemand.%s.saucelabs.com:80/wd/hub' % (username, access_key, region)

def before_feature(context, feature):
    CONFIG['capabilities']['sauce:options']['name'] = feature.name
    desired_capabilities = CONFIG['capabilities']
    # context.browser = webdriver.Remote(
    #     desired_capabilities=desired_capabilities,
    #     command_executor="http://hub-cloud.browserstack.com/wd/hub"
    # )
    context.browser = webdriver.Remote(
        desired_capabilities=desired_capabilities,
        command_executor=url,
        keep_alive=True
    )
    #context.driver = webdriver.Remote(url, desired_capabilities)

def after_feature(context, feature):
    # Invoke driver.quit() after the test is done to indicate to BrowserStack 
    # that the test is completed. Otherwise, test will appear as timed out on BrowserStack.
    # if context does not contain browser then something went wrong on initialization and no need to call quit.
    if hasattr(context, 'browser'):
        context.browser.quit()


