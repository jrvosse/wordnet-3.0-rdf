wnfull-schema.ttl: full-partial.ttl ../wncommon-schema.ttl Makefile
	cp full-partial.ttl $@
	cat ../wncommon-schema.ttl | egrep -v '^#|^@' >> $@
