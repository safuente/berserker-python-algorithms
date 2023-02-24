import pandas as pd

def convert_json_to_csv(input_file):
    print(input_file)
    with open(input_file, encoding='utf-8') as f:
        df = pd.read_json(f)
    df.to_csv('output.csv', encoding='utf-8', index=False)
    

print('Example 1')
convert_json_to_csv('input.json')
