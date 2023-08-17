import csv

result = {}
with open('E:\Only-CO-Lang\Python Code\CODE-py\Flood Ai\Flood-Prediction-shezin\srm\csv\lat_lon_data.csv', mode='r') as f:
    reader = csv.reader(f, delimiter=',')  # dialect=csv.excel_tab?
    for n, row in enumerate(reader):
        print(row)
        if not n:
            # Skip header row (n = 0).
            continue  
        id, long, lat, data = row
        if data not in result:
            result[data] = list()
        result[data].append((long, lat))

print(result)


# Use 'r' prefix before the string to treat it as a raw string
with open(r'E:\Only-CO-Lang\Python Code\CODE-py\Flood Ai\Flood-Prediction-shezin\srm\csv\new_dict.csv', 'w') as f:
    # Rest of the code remains the same
    w = csv.writer(f)
    w.writerow(result.keys())
    w.writerow(result.values())
