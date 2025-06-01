import csv
import pandas as pd

class Exporter:
    def __init__(self,courseList:list,exportFileName:str='output'):
        self.__courseList=courseList
        self.__exportFileName = exportFileName

    def toCsv(self)->None:
        if not self.__exportFileName:
            return
        df = pd.DataFrame(self.__courseList)
        df.to_csv(f'{self.__exportFileName}.csv', index=False)

    def toExcel(self)->None:
        if not self.__courseList:
            return
        df = pd.DataFrame(self.__courseList)
        df.to_excel(f'{self.__exportFileName}.xlsx',index=False)