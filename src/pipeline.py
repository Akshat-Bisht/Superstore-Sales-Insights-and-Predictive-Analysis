from pathlib import Path
import pandas as pd
import numpy as np

def load_data(path: Path) -> pd.DataFrame:
    try:
        return pd.read_csv(path, encoding='utf-8')
    except UnicodeDecodeError:
        return pd.read_csv(path, encoding='latin-1')

def clean(df: pd.DataFrame) -> pd.DataFrame:
    df = df.copy()
    df.columns = [c.strip().replace(' ', '_').replace('-', '_') for c in df.columns]
    # detect date
    order_col = None
    for c in df.columns:
        if c.lower().replace('_','').startswith('orderdate'):
            order_col = c
            break
    if order_col is None:
        cands = [c for c in df.columns if 'date' in c.lower()]
        order_col = cands[0] if cands else None
    if order_col:
        df[order_col] = pd.to_datetime(df[order_col], errors='coerce')
        df = df.dropna(subset=[order_col]).sort_values(order_col)
    for name in ['Sales','Profit','Discount','Quantity']:
        for c in df.columns:
            if c.lower()==name.lower():
                df[c] = pd.to_numeric(df[c], errors='coerce')
    df = df.dropna(subset=[c for c in df.columns if c.lower() in ['sales','profit']])
    return df

if __name__ == '__main__':
    data_path = Path(__file__).resolve().parents[1] / 'data' / 'Sample - Superstore.csv'
    df = load_data(data_path)
    df = clean(df)
    print(df.head())
