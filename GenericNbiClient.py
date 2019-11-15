#!/usr/bin/env python3

# Copyright (c) 2019 Robert Weiler
#
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in all
# copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
# SOFTWARE.

import argparse
import json
import requests
import sys

from urllib3.exceptions import InsecureRequestWarning

TOOL_NAME         = "XMC NBI GenericNbiClient.py"
TOOL_VERSION      = "0.3.0"
HTTP_USER_AGENT   = TOOL_NAME + "/" + TOOL_VERSION
ERR_SUCCESS       = 0 # No error
ERR_USAGE         = 1 # Usage error
ERR_MISSARG       = 2 # Missing arguments
ERR_HTTPREQUEST   = 10 # Error creating the HTTPS request
ERR_XMCCONNECT    = 11 # Error connecting to XMC
ERR_HTTPSRESPONSE = 12 # Error parsing the HTTPS response

requests.packages.urllib3.disable_warnings(category = InsecureRequestWarning)

parser = argparse.ArgumentParser(description = 'This tool queries the XMC API and prints the raw reply (JSON) to stdout.')
parser.add_argument('--host', help = 'XMC Hostname / IP', default = '')
parser.add_argument('--port', help = 'HTTP port where XMC is listening', default = 8443)
parser.add_argument('--httptimeout', help = 'Timeout for HTTP(S) connections', default = 5)
parser.add_argument('--insecurehttps', help = 'Do not validate HTTPS certificates', default = False, action = 'store_true')
parser.add_argument('--username', help = 'Username for HTTP auth', default = 'admin')
parser.add_argument('--password', help = 'Password for HTTP auth', default = '')
parser.add_argument('--query', help = 'GraphQL query to send to XMC', default = 'query { network { devices { up ip sysName nickName } } }')
parser.add_argument('--version', help = 'Print version information and exit', default = False, action = 'store_true')
args = parser.parse_args()

if args.version:
	print(HTTP_USER_AGENT)
	exit(ERR_SUCCESS)

if args.host == '':
	print('Variable --host must be defined. Use -h to get help.', file = sys.stderr)
	exit(ERR_MISSARG)

api_url = 'https://' + args.host + ':' + str(args.port) + '/nbi/graphql'
http_headers = {
	'User-Agent': HTTP_USER_AGENT
}
http_params = {
	'query': args.query
}

try:
	r = requests.get(api_url, headers = http_headers, auth = (args.username, args.password), params = http_params, timeout = args.httptimeout, verify = not args.insecurehttps)
	if r.status_code != requests.codes.ok:
		r.raise_for_status()
	result = r.json()
except BaseException as e:
	print('Failed to fetch data from XMC:')
	print(e)
	exit(ERR_XMCCONNECT)

print(json.dumps(result, indent = 2))

exit(ERR_SUCCESS)
