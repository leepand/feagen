import sys
import argparse

import yaml


def feagen_run_with_configs(path_config, feature_config):
    pass


def feagen_run(argv=sys.argv[1:]):

    parser = argparse.ArgumentParser(description='Generate features.')
    parser.add_argument('-p', '--path-config',
                        default=".feagenrc/path_config.yml",
                        help="the path of the path configuration yaml file")
    parser.add_argument('-f', '--feature-config',
                        default=".feagenrc/feature_config.yml",
                        help="the path of the feature configuration yaml file")
    args = parser.parse_args(argv)
    with open(args.path_config) as fp:
        path_config = yaml.loads(args.path_config)
    with open(args.feature_config) as fp:
        feature_config = yaml.loads(args.feature_config)
    import ipdb; ipdb.set_trace()
