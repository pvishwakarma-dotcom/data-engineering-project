import pandas as pd

def transform(df):
    # standardize column names
    df.columns = (
        df.columns
        .str.strip()
        .str.lower()
    )

    # remove missing rows based on some column
    df = df.dropna(subset = ["model year", "electric range"])
    
    # convert to numeric safely
    df["model year"] = pd.to_numeric(df["model year"],errors = "coerce")
    df["electric range"] = pd.to_numeric(df["electric range"],errors = "coerce")

    # remove missing rows based on some column
    df = df.dropna(subset = ["model year", "electric range"])

    # remove rows where electric range = 0
    df = df[df["electric range"] != 0]
    
    # remove duplicates based on dol vehicle id
    df = df.drop_duplicates(subset = ["dol vehicle id"])

    # reset index
    df = df.reset_index(drop=True)

    return df