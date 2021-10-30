from flask import Flask, request, redirect, render_template #, url_for
#from flask_sqlalchemy import SQLAlchemy
import sqlite3
import json

main_string = '"Nom Com","Code Iris","Nom Iris", "P16 Pop","SCORE GLOBAL region","ACCČS AUX INTERFACES NUMERIQUES region","ACCES A L\'INFORMATION region","COMPETENCES ADMINISTATIVES region","COMPÉTENCES NUMÉRIQUES / SCOLAIRES region","GLOBAL ACCES region","GLOBAL COMPETENCES region"'
FILTERS = ["region", "departement", "commune", "intercommunalite"]
REFERENCE_POINT = "reference"
FILTER_COLOUMNS = ["Libreg", "Libdep", "Libcom", "Libepci"]
ROW_COUNT_SENDIG_FIRST = 20
ROW_COUNT_SENDIG_SECOND = 10

app = Flask(__name__)
db = sqlite3.connect("database/output.sqlite", check_same_thread=False)

main_cursor = db.cursor()
main_query = "SELECT " + main_string + " FROM Tableau_Full_Data_data"
main_cursor.execute(main_query)
my_list = list(main_cursor.fetchall())
my_size_list = len(my_list)


def sliding_window(received_request):
	searching_words = []
	for word in FILTERS:
		searching_words.append(received_request.args.get(word))

	# please consider this drop_down filter
	reference_point= request.args.get(REFERENCE_POINT)

	sql_statement = main_query + " WHERE " + FILTER_COLOUMNS[0] + "=" + "\'" + searching_words[0] + "\'"
	for item, value in zip(FILTER_COLOUMNS, searching_words):
		if item == "Libreg":
			continue
		if value != "ALL":
			sql_statement+= " AND " + item + "=" + "\'" + value  + "\'"

	new_cursor = db.cursor()
	new_cursor.execute(sql_statement)
	query_result = list(new_cursor.fetchall())

	return query_result


# def returning_slides(id, my_list, my_size_list):
# 	if id == 0:
# 		new_dict_search = {}
# 		for p in range(id, ROW_COUNT_SENDIG):
# 			new_dict_search[p] = my_list[p]
# 		return json.dumps(new_dict_search, ensure_ascii=False)
# 	else:
# 		new_dict_search_next = {}
# 		new_dict_search_prev = {}
# 		start_prev = id - 10
# 		end_prev = id
# 		start_next = id + 10
# 		if (id+20) <= my_size_list:
# 			end_next = id+20
# 		else:
# 			end_next = my_size_list

# 		new_dict_search_next = {}
# 		new_dict_search_prev = {}
# 		for m in range(start_next, end_next):
# 			new_dict_search_next[m] = my_list[m]
# 		for n in range(start_prev, end_prev):
# 			new_dict_search_prev[n] = my_list[n]

# 		final_dict = {"previous":new_dict_search_prev, "next":new_dict_search_next}
# 		return json.dumps(final_dict, ensure_ascii=False)


@app.route('/', methods=["GET", "POST"])
def index():
	new_dict_search = {}
	dict_a = {}
	dict_b = {}
	if request.method == "GET":
		for i in range(ROW_COUNT_SENDIG_FIRST-10):
			dict_a[i] = my_list[i]
		for t in range(ROW_COUNT_SENDIG_FIRST-10, ROW_COUNT_SENDIG_FIRST):
			dict_b[t] = my_list[t]

		return json.dumps({"first":dict_a, "second":dict_b}, ensure_ascii=False)
	else:
		result_list = sliding_window(request)
		query_size = len(result_list)
		if query_size <= ROW_COUNT_SENDIG_FIRST:
			for i in range(ROW_COUNT_SENDIG_FIRST-10):
				dict_a[i] = my_list[i]
			for t in range(ROW_COUNT_SENDIG_FIRST-10, ROW_COUNT_SENDIG_FIRST):
				dict_a[t] = my_list[t]

			return json.dumps({"first":dict_a, "second":dict_b}, ensure_ascii=False)
		else:
			row_size = ROW_COUNT_SENDIG_FIRST
			for k in range(row_size):
				new_dict_search[k] = result_list[k]

			return json.dumps(new_dict_search, ensure_ascii=False)


@app.route('/<int:id>', methods=["GET"])
def main_page_sliding(id):
	id = int(id)
	new_dict_search = {}

	if (id + ROW_COUNT_SENDIG_SECOND) <= my_size_list:
		limit = id + ROW_COUNT_SENDIG_SECOND
	else:
		limit = my_size_list

	for m in range(id, limit):
		new_dict_search[m] = my_list[m]

	return json.dumps(new_dict_search, ensure_ascii=False)


@app.route('/<int:id>', methods=["POST"])
def second_page_sliding(id):
	id = int(id)
	new_dict_search = {}
	final_result = sliding_window(request)
	size_of_list = len(final_result)

	if (id + ROW_COUNT_SENDIG_SECOND) <= size_of_list:
		limit = id + ROW_COUNT_SENDIG_SECOND
	else:
		limit = size_of_list

	for n in range(id, limit):
		new_dict_search[n] = final_result[n]

	return json.dumps(new_dict_search, ensure_ascii=False)


if __name__ == "__main__":

	app.run(debug=True)
	main_cursor.close()
	db.close()


