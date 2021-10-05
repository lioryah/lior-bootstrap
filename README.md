# About

Image Processing Samples

## Get Started

> - Take look on the [Demo Notebook](./demo.ipynb)
> - Checkout [Documentation Site](https://yairdar.github.io/lior-bootstrap---a926e7b3b)

## develop env setup

> install environent

```bash
task deps:install
```

> to activate use `conda activate local-ci-config-cenv`

## Usage

> get help `python liorboot/flipper.py --help`

> sample usage `task run-sample --dry`

### live documentaion

> `task mkdocs:serve`

### cli usages

```bash
# task: [run-sample]
python liorboot/flipper.py \
  Backchannel-Lena-Soderberg-FA.jpg \
  --dest-path Backchannel-Lena-Soderberg-FA.jpg.run-sample._out.jpg
```

```bash
python liorboot/flipper.py Backchannel-Lena-Soderberg-FA.jpg --text dudu --dest-path readme.usage._out.jpg
python liorboot/flipper.py Backchannel-Lena-Soderberg-FA.jpg --dest-suff .lenoa._out.jpg
```

## test

- `task run-tests`
- `task -d tests -l`
- [ More on tests](./tests/README.md)

## misc

versions=https://openbase.com/js/mermaid/versions
