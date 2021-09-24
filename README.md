# lior-bootstrap

Image Processing Samples

## develop env setup

> install environent

```bash
task deps:install
```

> to activate use `conda activate local-ci-config-cenv`

## test

`task run-tests`
`task -d tests -l`

- [ More on tests](./tests/README.md)

# Usage

- `❯ python liorboot/flipper.py Backchannel-Lena-Soderberg-FA.jpg --text dudu --dbgout`
- `❯ python liorboot/flipper.py Backchannel-Lena-Soderberg-FA.jpg --dest-path lenoa._out.jpg`
