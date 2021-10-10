import os
import pandas as pd
import argparse
import numpy as np
from src.utils.all_utils import create_directory,read_yaml,copy_file
from tqdm import tqdm
def get_data(config_path):
     config= read_yaml(config_path)
     source_download_dir=config["source_download_dir"]
     local_data_dir=config["local_data_dir"]

     for source_download_dir,local_data_dir in tqdm(zip(source_download_dir,local_data_dir),total=2,desc="iterating list of folders"):
          create_directory([local_data_dir])
          print(source_download_dir)
          copy_file(source_download_dir,local_data_dir)
        

if __name__=="__main__":
      args=argparse.ArgumentParser()
      args.add_argument("--config","-c",default="config/config.yaml")
      parsed_args= args.parse_args()
      get_data(config_path=parsed_args.config)