# OVH-Mass-Domain-Replacer
With this script it is possible to replace a specific IP address with another in the DNS zone. This could be helpful if you transfere a webserver to another IP address.

## Setup
First, install the latest release of Python wrapper: `$ pip install ovh`
Then change the values `oldIP` and `newIP`
After that you need to create a [OVH API Key](https://api.ovh.com/createToken/index.cgi?GET=/*&PUT=/*&POST=/*&DELETE=/* "OVH API Key") and edit the values in `ovh.Client()` function
