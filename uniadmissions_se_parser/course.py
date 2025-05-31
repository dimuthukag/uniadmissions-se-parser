import re
from bs4 import BeautifulSoup

class Course:
    def __init__(self,htmlContent:BeautifulSoup):
        self.__htmlContent=htmlContent
        self.__courseDetails={
            'Application Code':'',
            'Name':'',
            'Level':'',
            'University':'',
            'Location':'',            
            'No: of Credits':0,
            'Subject Areas':'',
            'Period':'',
            'Start Date':'',
            'Language':'',
            'Teaching Form':'',
            'Pace of Study':'',
            'Instructional Time':'',
            'First Tution Fee Installment':0,
            'Total Tution Fee':0,
            'Link':''
        }
        self.__parse()
    
    '''
    @property
    def name(self)->str:
        return self.__name
    
    @property
    def university(self)->str:
        return self.__university
    
    @property
    def noCredits(self)->str:
        return self.__nCredits
    
    @property
    def location(self)->str:
        return self.__location
    
    @property
    def firstTutionFeeInstallment(self)->str:
        return self.__firstTutionFeeInstallment
    
    @property
    def totalTutionFee(self)->str:
        return self.__totalTutionFee
    
    @property
    def period(self)->str:
        return self.__period
    
    @property
    def startDate(self)->str:
        return self.__startDate
    
    @property
    def level(self)->str:
        return self.__level
    
    @property
    def language(self)->str:
        return self.__language
    
    @property
    def applicationCode(self)->str:
        return self.__applicationCode
    
    @property
    def teachingForm(self)->str:
        return self.__teachingForm
    
    @property
    def studyPace(self)->str:
        return self.__studyPace
    
    @property
    def instructionTime(self)->str:
        return self.__instructionTime
    
    @property
    def subjectAreas(self)->str:
        return self.__subjectAreas
    
    @property
    def link(self)->str:
        return self.__link '''

    def __parse(self)->None:
        self.__courseDetails['Name']=self.__htmlContent.find("h3",class_="headline4").text
        self.__courseDetails['No: of Credits']= str(self.__htmlContent.find("p",class_="universal_medium").text).split(",")[0].replace("Credits","").strip()
        self.__courseDetails['University']= str(self.__htmlContent.find("p",class_="universal_medium").text).split(",")[1].strip()
        self.__courseDetails['Location']= str(self.__htmlContent.find("p",class_="universal_medium").text).split(",")[2].replace("Location:","").strip()
        
        _courseDetails = str(self.__htmlContent.find("div",class_="resultcard_expanded").text)

        self.__courseDetails['First Tution Fee Installment'] = str(re.findall(r'First tuition fee instalment:\n(\d{1,3},?\d{3})',_courseDetails)[0]).replace(",","")
        self.__courseDetails['Total Tution Fee'] = str(re.findall(r'Total tuition fee:\n(\d{1,3},?\d{3})',_courseDetails)[0]).replace(",","")
        self.__courseDetails['Period'] = str(re.findall(r'Period:\n([a-zA-Z]{4,8}\n\d{4}\sPeriod\s\d{1})',_courseDetails)[0]).replace(",","").replace("\n",' ')
        
        try:
            self.__courseDetails['Start Date'] = str(re.findall(r'Course starts:\n(\d{1,2}\s[a-zA-Z]{3,4})',_courseDetails)[0]).replace(",","")
        except IndexError:
            self.__courseDetails['Start Date'] = 'n/a'
        self.__courseDetails['Level'] = str(re.findall(r'Level:\n(.+)\n',_courseDetails)[0])
        self.__courseDetails['Language'] = str(re.findall(r'Language of instruction:\n([a-zA-Z]+)\n',_courseDetails)[0])
        self.__courseDetails['Application Code'] = str(re.findall(r'Application code:\n(.+)\n',_courseDetails)[0])
        self.__courseDetails['Teaching Form'] = str(re.findall(r'Teaching form:\n(.+\n.+)\n',_courseDetails)[0]).replace('\n',' ')
        self.__courseDetails['Pace of Study'] = str(re.findall(r'Pace of study:\n(.+)\n',_courseDetails)[0]).replace('\n',' ')
        self.__courseDetails['Instructional Time'] = str(re.findall(r'Instructional time:\n(.+)\n',_courseDetails)[0]).replace('\n',' ')
        self.__courseDetails['Subject Areas'] = str(re.findall(r'Subject Areas:\n(.+)\n',_courseDetails)[0]).replace('\n',' ')
        self.__courseDetails['Link'] = self.__htmlContent.find("a",class_="external")["href"]
        
    def details(self)->dict:
        return self.__courseDetails