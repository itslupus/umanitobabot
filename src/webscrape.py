from lxml import html
import requests

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

        results = {}
        results['title'] = page.xpath('//td[@class="nttitle"]/text()')
        results['desc'] = page.xpath('//td[@class="ntdefault"]/text()')

        return results

    return None

