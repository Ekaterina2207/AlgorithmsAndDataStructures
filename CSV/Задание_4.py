import pandas as pd

def count_average(input_file, output_file, avg=None):
    data = pd.read_csv(input_file)
    if avg is None:
        avg = data.select_dtypes(include=['number']).columns.tolist()
    data['Среднее'] = data[numeric_columns].mean(axis=1).round(2)
    data.to_csv(output_file, index=False)
count_average('all_mark.csv', 'avg_mark.csv')