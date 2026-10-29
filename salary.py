# import pandas as pd
# import numpy as np

# salary_series = pd.Series([50000, 60000, 70000, 80000, 90000])

# print(salary_series)
# import pandas as pd
# import numpy as np

# salary_series = pd.Series([50000, 60000, 70000, 80000, 90000])

# print(salary_series)
employee_data = {
"Employee_ID":["E001","E002","E003","E004","E005"],
" Employee_Name":["Alice","Bob","Charlie","David","Eve"],
"Department":["HR","Finance","IT","Marketing","Sales"],
City":["New York","Los Angeles","Chicago","Houston","Phoenix"],
"Salary":[50000,60000,70000,80000,90000],
"Experience":[2,3,5,4,6],
"Rating":[4.5,4.2,4.8,4.6,4.9]
}
print(employee_data)
employee_df = pd.DataFrame(employee_data)
print(employee_df)