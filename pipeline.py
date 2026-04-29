from src.extract import extract
from src.transform import transform
from src.load import load

def run_pipeline():
    print("starting pipeline..")

    df = extract()
    print("After extract",df.shape)

    df = transform(df)
    print("After transform",df.shape)

    load(df)
    print("Data loaded successfully!")

if __name__ == "__main__":
    run_pipeline()
