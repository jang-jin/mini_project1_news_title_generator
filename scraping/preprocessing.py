import pandas as pd

data = pd.read_csv('./scraping/kbsnews.csv', header=None)
print(data[1])