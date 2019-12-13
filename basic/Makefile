wnbasic-schema.ttl: basic-partial.ttl ../wncommon-schema.ttl Makefile
	cp basic-partial.ttl $@
	cat ../wncommon-schema.ttl | egrep -v '^#|^@' >> $@
