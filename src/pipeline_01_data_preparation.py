import os
import argparse
import yaml
import logging as lg

def read_params(config_path):
    with open(config_path) as f:
        config = yaml.safe_load(f)
    return config


def main(config_path, datasource):
    config = read_params(config_path)
    print(config)


if __name__=='__main__':
    args=argparse.ArgumentParser()
    config_path=os.path.join('config','params.yaml')
    args.add_argument("--config", default=config_path)
    args.add_argument("--datasource", default=None)

    parsed_args=args.parse_args()
    main(config_path=parsed_args.config, datasource=parsed_args.datasource)

