import pandas as pd

class Exporter:
    def __init__(self,courseList:list,exportFileName:str='output'):
        self.__courseList=courseList
        self.__exportFileName = exportFileName
        self.__dataFrame = pd.DataFrame(self.__courseList)

    def toCsv(self)->None:
        if not self.__exportFileName:
            return
        self.__dataFrame.to_csv(f'{self.__exportFileName}.csv', index=False)

    def toExcel(self)->None:
        if not self.__courseList:
            return
        self.__dataFrame.to_excel(f'{self.__exportFileName}.xlsx',index=False)