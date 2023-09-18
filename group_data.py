import os
import pandas as pd


def group_csvs(directory: str, finalfile: str) -> None:
    """
    groups all csvs files together into one file

    Args:
        directory str: main directory path to the csvs
        filename str: grouped csv path or file name
    """
    all_data = pd.DataFrame()
    for filename in os.listdir(directory):
        if filename.startswith('jobs_') and filename.endswith('.csv'):
            df = pd.read_csv(os.path.join(directory, filename))
            all_data = pd.concat([all_data, df])

    all_data.to_csv(finalfile, index=False)


if __name__ == '__main__':
    group_csvs('data_scientist', 'grouped files/data_scientist.csv')
