import logging
import sys
import argparse

from swarmlib.aco4tsp.main import configure_parser as aco_parser
from swarmlib._version import __version__

logging.basicConfig(
    format='%(asctime)s [%(threadName)-12.12s] [%(levelname)-5.5s]  %(message)s',
    stream=sys.stdout,
    level=logging.INFO)

LOGGER = logging.getLogger(__name__)


def run_swarm():
    parser = argparse.ArgumentParser(
        description='Solve an optimization problem with the chosen algorithm.')

    parser.add_argument(
        '-v',
        '--version',
        action='version',
        version='%(prog)s v' + __version__,
        help='Show version and exit')

    sub_parsers = parser.add_subparsers(
        title='Commands',
        description='Valid commands',
        help='Choose the algorithm to execute')
    aco_parser(sub_parsers)

    args = vars(parser.parse_args())
    if args:
        algorithm = args.pop('func')
        algorithm(args)
    else:
        parser.print_usage()

if __name__ == '__main__':
    run_swarm()
