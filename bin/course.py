from lxml import html
import requests

xxxx = '201910'
yyyy = 'COMP'
zzzz = '2160'
requestURL = 'https://aurora.umanitoba.ca/banprod/bwckctlg.p_disp_course_detail?cat_term_in=' + xxxx + '&subj_code_in=' + yyyy + '&crse_numb_in=' + zzzz
response = requests.get(requestURL)
if (response.status_code == 200):
    page = html.fromstring(response.content)
    title = page.xpath('//td[@class="nttitle"]/text()')
    desc = page.xpath('//td[@class="ntdefault"]/text()')

    print(title)
    print(desc[0])

# fall term (20xx90)
# winter term (20xx10)
# summer term (20xx50)

# XXXX = year (2019)
# YY = month - trailing zeroes (50 - April) (12 - Dec)
# AAAA = subject (MATH)
# BBBB = number (1240)

# https://aurora.umanitoba.ca/banprod/bwckctlg.p_disp_course_detail?cat_term_in=XXXXYY&subj_code_in=AAA&crse_numb_in=BBBB