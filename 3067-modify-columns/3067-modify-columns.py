import pandas as pd

def modifySalaryColumn(employees: pd.DataFrame) -> pd.DataFrame:
    #employees['salary']=employees['salary'].apply(lambda x: x*2)
    employees['salary']=employees['salary']*2
    return employees