import os
from lxml import html
import requests

root = html.fromstring(open("/Users/glacier/work/leetcode/problem_list_all.htm").read())

rows = root.xpath('//tbody[contains(@class, "reactable-data")]/tr')

#base = '/Users/glacier/work/leetcode/unsolved/'
base = '/Users/glacier/work/leetcode/solutions/'
ss = dict({(a[:4],a) for a in os.listdir('/Users/glacier/work/leetcode/solutions/')})
for rr in rows:    
    no = int(rr.getchildren()[1].text)
    no = f'{no:04d}'
    title = rr.getchildren()[2].attrib['value']
    acc_rate = float(rr.getchildren()[4].attrib['value'])  # acc rate
    difficulty = rr.getchildren()[5].getchildren()[0].text.lower()  # difficulty          
    freq = rr.getchildren()[6].find('div').find('div').attrib['style'][7:9] #['value'])  # freq
    link = rr.getchildren()[2].find('div/a').get('href')  # link: /problems/fraction-to-recurring-decimal

    lock = rr.getchildren()[2].find('div/span/i')
    if lock is not None and lock.get('class').find('fa-unlock') > 0:
        lock = 'locked'
    else:
        lock = ''
    fn = f'{no}. {title}.md'
    line1 = f'# {no}. {title}, {difficulty}, {lock}, freq: {freq}%, acceptance: {acc_rate:0.1f}%\n\n'
    text = f'{line1}\n```c++\n// \n\n```\n'
    if no in ss:
        fn = base + ss[no]
        content = open(fn,'r').read()
        if content.find(title) < 0:
            print("changing " + title)
            atime = os.path.getatime(fn)
            mtime = os.path.getmtime(fn)
            with open(fn, 'w') as f:
                f.write(line1)
                f.write(content)
            os.utime(fn, (atime, mtime))


