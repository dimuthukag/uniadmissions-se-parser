import csv

class Exporter:
    def __init__(self,courseList:list,exportFileName:str='output'):
        self.__courseList=courseList
        self.__exportFileName = exportFileName

    def toCsv(self)->None:
        if not self.__courseList:
                return  # Handle empty list case

        fieldnames = self.__courseList[0].keys()  # Get keys from the first dictionary

        with open(f'{self.__exportFileName}.csv', 'w', newline='', encoding='utf-8') as csvfile:
            writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
            writer.writeheader()  # Write the column headers
            writer.writerows(self.__courseList)  # Write the data rows
