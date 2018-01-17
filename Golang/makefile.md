# Описание создания makefile

На основании статьи: https://oppodelldog.github.io/posts/go-makefile/


Пример Makefile

```makefile

setup: ## Install all the build and lint dependencies
	go get -u gopkg.in/alecthomas/gometalinter.v2
	go get -u github.com/golang/dep/cmd/dep
	go get -u golang.org/x/tools/cmd/cover
	go get -u golang.org/x/tools/cmd/goimports


build: ## Build a beta version
	go build -race -o ./dist/logreplay ./main.go

run: ## Build a beta version
	go run -race -o ./dist/logreplay ./main.go

install: ## Install to $GOPATH/src
	go install ./...

```

Пример запуска:

```
make run
```
