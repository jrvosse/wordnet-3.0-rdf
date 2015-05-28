How to load the RDF files into your triple store?

I personally use ClioPatria [1] as my triple store, which understands the "void.ttl" file in the distribution. So I only need to say 

	rdf_load_library('wn30-full').

and it will load all the triples I need (and it will load it fast from the compressed .ttl.gz files)!

So assuming you have a triple store without similar VOiD support, you need to to the void-part by hand.  Should not be to difficult if you look at the rdf/void.ttl file in this directory.

So stuff you need for both full and basic versions are the files listed in wn30-common:

                <wordnet-attribute.ttl.gz> ,
                <wordnet-causes.ttl.gz> ,
                <wordnet-classifiedby.ttl.gz> ,
                <wordnet-entailment.ttl.gz> ,
                <wordnet-frame.ttl.gz> ,
                <wordnet-glossary.ttl.gz> ,
                <wordnet-hyponym.ttl.gz> ,
                <wordnet-instances.ttl.gz> ,
                <wordnet-membermeronym.ttl.gz> ,
                <wordnet-partmeronym.ttl.gz> ,
                <wordnet-sameverbgroupas.ttl.gz> ,
                <wordnet-similarity.ttl.gz> ,
                <wordnet-substancemeronym.ttl.gz> ,
                <wordnet-synset.ttl.gz> .

If you do not know if you need basic or full, 
I recommend you to use the basic version (see http://www.w3.org/TR/wordnet-rdf/#basicfull for more info).
In rdf/basic/void.ttl you see this requires just tow extra files:
           <wnbasic-schema.ttl.gz> ,
           <wordnet-senselabels.ttl.gz> .

This should be sufficient for most applications!

For full, you need some more files, see rdf/full/void.ttl for the list.

To enable a SKOS-view, load the mappings provide in
     <wnskosmap.ttl.gz> ,	
     <wordnet-skos-inScheme.ttl.gz> .

[1] http://cliopatria.swi-prolog.org/help/Download.html
