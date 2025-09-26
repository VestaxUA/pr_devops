from CsvReader import CsvReader
from CsvToJsonConverter import CsvToJsonConverter
from JsonReader import JsonReader
from pr_2.StudentFinder import StudentFinder

"""if __name__ == "__main__":
    csv_url = "https://informer.com.ua/dut/python/import/st_gt.csv"
    csv_reader = CsvReader()
    data = csv_reader.read_data(csv_url)
    for row in data:
        print(row)"""

if __name__ == "__main__":
    csv_url = "https://informer.com.ua/dut/python/import/st_gt.csv"
    json_path = "students_data.json"  # Шлях до файлу JSON

    # Ініціалізація CsvToJsonConverter та виконання конвертації
    converter = CsvToJsonConverter()
    converter.read_and_convert(csv_url, json_path)

    # Читання та відображення даних з JSON
    json_reader = JsonReader()
    #json_reader.display_data(json_path)

    # Пошук та виведення інформації про студентів
    finder = StudentFinder(json_reader)
    finder.load_data(json_path)
    surname_to_find = "Барченко"  # Вкажіть прізвище для пошуку
    found_students = finder.find_students_by_surname(surname_to_find)
    finder.display_students_info(found_students)



