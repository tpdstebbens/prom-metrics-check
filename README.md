# prom-metrics-check

`prom-metrics-check` is a command line tools which helps checking metrics between dashboards of grafana and prometheus metrics.

If you download external dashboards to your grafana instance (eg. https://github.com/kubernetes-monitoring/kubernetes-mixin)
you are not 100% sure that all queries used in dashboard work with your prometheus instance. This tool looking for in any
dashboard all queries, then it extracts only metrics and check that all used metrics exist in your prometheus instance.


## Usage

To use this tool locally, you will need to create port-forwards for your grafana and prometheus services.


    $ kubectl port-forward svc/grafana 3000:3000
    $ kubectl port-forward svc/prometheus 9090:9090

Also, if you use an API key for Grafana you should set it in you environment.


    $ export GRAFANA_KEY=...

Now you should be able to run the following script:


    $ prom-metrics-check

```
usage: __main__.py [-h] [--grafana-url [grafana_url]] [--grafana-key [grafana_key]] [--json-file [json_file]] [--json-dir [json_dir]] [--prometheus-urls [prometheus_urls ...]]

Command line tool for check metrics between grafana and prometheus instance.

optional arguments:
  -h, --help            show this help message and exit
  --grafana-url [grafana_url]
                        Set grafana url. Must be set with --grafana-key.
  --grafana-key [grafana_key]
                        Set grafana key to have API access. Must be set with --grafana-url
  --json-file [json_file], -j [json_file]
                        Set json file to Grafana dashboard.
  --json-dir [json_dir], -d [json_dir]
                        Set json directory for Grafana dashboards.
  --prometheus-urls [prometheus_urls ...]
                        Set prometheus url. Default value is http://localhost:9090

```

