help:
	@echo "###"
	@echo "# Build targets for WenKai"
	@echo "###"
	@echo
	@echo "  make build: Builds the fonts and places them in the fonts/ directory"
	@echo

venv: venv/touchfile

merge:
	. venv/bin/activate; ./sources/build.sh;

export:
	. venv/bin/activate; gftools builder sources/project.yaml;

build: venv merge export
	. venv/bin/activate; python3 sources/shared/scripts/post.py;

venv/touchfile: requirements.txt
	test -d venv || python3 -m venv venv
	. venv/bin/activate; pip install -Ur requirements.txt
	touch venv/touchfile

clean:
	rm -rf venv
	find -iname "*.ufo" -delete
	find -iname "*.pyc" -delete
