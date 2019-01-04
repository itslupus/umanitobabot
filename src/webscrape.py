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

        description = page.xpath('//td[@class="ntdefault"]/text()')[0]

        results = {}
        results['title'] = page.xpath('//td[@class="nttitle"]/text()')[0]
        results['desc'] = description
        results['notHeld'] = findNotHeld(description)
        results['preReq'] = findPrereq(description)

        return results

    return None

def findNotHeld(desc):
    match = re.findall(r'(?<=May not be held with )(.*?)\.', desc)
    return match

def findPrereq(desc):
    # regex HELL
    match = re.findall(r'(?:(?<=Prerequisite: )|(?<=Prerequisites: ))(.*?)\.', desc)
    return match
