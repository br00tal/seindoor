# Basic Makefile that simply installs seindoor to the default location

PREFIX=/usr
ETCPREFIX=/etc

install:
	mkdir -p $(ETCPREFIX)/seindoor
	install -m 755 seindoor.py $(PREFIX)/bin
	install -m 644 seindoor.conf $(ETCPREFIX)/seindoor
	install -m 644 seindoor@.service $(ETCPREFIX)/systemd/system

uninstall:
	rm -rf $(PREFIX)/bin/seindoor.py
	rm -rf $(ETCPREFIX)/seindoor/seindoor.conf
	rm -rf $(ETCPREFIX)/systemd/system/seindoor@.service

.PHONY: install uninstall
