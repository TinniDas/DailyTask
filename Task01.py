import pandas as pd
import matplotlib.pyplot as plt






cinnamon_data = pd.read_csv('C:/Users/Ishita/Downloads/archive/balanced_cinnamon_quality_dataset.csv')
print(cinnamon_data)

new_entry = pd.DataFrame({'Sample_ID':['L0071'],
             'Moisture (%)':[10],
             'Ash (%)':[20],
              'Volatile_Oil (%)':[30],
              'Acid_Insoluble_Ash (%)':[40],
              'Chromium (mg/kg)':[50],
              'Coumarin (mg/kg)':[60],
                 'Quality_Label':['High']
            })
print(new_entry)

user_position = int(input("Enter position to insert: "))
if user_position < 0 or user_position > (len(cinnamon_data)+1): #not below 0 index and not leaving cells empty at the end of dataframe
        raise ValueError("Invalid insertion index!")
elif 0 < user_position < len(cinnamon_data):
    cinnamon_data = pd.concat([cinnamon_data.iloc[:user_position],new_entry,cinnamon_data.iloc[user_position:]]).reset_index(drop=True)
    print(cinnamon_data.iloc[user_position-1:user_position+2])
else: #when inserting row at end: just next to the last entry
    cinnamon_data = pd.concat([cinnamon_data,new_entry], ignore_index=True)
    print(cinnamon_data.tail(3))


header_list = cinnamon_data.columns.tolist()
print(header_list)

for header in header_list:
     col = header
     if pd.api.types.is_numeric_dtype(cinnamon_data[col]):
         mean_val = cinnamon_data[col].mean()
         median_val = cinnamon_data[col].median()
         first_diff = cinnamon_data[col].diff()
         print(f"Mean of {col}: {mean_val}")

<<<<<<< Updated upstream
    print(f"Median of {col}: {median_val}")
=======
 #        print(f"Median of {col}: {median_val}")
>>>>>>> Stashed changes
    print(f"First difference of {col}:\n{first_diff}")


         # Plot
         # plt.figure(figsize=(10, 6))
         # first_diff.plot(kind='line', color='blue')
         # plt.title('First Difference plot')
         # plt.xlabel(f'Column:{col}')
         # plt.ylabel(f' First difference Value of {col}')
         # plt.show()
         # continue
     else:
         print(f"\nColumn '{col}' is not numeric. Skipping.")


for header in header_list:
    plt.figure(figsize=(10,6))
