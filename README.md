# Dashboard - Users Access on a fictional e-Commerce website

## 📃Description

This repository contains a dashboard, made on Power BI by myself and [@Guilherme Abreu](https://github.com/guilhermedel), that explores fictional users access into an e-Commerce website. The website sells laptops, monitors, servers, printers and SmartOffice packages. There are 3 types of log in: error (user failed to log in the platform), success (user successfuly logged in the platform) and info (user, who is probably an employee/system admin, changed an information in the website).

![image](https://github.com/user-attachments/assets/67f741ac-0cbf-4a49-804c-f26979b33117)

## 🤖 Used Technologies
- Power BI
- Python  
    - pandas
    - datetime
    - random
    - faker

## 🖥️Data Extraction 

The fictional data (contained in the _random_data.json_ file), was generated using a Python code, which can be seen in the "fake_data_generator.py" file. This code was idealized by [@Michael Machado](https://github.com/MachadoMichael/MachadoMichael).

## 👩‍💻Data Transformation
The fictional data was treated in another Python program (_treating_fake_data.py_). To achieve that, the pandas lib was used to turn the .json file into a dataframe. The 'date' column was converted to the datetime type, and the hours and months in that column were analysed. 

## - New Column: Shift
A new column ('shift') was created in the dataframe, and the 'date' column (its hours, to be more specific) determines its value. The logic below was used to fill the 'shift' column:

If the hour in the 'date' column is...

- lower than 6 and higher or equal to 0 (midnight), the shift should be 'dawn' ('madrugada', in portuguese.)

- lower than 12 and higher or equal to 6, the shift should be 'morning' ('manhã', in portuguese.)

- lower than 18 and higher or equal to 12, the shift should be 'afternoon' ('tarde', in portuguese.)

- lower than 0 (midnight) and higher or equal to 18, the shift should be 'night' ('noite', in portuguese.)

With that column in hands, it is possible to analyse when (in which shift) the e-Commerce platform was most used. 

## - New Column: Month
A new column ('month') was created in the dataframe, and the 'date' column (its months, to be more specific) determines its value. The logic below was used to fill this new column:

A list of months was created in the function 'get_month' of the program. Each element of the list corresponds to a month of the year ('january', 'february', 'march', ..., 'december').

The function receives as a parameter the month contained in the 'date' column, which is an integer number that varies from 1 to 12, and returns the list element contained in the position determined by the given number - 1.

With that column in hands, it is possible to analyse in which month of 2023 the e-Commerce platform was most accessed. 

## 📊Data Load
After the data transformation, the dataframe was converted into a new .json file (_treated_data.json_). That json file was loaded on Power BI and proper grapphics were selected to data visualization on the dashboard.

## 🧐 Dashboard's Functionalities 
Power BI allows data visualization dynamism by making possible to apply filters on the dashboard.
You can filter the data based on an user, type of content accessed, access shift, searched product or month. The dashboard will adapt itself to show the data while having your filter as the primary parameter.


## 💡Insights
- The fictional website had a total of 114 accesses in 2023;
- Video is the most required type of information;
- The afternoon is the peak shift in terms of user access;
- December of 2023 was the month of the year with the higher number of accesses;
- Failed attempts (ERROR) of logins happen most often at night (14) and during afternoons (14);
- Laptop is the most required product.
