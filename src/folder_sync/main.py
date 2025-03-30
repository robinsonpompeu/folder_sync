"""
Folder Monitoring and Synchronization

This is the main script of the project and it performs the following steps:
- Parses command line arguments
- Checks if the source and replica informed directories are valid
- Verifies if the log file already exists (and creates it if not)
- Configures the log process
- Executes the source and replica monitoring and synchronization

In order to stop the execution the user must produce a keyboard interruption.

Arguments:
-----
    --source_dir      Absolute path of source dir
    --replica_dir     Absolute path of replica dir
    --log_file        Absolute path of log file
    --t_interval      Synchronization interval in seconds

Notes:
-----
    - The user running this script must have write permissions on both folders
    - Source and replica absolute paths must have a trailing slash
    - Both source and replica folder cannot be removed during monitoring.

"""

import argparse
import sys
import types
import time

import dir_monitor
import log_recorder
import vol_manager

import pandas as pd

from pathlib import Path

parser = argparse.ArgumentParser(description = 'Folder Sync configuration.')
parser.add_argument(
    '--source_dir', 
    type = str,
    required = True, 
    help = 'Absolute path of source directory.'
)
parser.add_argument(
    '--replica_dir', 
    type = str,
    required = True, 
    help = 'Absolute path of replica directory.'
)
parser.add_argument(
    '--log_file', 
    type = str,
    required = True, 
    help = 'Absolute path of log file.'
)
parser.add_argument(
    '--t_interval', 
    type = float, 
    help = 'Synchronization interval.'
)

args = parser.parse_args()

if not Path(args.source_dir).is_dir():
    print("Source dir is invalid.")
    sys.exit()
    
if not Path(args.replica_dir).is_dir():
    print("Replica dir is invalid.")
    sys.exit()

if not Path(args.log_file).is_file():
    try:
        Path(args.log_file).touch()
    except FileNotFoundError:
        print("Log file is invalid.")
        sys.exit()
    
if __name__ == '__main__':
    log_recorder.decorate(vol_manager, log_recorder.log, args.log_file)
    try:
        while True:
            if not Path(args.source_dir).exists():
                raise FileNotFoundError(
                    f"Source dir {str(args.source_dir)} not found."
                )
                sys.exit()
            df_source  = dir_monitor.list_tree(args.source_dir)
            if not Path(args.replica_dir).exists():
                Path(args.replica_dir).mkdir(parents = True)
            df_replica = dir_monitor.list_tree(args.replica_dir)
            df_update  = df_source[~df_source.index.isin(df_replica.index)]
            df_delete  = df_replica[~df_replica.index.isin(df_source.index)]
            hash_index = df_source.index.intersection(df_replica.index)
            df_hashes  = df_source.loc[hash_index].compare(
                df_replica.loc[hash_index], 
                result_names = ("Source", "Replica")
            )
            if not df_hashes.empty:
                df_update = pd.concat(
                    [
                        df_update,
                        df_hashes[df_hashes.hash.Source != df_hashes.hash.Replica]
                    ]
                )
            for row in df_update.itertuples():
                vol_manager.update_dest(
                    args.source_dir + row.Index, 
                    args.replica_dir + row.Index
                )
            for row in df_delete.itertuples():
                if (Path(args.replica_dir) / Path(row.Index)).is_dir():
                    vol_manager.remove_dir(args.replica_dir + row.Index)
                else:
                    vol_manager.remove_file(args.replica_dir + row.Index)
            time.sleep(args.t_interval)
    except KeyboardInterrupt:
        print('', end = '\r')
        print("\nSystem interrupted by user.\n")
        sys.exit()