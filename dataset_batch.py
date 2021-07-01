import sys
from jotform import *
import pandas as pd
from tqdm import tqdm
import numpy as np
import json

def preprocess_form(form_id):
    questions = {}
    try:
        questions = jotformAPI.get_form_questions(form_id)
    except:
        print("JotformAPI failed!")
        questions = {}
        return
    if not questions:
        return
    df_json = pd.json_normalize(questions)
    df_json.columns = df_json.columns.str.lower()
    old_cols = df_json.columns
    df_json = df_json.filter(regex='\.text$')
    for colname in df_json:
        test_str = colname[:-5] + '.src'
        if test_str in old_cols:
            df_json.drop([colname], axis=1, inplace=True)
    df_json['result'] = pd.Series(df_json.fillna('').values.tolist()).str.join('. ')
    df_json['id'] = form_id
    df_json = df_json.loc[:, ['id', 'result']]
    results.append(df_json.values.tolist()[0])

args = sys.argv[1:]
start, end, file_idx = int(args[0]), int(args[1]), args[2]
API_KEY = '######################'
output_path = 'text1%s.csv' % file_idx
df = pd.read_csv('form_ids.csv')
df = df.round()
FORM_COUNT = end - start
df = df.iloc[start:end,:]
df = df.astype(str)
jotformAPI = JotformAPIClient(API_KEY)
results = []
flag = True

for idx, row in enumerate(tqdm(df.itertuples(), total=FORM_COUNT)):
    if (idx+1) % 1000 == 0:
        df_str = pd.DataFrame(results, columns =['id', 'sentence'])
        df_str.to_csv(output_path, mode='a', header=flag, encoding='utf-8', index=False)
        results.clear()
        flag = False
    preprocess_form(row.formID)
df_str = pd.DataFrame(results, columns =['id', 'sentence'])
df_str.to_csv(output_path,  mode='a', header=False, encoding='utf-8', index=False)

