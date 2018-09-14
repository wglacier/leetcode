import os

outfile = 'README.md'
sol_path = './solutions/'

header = """
# LeetCode Solutions by wglacier


## Links:
[Leetcode Algorithms Problems](https://leetcode.com/problemset/algorithms/)  

---

| Problems | Solutions |
|----------|-----------|
"""

with open(outfile, 'w') as outf:
    outf.write(header)
    files = sorted(os.listdir(sol_path))
    for fn in files:
        if not fn.endswith('.md'):
            continue
        fbase = os.path.splitext(fn)[0]
        fname = fbase[6:] # without leading number
        line = '| [{base}](https://leetcode.com/problems/{link}/) | [source](./solutions/{fn}) |'.format(
            base=fbase,
            link=fname.replace('(', '').replace(')', '').replace(' ', '-').lower(),
            fn=fn.replace(' ', '%20')
        )
        outf.write(line + '\n')
        
