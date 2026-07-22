APP_NAME = keepalive
VENV = venv
BINARY = dist/$(APP_NAME)

.PHONY: all build clean release

all: build

build: $(BINARY)

$(BINARY): keepalive.py
	$(VENV)/bin/pip install -q pyinstaller
	$(VENV)/bin/pyinstaller --onefile --name $(APP_NAME) keepalive.py

clean:
	rm -rf build dist *.spec

release:
	@[ "${VERSION}" ] || ( echo "Usage: make release VERSION=1.0.0"; exit 1 )
	git tag v$(VERSION)
	git push origin v$(VERSION)
	@echo ""
	@echo "✅ Tag v$(VERSION) pushed."
	@echo "   Create release on GitHub:"
	@echo "   https://github.com/$$(git remote get-url origin | sed 's|.*[:/]\(.*\)/\(.*\).git|\1/\2|')/releases/new?tag=v$(VERSION)"
	@echo "   Attach: dist/$(APP_NAME)"
