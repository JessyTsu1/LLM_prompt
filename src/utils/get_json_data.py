import json


def process_json_partial(file_path, start_line, end_line):
    res_data_list = []
    with open(file_path, 'r') as file:
        for _ in range(start_line):
            next(file)
        for line_number, line in enumerate(file, start=1):
            if line_number > end_line:
                break
            try:
                data = json.loads(line)
                res_data_list.append(data)
            except json.JSONDecodeError as e:
                print(f"Error decoding JSON at line {line_number}: {e}")


if __name__ == "__main__":
    json_data = '../../data/file-000000000001.json'
    process_json_partial(json_data, 1, 2)
