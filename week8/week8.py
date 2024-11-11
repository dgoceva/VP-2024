# "C:\\Samples\\VP-2024\\week8\\demofile.txt"
import random
import json
import csv

def file_operations1():
    f = open(r"C:\Samples\VP-2024\week8\demofile.txt","r")
    txt = f.read()
    f.close()
    print(txt)
    fout = open(r"C:\Samples\VP-2024\week8\demofile.out.txt","a")
    fout.write(txt+"\n")
    fout.close()

def file_operations2():
    with open(r"C:\Samples\VP-2024\week8\demofile.txt","r") as f:
        txt = f.read()
    print(txt)
    with open(r"C:\Samples\VP-2024\week8\demofile.out.txt","a") as fout:
        fout.write(txt+"\n")

def file_operation3():
    try:
        with open(r"C:\Samples\VP-2024\week8\demofile1.txt","r") as f:
            txt = f.read()
        print(txt)
        with open(r"C:\Samples\VP-2024\week8\demofile.out.txt","a") as fout:
            fout.write(txt+"\n")
    except FileNotFoundError:
        print("File not found")
    except Exception as e:
        print("An error occurred:", e)

def file_operation4():
    words = 0
    with open(r"C:\Samples\VP-2024\week8\demofile.txt","r") as f:
        try:
            print(f.readline().upper())
            for line in f.readlines():
                print(line,end="")
                words += len(line.split())
            print("\nTotal words: "+str(words))
        except Exception as e:
            print("An error occurred:", e)

def file_operation5():
    words = 0
    try:
        with open(r"C:\Samples\VP-2024\week8\demofile.txt","r") as f:
            for line in f:
                print(line,end="")
                words += len(line.split())
            print("\nTotal words: "+str(words))
    except Exception as e:
            print("An error occurred:", e)

def write_numbers():
    try:
        with open(r"C:\Samples\VP-2024\week8\numbers.txt","w") as f:
            for i in range(10):
                f.write(str(random.randint(-10,10))+"\n")
    except Exception as e:
        print("An error occurred:", e)

def read_numbers():
    sum = 0
    try:
        with open(r"C:\Samples\VP-2024\week8\numbers.txt","r") as f:
            for line in f:
                print(line.strip())
                sum += int(line)
            print("\nSum: "+str(sum))
    except Exception as e:
        print("An error occurred:", e)

def read_json():
    try:
        with open(r"C:\Samples\VP-2024\week8\info.json","r") as f:
            data = json.load(f)
            print(data)
            for employee in data["employees"]:
                print(employee["name"])
    except FileNotFoundError:
        print("File not found")
    except json.JSONDecodeError:
        print("Invalid JSON")
    except Exception as e:
        print("An error occurred:", e)

def write_json():
    try:
        with open(r"C:\Samples\VP-2024\week8\info.out.json","w") as f:
            data = {
                "employees": [
                    {"name": "John Doe", "age": 30, "city": "New York"},
                    {"name": "Jane Smith", "age": 28, "city": "Los Angeles"},
                    {"name": "Mike Johnson", "age": 35, "city": "Chicago"}
                ]
            }
            json.dump(data, f, indent=2)
            # json.dump(data,f)
    except Exception as e:
        print("An error occurred:", e)

def read_json_from_memory():
    data = '{\
        "employees": [\
            {"name": "John Doe", "age": 30, "city": "New York"},\
            {"name": "Jane Smith", "age": 28, "city": "Los Angeles"},\
            {"name": "Mike Johnson", "age": 35, "city": "Chicago"}\
        ]\
    }'
    try:
        info = json.loads(data)
        print(info)
    except json.JSONDecodeError:
        print("Invalid JSON")

def write_json_from_memory():
    data = {
        "employees": [
            {"name": "John Doe", "age": 30, "city": "New York"},
            {"name": "Jane Smith", "age": 28, "city": "Los Angeles"},
            {"name": "Mike Johnson", "age": 35, "city": "Chicago"}
        ]
    }
    try:
        print(json.dumps(data))
    except Exception as e:
        print("An error occurred:", e)

def read_csv():
    try:
        with open(r"C:\Samples\VP-2024\week8\info.csv","r") as f:
            reader = csv.reader(f)
            for row in reader:
                print(row)
    except FileNotFoundError:
        print("File not found")
    except csv.Error as e:
        print("Invalid CSV format:", e)
    except Exception as e:
        print("An error occurred:", e)

def write_csv():
    try:
        with open(r"C:\Samples\VP-2024\week8\info.out.csv","w", newline='') as f:
            writer = csv.writer(f)
            writer.writerow(["Name", "Age", "City"])
            writer.writerows([
                ("John", 30, "New York"),
                ("Peter", 20, "Sofia"),
                ("Ivan", 35, "Plovdiv")
            ])
    except Exception as e:
        print("An error occurred:", e)

        
if __name__ == "__main__":
    # file_operations1()
    # file_operations2()
    # file_operation3()
    # file_operation4()
    # file_operation5()
    # write_numbers()
    # read_numbers()
    # read_json()
    # write_json()
    # read_json_from_memory()
    # write_json_from_memory()
    # read_csv()
    write_csv()