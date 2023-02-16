import json
import csv

with open( "C:\\Users\\user\\PycharmProjects\\APITestDemo\\employee.json") as json_file:
     json_data = json.load(json_file)


     data_file =open('C:\\Users\\user\\PycharmProjects\\APITestDemo\\employee.csv','w', newline='')
     csv_writer= csv.writer(data_file)

     count =0
     for data in json_data['Employees']:
         if count==0:
             header = data.keys()
             csv_writer.writerow(header)
             count +=1
         csv_writer.writerow(data.values())
     data_file.close()