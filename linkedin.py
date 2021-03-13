from urllib.request import urlopen  
from bs4 import BeautifulSoup
import re

def getJob(role):
    jobsDictionary = {
        'success': True,
        'role': role,
        'data': []
    }
    jobs = []
    company_name = []
    location = []
    snippet = []
    l = []
    p = re.compile('at-([A-Za-z-$]*)')
    for i in range(0,100,25):
        html = urlopen('https://www.linkedin.com/jobs/search/?keywords={0}&start={1}'.format(role, str(i)))
        
        bsyc = BeautifulSoup(html.read(), "lxml")
        for c in bsyc.findAll('span', { "class" : "screen-reader-text" } ):
            jobs.extend(c.contents)
        for c in bsyc.findAll('span',{'class':'job-result-card__location'}):
            location.extend(c.contents)
        for c in bsyc.findAll('p',{'class':'job-result-card__snippet'}):
            snippet.extend(c.contents)
        for c in bsyc.findAll('a', { "class" : "result-card__full-card-link" } ):
            l.append(c.get('href'))
    for st in l:
        result = p.search(st)
        company_name.append(result.group(1).replace('-'," ").strip())
    for company in range(len(company_name)):
        jobsObject = {
            'Company': company_name[company],
            'Profile': jobs[company],
            'location': location[company],
            'snippet': snippet[company]
        }

        jobsDictionary['data'].append(jobsObject)

       
        
    return jobsDictionary