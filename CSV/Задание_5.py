import pandas as pd

def union_files(input_files, output_file):
    dataframes = []
    for file in input_files:
        data = pd.read_csv(file)
        dataframes.append(data)
    union_data = pd.concat(dataframes, ignore_index=True)
    union_data.to_csv(output_file, index=False)
union_files(['file1.csv', 'file2.csv'], 'file3.csv')