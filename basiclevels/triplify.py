import sys
import re

def main():
    basics_file = open ("basiclevels.txt", "r")
    p = re.compile("(\"Synset)\('(.*)'\)")
    n = re.compile("\.n\.")
    print "@prefix wn30:  <http://purl.org/vocabularies/princeton/wn30/> ."
    print "@prefix cgraph: <http://purl.org/vocabularies/cgraph/> ."
    for line in basics_file:
        (synset, sid) = p.match(line).groups()
        (l, ns) = n.split(sid)
        normalized1 = l.replace('\'', '_')
        normalized = normalized1.replace('/', '_')
        nn = int(ns)
        print("wn30:synset-%s-noun-%d a cgraph:BasicLevelSynset ." % (normalized,nn))

if __name__== "__main__":
    main()
