import pandas as pd

df = pd.read_csv("data/employee.csv")

assert len(df) > 0

assert df["EMP_ID"].is_unique

assert df["SALARY"].isnull().sum() == 0

print("Validation Passed")
