import os,re

outfile = 'README.md'
outhtml_name = 'problems.htm'
sol_path = './solutions/'

header = """
# LeetCode Solutions by wglacier


## Links:
[Leetcode Algorithms Problems](https://leetcode.com/problemset/algorithms/)  

---

| No. | Problems |    Level  | Solutions |
|-----|----------|-----------|-----------|
"""

headerHtml = """
<html>
<title> LeetCode Solutions by wglacier </title>
<body>
<table>
    <th>No.</th>
    <th>Problems</th>
    <th>Solutions</th>
    <th>LeetCode Link</th>
"""
outhtml = open(outhtml_name, 'w')

with open(outfile, 'w') as outf:
    outf.write(header)
    outhtml.write(headerHtml)
    files = sorted(os.listdir(sol_path))
    no = 0
    for fn in files:
        if not fn.endswith('.md'):
            continue
        no += 1
        fbase = os.path.splitext(fn)[0]
        fname = fbase[6:] # without leading number
        fnamelink = fname.replace('(', '').replace(')', '').replace(' ', '-').lower()
        fn_name = fn.replace(' ', '%20')
        locallink = './solutions/' + fn_name
        leetlink = 'https://leetcode.com/problems/' + fnamelink
        first_line = open(sol_path + fn, 'r').readline()
        m = re.match(r'^[^,]+,\s*(\w+)',first_line)
        level = m.group(1) if m else ''
        line = '| {no} | <a href="{link}" target="_blank">{base}</a> | {level} | <a href="{fn}" target="_blank">source</a> |'.format(
            no=no,
            base=fbase,
            link=leetlink,
            level=level,
            fn=locallink
        )
        

        outf.write(line + '\n')

        linehtml = """<tr><td>%d</td>
                      <td>%s</td>
                      <td><a href="%s" target="_blank">Solutions</a></td>
                      <td><a href="%s" target="_blank">LeetCode</a></td></tr>\n""" % (
            no, fbase, locallink, leetlink)
        outhtml.write(linehtml)

outhtml.write("</table></body></html>")
outhtml.close()
        
