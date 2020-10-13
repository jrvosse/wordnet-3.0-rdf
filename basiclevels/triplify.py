#!/usr/bin/env python

import sys
import re

def main():
    basics_file = open ("basiclevels.txt", "r")
    p = re.compile("(Synset)\('(.*)'\)\t(.*)")
    n = re.compile("\.n\.")
    print("@prefix wn30:  <http://purl.org/vocabularies/princeton/wn30/> .")
    print("@prefix cgraph: <http://purl.org/vocabularies/cgraph/> .")
    for line in basics_file:
        (synset, sid, lemma) = p.match(line).groups()
        (l, ns) = n.split(sid)
        normalized1 = lemma.replace('\'', '_')
        normalized2 = normalized1.replace('/', '_')
        normalized  = normalized2.replace('.', '_')
        nn = int(ns)
        print("wn30:synset-%s-noun-%d a cgraph:BasicLevelSynset ." % (normalized,nn))

if __name__== "__main__":
    main()
