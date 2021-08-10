import csv, json

headers = ["Name", "Color", "Parent", "Start", "Stop", "Description", "cambio_nombre1", "When1", "Description1", "cambio_nombre2", "When2", "Description2", "cambio_nombre3", "When3", "Description3"]

result = {}


with open('gldt.csv', mode='r') as csv_file:
	csv_reader = csv.DictReader(csv_file)
	line_count = 0
	for row in csv_reader:
		if line_count == 0:
			line_count += 1
		



		item = {}
		item["Color"] = row["Color"]
		item["Comienzo"] = row["Start"]
		item["Termino"] = row["Stop"]
		item["Descripcion"] = row["Description"]
		item["Padre"] = row["Parent"]

		if row["Namechange1"] != "":

			item["cambio_nombre"] = {}
			item["cambio_nombre"]["Nombre"] = row["Namechange1"]
			item["cambio_nombre"]["Comienzo"] = row["When1"]
			item["cambio_nombre"]["Descripcion"] = row["Description1"]

			if row["Namechange2"] != "":
				item["cambio_nombre"]["cambio_nombre"] = {}
				item["cambio_nombre"]["cambio_nombre"]["Nombre"] = row["Namechange2"]
				item["cambio_nombre"]["cambio_nombre"]["Comienzo"] = row["When2"]
				item["cambio_nombre"]["cambio_nombre"]["Descripcion"] = row["Description2"]

				if row["Namechange3"] != "":
					item["cambio_nombre"]["cambio_nombre"]["cambio_nombre"] = {}
					item["cambio_nombre"]["cambio_nombre"]["cambio_nombre"]["Nombre"] = row["Namechange3"]
					item["cambio_nombre"]["cambio_nombre"]["cambio_nombre"]["Comienzo"] = row["When3"]
					item["cambio_nombre"]["cambio_nombre"]["cambio_nombre"]["Descripcion"] = row["Description3"]





		result[row["Name"]] = item
		line_count += 1



	print(f'Procesadas {line_count} lineas')

with open('distros.json', 'w', encoding='utf-8') as f:
    json.dump(result, f, ensure_ascii=False, indent=4)