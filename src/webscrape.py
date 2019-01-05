from lxml import html

import requests
import re

def getAuroraCourse(subject, number):
    # 1.1 = year (2019)
    # 1.2 = month - trailing zeroes (50 - April) (12 - Dec)

    # 2 = subject (MATH)
    # 3 = number (1240)

    term = '201910'
    reqURL = 'https://aurora.umanitoba.ca/banprod/bwckctlg.p_disp_course_detail?cat_term_in=' + term + '&subj_code_in=' + subject + '&crse_numb_in=' + number

    response = requests.get(reqURL)
    if (response.status_code == 200):
        page = html.fromstring(response.content)

        title = page.xpath('//td[@class="nttitle"]/text()')
        summary = page.xpath('//td[@class="ntdefault"]/text()')[0].strip()

        if (len(title) == 0):
            return None
            
        results = {}
        results['title'] = title[0]
        results['desc'] = findDescription(summary)
        results['notHeld'] = findNotHeld(summary)
        results['preReq'] = findPrereq(summary)

        return results

    return None

# TODO need to redo these regex
def findDescription(summary):
    match = re.findall(r'(.*?)(?:(?= Préalable)|(?= Prerequisite)|(?= May not be held with)|(?= Not to be held with)|(?= On ne peut se faire créditer))', summary)
    
    if (len(match) == 0):
        return 'None'
    
    return match[0]

def findNotHeld(summary):
    match = re.findall(r'(?:(?<=On ne peut se faire créditer )|(?<=Not to be held with )|(?<=May not be held with ))(.*?)\.', summary)
    
    if (len(match) == 0):
        return 'None'
    
    return match[0]

def findPrereq(summary):
    # regex HELL
    match = re.findall(r'(?:(?<=Prerequisite: )|(?<=Prerequisites: )|(?<=Préalable : ))(.*?)\.', summary)
    
    if (len(match) == 0):
        return 'None'
    
    return match[0]