pretty_pre-commit:
	yq r --prettyPrint .pre-commit-config.yaml > .pre-commit-config.yaml.bak
	mv .pre-commit-config.yaml.bak .pre-commit-config.yaml
	git add .pre-commit-config.yaml
