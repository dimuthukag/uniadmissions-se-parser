class CourseType:
    def __init__(self):
        self.__both=''
        self.__courses='&type=courses'
        self.__programmes='&type=programs'

    @property
    def both(self)->str:
        return self.__both

    @property
    def courses(self)->str:
        return self.__courses

    @property
    def programmes(self)->str:
        return self.__programmes
    
class CourseLevel:
    def __init__(self):
        self.__preparatoryLevel='&basicLevel=true'
        self.__bachelorsLevel='&graduateLevel=true'
        self.__mastersLevel='&advancedLevel=true'
        self.__noPrerequisite='&noPrerequisite=true'
        self.__multiLevel=''

    @property
    def preparatoryLevel(self)->str:
        return self.__preparatoryLevel
    
    @property
    def bachelorsLevel(self)->str:
        return self.__bachelorsLevel

    @property
    def mastersLevel(self)->str:
        return self.__mastersLevel

    @property
    def noPrerequisite(self)->str:
        return self.__noPrerequisite
    
    def __buildMultiLevelQuery(self,queryString:str)->None:
        try:
            if queryString.__len__()!=0:
                self.__multiLevel+=queryString
        except TypeError:
            print("Error:")

    def multiLevel(self,preparatoryLevel:bool=False,bachelorsLevel:bool=False,mastersLevel:bool=False,noPrerequisite:bool=False)->str:
        if preparatoryLevel:
            self.__buildMultiLevelQuery(self.preparatoryLevel)
        if bachelorsLevel:
            self.__buildMultiLevelQuery(self.bachelorsLevel)
        if mastersLevel:
            self.__buildMultiLevelQuery(self.mastersLevel)
        if noPrerequisite:
            self.__buildMultiLevelQuery(self.noPrerequisite)
        return self.__multiLevel
    
class CourseStudyPace:
    def __init__(self):
        self.__fullTime='&pace=full_time'
        self.__upTo75Percent='&pace=up_to_75'
        self.__upTo50Percent='&pace=up_to_50'
        self.__upTo25Percent='&pace=up_to_75'

    @property
    def fullTime(self)->str:
        return self.__fullTime
    
    @property
    def upTo75Percent(self)->str:
        return self.__upTo75Percent
    
    @property
    def upTo50Percent(self)->str:
        return self.__upTo50Percent
    
    @property
    def upTo25Percent(self)->str:
        return self.__upTo25Percent
    
class CourseLanguage:
    def __init__(self):
        self.__all=''
        self.__english='&languageOfInstruction=en'
        self.__swedish='&languageOfInstruction=sv'
        self.__other='&languageOfInstruction=other'

    @property
    def all(self)->str:
        return self.__all
    
    @property
    def english(self)->str:
        return self.__english
    
    @property
    def swedish(self)->str:
        return self.__swedish
    
    @property
    def other(self)->str:
        return self.__other