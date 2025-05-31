import requests
from bs4 import BeautifulSoup

class Query:
    def __init__(self):
        self.__courseType=''
        self.__courseLevel=''
        self.__courseStudyPace=''
        self.__courseLanguage=''
        self.__courseKeyword=''
        self.__queryString=''

    @property
    def queryCourseType(self)->str:
        return self.__courseType
    
    @queryCourseType.setter
    def queryCourseType(self,courseType:str)->None:
        self.__courseType=courseType
        self.build()

    @property
    def queryCourseLevel(self)->str:
        return self.__courseLevel
    
    @queryCourseLevel.setter
    def queryCourseLevel(self,courseLevel:str)->None:
        self.__courseLevel=courseLevel
        self.build()

    @property
    def queryCourseStudyPace(self)->str:
        return self.__courseStudyPace
    
    @queryCourseStudyPace.setter
    def queryCourseStudyPace(self,courseStudyPace:str)->None:
        self.__courseStudyPace=courseStudyPace
        self.build()
    
    @property
    def queryCourseLanguage(self)->str:
        return self.__courseLanguage
    
    @queryCourseLanguage.setter
    def queryCourseLanguage(self,courseLanguage:str)->None:
        self.__courseLanguage=courseLanguage
        self.build()

    @property
    def queryCourseKeyword(self)->str:
        return self.__courseKeyword
    
    @queryCourseKeyword.setter
    def queryCourseKeyword(self,courseKeyword:str)->None:
        self.__courseKeyword=f'&freeText={courseKeyword.replace(' ','%20')}'
        self.build()
    
    def build(self)->None:
        self.__queryString=f'{self.queryCourseKeyword}{self.queryCourseType}{self.queryCourseStudyPace}{self.queryCourseLanguage}{self.queryCourseLevel}'
    
    @property
    def get(self)->str:
        return self.__queryString

class Url:
    def __init__(self,query:Query):
        self.__baseURL='https://www.universityadmissions.se'
        self.__path='/intl/search?period=24'
        self.__query=query.get

    def __getBaseURL(self)->str:
        return self.__baseURL

    def __getPath(self)->str:
        return self.__path

    def __getQuery(self)->str:
        return self.__query

    @property
    def get(self)->str:
        return f'{self.__getBaseURL()}{self.__getPath()}{self.__getQuery()}'

class Scraper:
    def __init__(self, url:Url):
        self.__page = requests.get(url.get)
        self.__bs = BeautifulSoup(self.__page.content, "html.parser")
    
    def getCourses(self)->list:
        return self.__bs.find_all("div",class_="searchresultcard")