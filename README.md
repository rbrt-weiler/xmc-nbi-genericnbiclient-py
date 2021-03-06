# XMC NBI GenericNbiClient (Python)

GenericNbiClient sends a query to the GraphQL-based API provided by the Northbound Interface (NBI) of [Extreme Management Center (XMC)](https://www.extremenetworks.com/product/extreme-management-center/) and prints the raw JSON response to stdout.

**Notice**: This project has surfaced as a proof of concept and is _not maintained_ anymore. If you need a production ready NBI client, please refer to [the Go version of GenericNbiClient](https://gitlab.com/rbrt-weiler/xmc-nbi-genericnbiclient-go).

## Branches

This project uses two defined branches:

* `master` is the primary development branch. Code within `master` may be broken at any time.
* `stable` is reserved for code that compiles without errors and is tested. Track `stable` if you just want to use the software.

Other branches, for example for developing specific features, may be created and deleted at any time.

## Dependencies

GenericNbiClient.py requires the Python module `requests` to be installed. PIP may be used to install it:

`pip install requests`

## Usage

Tested with Python 3.8.0.

`GenericNbiClient.py -h`:

```text
  -h, --help            show this help message and exit
  --host HOST           XMC Hostname / IP
  --port PORT           HTTP port where XMC is listening
  --httptimeout HTTPTIMEOUT
                        Timeout for HTTP(S) connections
  --insecurehttps       Do not validate HTTPS certificates
  --username USERNAME   Username for HTTP auth
  --password PASSWORD   Password for HTTP auth
  --query QUERY         GraphQL query to send to XMC
  --version             Print version information and exit
```

## Source

The original project is [hosted at GitLab](https://gitlab.com/rbrt-weiler/xmc-nbi-genericnbiclient-py), with a [copy over at GitHub](https://github.com/rbrt-weiler/xmc-nbi-genericnbiclient-py) for the folks over there. Additionally, there is a project at GitLab which [collects all available clients](https://gitlab.com/rbrt-weiler/xmc-nbi-clients).
