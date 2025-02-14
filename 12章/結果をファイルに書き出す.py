from census2010 import all_data

POPULATION   = 'pop'

print(all_data['AK']['Anchorage'])

anchorage_population = all_data['AK']['Anchorage'][POPULATION]
print(f'2010年のアンカレッジの人口は{anchorage_population}')
