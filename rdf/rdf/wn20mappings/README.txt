Mappings from Wordnet 3.0 synsets to Wordnet 2.0 synsets.

Note:  The mappings in this folder are not based on any Princeton sourcefile.
All erroneous mappings are my responsibility, not Princetons.

Mapping statistics and origin:
The mappings in this folder have been created in multiple steps.
The result of each step is reflected in a separate file.

In the RDF version we have 117,659 Wordnet 3.0 synsets to be mapped.

Step one: detecting new labels (3,364).
I've detected 3,364 Wordnet 3.0 synsets with an rdfs:label that does not appear as a label in Wordnet 2.0.
I assume these are all new synsets in 3.0 that should _not_ be mapped to 2.0.
These synsets will be ignored in the following steps.
Results are in file: label-new.ttl 

Step two: detecting synsets with identical label and gloss (102,964)
I've detected 102,964 Wordnet 3.0 synsets of which there is at least one Wordnet 2.0 synset
with both an identical label and gloss. I assume these synsets correspond.  See comments in 
the result file for more detail on how ambiguity is handled. Note that this step covers already around 87% of all sysnets.
Results are in file: glossmatches.ttl 

Step tree: detecting synsets with identical label and strong family resemblences.
For all the 3.0 synsets not mapped already, I've looked at 2.0 synsets that have identical labels and:
1. Both have a matching broader and narrower synset in the hyponym that was already matched by an earlier step.
   Results are in file: label-childparent-matches.ttl (1,280/1.559).
2. Only have a broader (based on hyponym or instance) match.
   Results are in file: label-parent-matches.ttl (4,228/4.754).
   Results are in file: label-instance-matches.ttl (805/871).
3. Only have a narrower match.
   Results are in file: label-child-matches.ttl (349/151).
4. If non of the above applies, but a label accurs only once in wn30 and only once in wn20, we consider the corresponding synsets to match as well.
   Results are in file: label-unique-matches.ttl (1342/921).
4. Before saving the above 3 results, we have removed the 131 (143) synsets for which this step three resulted in ambiguous alignments, and saved this ambigous mappings in a separate file.
   Results are in file: ambiguous-label-pc-matches.ttl

Step four: rerun step three multiple times to take advantage of the new mappings generated.  Repeat until no new mappings
are found (this was the case after two repetitions).  The second number in the statics shows the number on which this stabelizes.  

This leaves us with 117659 - 102964 - 1559 - 4754 - 871 - 151 - 921 = 6439 unmapped synsets.
Of these we have assumed 3,364 to be new, which leaves 6439 - 3364 = 3075 missing synset mappings (< 2.62 %).

A quick manual inspection showed that many of these are named entities, and many are synsets of which both the gloss and the position in the hierarchy changed.  I suspect of the missing 4660, some extra can be found by taking into account that step one now only finds 100% matching glosses, while many glosses have changed only minorly in terms of capitalization, punctiation or correcting typing errors.  

Jacco van Ossenbruggen
VU University Amsterdam
May 2010
