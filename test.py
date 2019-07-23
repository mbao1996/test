#coding=gbk
import tushare as ts
import tushare
import os
import pandas as pd

print('   ***   tushare_version: ', tushare.__version__, '   ***\n')
TOKEN = 'c27f964551786735a0cebbc26a743d0e18b06e9181f2166632964e37'

ts.set_token(TOKEN)
pro = ts.pro_api()


df_query = pd.DataFrame()
print('-------0---:', len(df_query), df_query.shape[0])
df = pro.query('fina_indicator', ts_code='600036.SH', period='20190630')
print(df, len(df))


'''
df_query = df_query.append(df, ignore_index=True)
print(df_query)
print('-------1---:', len(df_query), df_query.shape[0])
df = pro.query('fina_indicator', ts_code='600066.SH', period='20181231')
print(df)
df_query = df_query.append(df, ignore_index=True)
print('-------2---:', len(df_query), df_query.shape[0])
print(df_query)
print('-------3---:', len(df_query), df_query.shape[0])
print(df_query.iloc[0]['eps'])
'''

print('\n finished')
