import os  
import argparse # give command line input

import yaml #read yaml files
import logging # to store log with date and time



def read_params(config_path):
    with open(config_path) as yaml_file:
        config=yaml.safe_load(yaml_file)
    return config 

def main(config_path,datasource):
    config=read_params(config_path)
    print(config)



if __name__=="__main__":
    args=argparse.ArgumentParser()
    default_config_path=os.path.join("config","params.yaml")
    args.add_argument("--config",default=default_config_path) # add the argument we want to pass while using the command line,
    args.add_argument("--datasource",default=None) # data scource,if it is not then it will choose from configration file
    parsed_args=args.parse_args()
    main(config_path=parsed_args.config , datasource=parsed_args.datasource)

    # in the output we will get the the parameters details

    


    