.PHONY: build install uninstall bump-version

PREFIX=${HOME}/.local
version:=v$(shell date -u +%H%M%S.%Y-%m-%d)

install: bump-version build
	mkdir -p              $(PREFIX)/bin
	cp bin/my-app.py      $(PREFIX)/bin/my-app
	mkdir -p              $(PREFIX)/share/applications	
	cp bin/my-app.desktop $(PREFIX)/share/applications/my-app.desktop
	@-update-desktop-database $(PREFIX)/share/applications
	# ensure app is installed
	which my-app 2>/dev/null

uninstall:
	rm -f $(PREFIX)/bin/my-app
	rm -f $(PREFIX)/share/applications/my-app*
	@-update-desktop-database $(PREFIX)/share/applications
	# ensure app is gone
	! which my-app 2>/dev/null

build:
	black .

bump-version:
	@echo updating version to $(version)
	@sed -i 's/Name=MyApp.*/Name=MyApp $(version)/'          bin/my-app.desktop
	@sed -i 's/app_version = ".*"/app_version="$(version)"/' bin/my-app.py
