from uniadmissions_se_parser import filter,scrape,course,export

QUERY = scrape.Query()
QUERY.queryCourseType=filter.CourseType().programmes
QUERY.queryCourseLevel=filter.CourseLevel().mastersLevel
QUERY.queryCourseStudyPace=filter.CourseStudyPace().fullTime
QUERY.queryCourseLanguage=filter.CourseLanguage().english

QUERY.queryCourseKeyword='Bio Medical'

URL = scrape.Url(QUERY)
SCRAPER = scrape.Scraper(URL)

courseList = []

for _C in SCRAPER.getCourses():
    
    COURSE=course.Course(_C)
    courseList.append(COURSE.details())

EXPORTER=export.Exporter(courseList)
EXPORTER.toCsv()