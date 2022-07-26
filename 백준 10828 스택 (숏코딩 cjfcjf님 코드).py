# 백준 10828 스택 (숏코딩 cjfcjf님 코드)

import sys
s,p=[],print
for a in sys.stdin.readlines()[1:]:
 a=a.strip()
 if 'z'in a:p(len(s))
 elif 'm'in a:p((not s)*1)
 elif 'h'in a:s+=int(a[5:]),
 else:
  p(s[-1] if s else -1)
  if a=='pop'and s:s.pop()