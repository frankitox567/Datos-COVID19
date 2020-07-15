'''
MIT License

Copyright (c) 2020 Sebastian Cornejo

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
'''


import sys
import pandas as pd
from utils import *
import datetime as dt

def prod50(url, prod):
    print('Generando prod 50')
    df = pd.read_csv(url)

    # drop empty columns
    df.dropna(axis=1, how='all', inplace=True)

    #Standardize column names
    df.columns = map(str.capitalize, df.columns)
    df.columns = df.columns.str.replace('_', ' ')
    df = normalizaNombreCodigoRegionYComuna(df)

    #get each week Monday as date
    df['Fecha'] = '2020-W' + df['Week'].astype(str) + '-1'

    #df['Fecha'] = pd.datetime(df['Fecha'], format="%Y-W%W-%w")
    print(df.dtypes)
    print(df.head(10).to_string())


if __name__ == '__main__':
    if len(sys.argv) == 2:
        url = sys.argv[1]
        prod50(url, 'tests')
