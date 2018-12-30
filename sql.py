import sqlite3
import os

# less typing for me
workingDir = os.path.dirname(os.path.realpath(__file__))

connection = sqlite3.connect(workingDir + '/database.db')
cursor = connection.cursor()

cursor.execute('''
    CREATE TABLE IF NOT EXISTS `
''')

connection.close()

# fall term (20xx90)
# winter term (20xx10)
# summer term (20xx50)

# XXXX = year (2019)
# YY = month - trailing zeroes (50 - April) (12 - Dec)
# AAAA = subject (MATH)
# BBBB = number (1240)

# https://aurora.umanitoba.ca/banprod/bwckctlg.p_disp_course_detail?cat_term_in=XXXXYY&subj_code_in=AAA&crse_numb_in=BBBB