adict = {1:'a', 2:'b', 3:'c', 4:'d', 5:'c'}
print(adict)
sleep(2)
print(adict)
sleep(2)
print(adict)
sleep(2)
print(adict)



# import sqlite3
# import json

# main_columns = ("\"Nom Com\"", "\"Code Iris\"", "\"Nom Iris\"", "\"P16 Pop\"", "\"SCORE GLOBAL region\"",
# 				"\"ACCČS AUX INTERFACES NUMERIQUES region\"", "\"ACCES A L'INFORMATION region\"", 
# 				"\"COMPETENCES ADMINISTATIVES region\"","\"COMPÉTENCES NUMÉRIQUES / SCOLAIRES region\"", 
# 				"\"GLOBAL ACCES region\"", "\"GLOBAL COMPETENCES region\"")

# main_columns_string = main_columns[0]
# for i in range(1, 11):
# 	main_columns_string +=',' + main_columns[i]

# db = sqlite3.connect("database/output.sqlite", check_same_thread=False)

# cursor = db.cursor()
# cursor.execute("SELECT " + main_columns_string + " FROM Tableau_Full_Data_data")

# my_tuple = tuple(cursor.fetchmany(size=10))
# for i in my_tuple:
# 	print(i)

# print("="*80)
# my_list = sorted(my_tuple, key=lambda x: int(x[4]))
# for j in my_list:
# 	print(j)

# print("="*80)
# main_dict = {x+1:y for x, y in enumerate(my_list)}
# print(main_dict)

# print("="*80)
# dumped_file = json.dumps(main_dict, ensure_ascii=False)
# print(dumped_file)

# cursor.close()
# db.close()