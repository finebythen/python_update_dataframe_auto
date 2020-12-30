import pandas as pd

df_cols = ["id", "product", "value" ]
df_list = [
    [1, "product_a", 17],
    [2, "product_b", 19],
    [3, "product_c", 5],
    [4, "product_d", 11],
    [5, "product_e", 23],
]

df = pd.DataFrame(df_list, columns=df_cols)

max_val = 20
values_list = [3, 11, 2, 19]

for i in range(len(values_list)):
    cck_val = values_list[i]

    for idx in df.index:
        val = df.at[idx, "value"]
        if (cck_val + val) <= max_val:
            df.iloc[idx, df.columns.get_loc("value")] = cck_val + val
            break