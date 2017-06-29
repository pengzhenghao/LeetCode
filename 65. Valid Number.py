import re
class Solution(object):
    def isNumber(self, s):
        pattern=re.compile(r"(-?|\+?)[0-9]+\.[0-9]*e(-?|\+?)[0-9]+|(-?|\+?)\.[0-9]+e(-?|\+?)[0-9]+|(-?|\+?)[0-9]*\.[0-9]+|(-?|\+?)[0-9]+\.[0-9]*|(-?|\+?)[0-9]+\.?e(-?|\+?)[0-9]+|(-?|\+?)[0-9]+")
        result=re.match(pattern,s.strip())
        if result:
            if result.group(0)==s.strip():
                return True
        return False
