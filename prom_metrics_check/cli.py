"""Console script for prom-metrics-check."""
import os
import sys
import argparse
import logging

from .prom_metrics_check import load_dashboard, get_all_metrics, \
    check_exist_metrics, json_dashboard, json_dir_dashboards


logging.basicConfig(level='ERROR')
logger = logging.getLogger('prom-metric-check')


GRAFANA_DEFAULT_URL = 'http://localhost:3000'
PROMETHEUS_DEFAULT_URL = 'http://localhost:9090'

GRAFANA_URL = os.environ.get(
    'GRAFANA_URL', GRAFANA_DEFAULT_URL)
#GRAFANA_KEY = os.environ.get(
#    'GRAFANA_KEY')
GRAFANA_KEY = "eyJrIjoidDYwT1N4cmhGSWFWTXE3RkwxSERrT29GeGtaUGZVQXAiLCJuIjoic3RldmVudGVzdCIsImlkIjoxfQ=="

PROMETHEUS_URLS = os.environ.get(
    'PROMETHEUS_URLS', PROMETHEUS_DEFAULT_URL).split(',')

JSON_DIRECTORY = 'dashboards'

def main(args=None):
    """Console script for prom_metrics_check."""
    parser = argparse.ArgumentParser(
        description='Command line tool for check metrics between '
                    'grafana and prometheus instance.')
    parser.add_argument(
        '--grafana-url',
        metavar='grafana_url',
        help='Set grafana url. Default value is {url}. Must be set with --grafana-key.'.format(
            url=GRAFANA_DEFAULT_URL),
        nargs='?',
        default=GRAFANA_URL)
    parser.add_argument(
        '--grafana-key',
        metavar='grafana_key',
        help='Set grafana key to have API access. Must be set with --grafana-url',
        nargs='?',
        default=GRAFANA_KEY)
    parser.add_argument(
        '--json-file',
        metavar='json_file',
        help='Set json file to Grafana dashboard.',
        nargs='?')
    parser.add_argument(
        '--json-dir',
        metavar='json_dir',
        help='Set json directory for Grafana dashboards. Default is /{directory}'.format(
            directory=JSON_DIRECTORY),
        nargs='?',
        default=JSON_DIRECTORY)
    parser.add_argument(
        '--prometheus-urls',
        metavar='prometheus_urls',
        help='Set prometheus url. Default value is {url}'.format(
            url=PROMETHEUS_DEFAULT_URL),
        nargs='*',
        default=PROMETHEUS_URLS)
    args = parser.parse_args(args)
    print(args)
    for url in args.prometheus_urls:
       # dashboards = load_dashboard(url=args.grafana_url, key=args.grafana_key) if 
        #dashboards = json_dashboard(json_file=args.json_file)
        dashboards = json_dir_dashboards(directory=args.json_dir)
        except_metrics = get_all_metrics(dashboards=dashboards)
        missing_metrics = check_exist_metrics(except_metrics, url)
        if missing_metrics:
            logger.critical(
                " Metrics which don't exist: {metrics}".format(
                    metrics=', '.join(missing_metrics)))
    return 0


if __name__ == '__main__':
    sys.exit(main())    # pragma: no cover
