import pandas as pandas

list_of_static_paths = ['2020', '2021', '2022', '2023']
months = ['01', '02', '03', '04', '05', '06', '07', '08', '09', '10', '11', '12']
days = [
    '01', '02', '03', '04', '05', '06', '07', '08', '09', '10',
    '11', '12', '13', '14', '15', '16', '17', '18', '19', '20',
    '21', '22', '23', '24', '25', '26', '27', '28', '29', '30', '31'
]

dataframes = []

for path in list_of_static_paths:
    for month in months:
        for day in days:
            try:
                dataframes.append(pandas.read_csv(f'orderstats/{path}/{path}-{month}-{day}.csv'))

            except Exception:
                    print('Такого файла нет')

final_frame = pandas.concat(dataframes, ignore_index=True)

final_frame.to_csv('FinalStats.csv', encoding='utf-8')
