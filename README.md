[![Test multiple cases](https://github.com/Jalkhov/docs-pro/actions/workflows/multicases_test.yml/badge.svg)](https://github.com/Jalkhov/docs-pro/actions/workflows/multicases_test.yml) [![Lint](https://github.com/Jalkhov/docs-pro/actions/workflows/lint.yml/badge.svg)](https://github.com/Jalkhov/docs-pro/actions/workflows/lint.yml)

# Docs Progress

Calculate the translation percentage of your project, whether it is a single language or several languages. You will be able to get both the percentage of each language separately and the progress of the project in general, you will also have the opportunity to omit the languages you want from the final progress.

Inspired in [i18n coverage](https://github.com/alexkiro/i18n-coverage).

## Usage

### Example workflow

```yaml
name: Calculate translation progress
on: [push, pull_request]
jobs:
  progress-check:
    runs-on: ubuntu-latest
    steps:
      - name: Checkout
        uses: actions/checkout@v2.3.1

      - name: Get Spanish translation progress
        id: es_progress
        uses: Jalkhov/docs-progress@v1.0.0
        with:
          path: "docs/locales/es"
```

### Inputs

| Input                           | Description                                                  | Type     |
| ------------------------------- | ------------------------------------------------------------ | -------- |
| `path`                          | Path to the `.po` files. The action will take ALL existing `.po` files in the given `path`. | `string` |
| `multilang` _(optional)_        | The project have multiple languages. When `True` a dict is returned, ex: `{'es':'30.00', 'en':'12.00'}`. | `bool`   |
| `ignore-languages` _(optional)_ | Check all languages expect this one, comma separated list.   | `string` |

### Outputs

| Output     | Description                                  |
| ---------- | -------------------------------------------- |
| `progress` | Return total progress of the given languages |

### Using the optional input

```yaml
with:
  path: "docs/locales"
  multilang: true
  ignore-languages: "zh_CN"
```

### Using outputs

```yaml
name: Calculate translation progress
on: [push, pull_request]
jobs:
  progress-check:
    runs-on: ubuntu-latest
    steps:
      - name: Checkout
        uses: actions/checkout@v2.3.1

      - name: Get Spanish translation progress
        id: es_progress
        uses: Jalkhov/docs-progress@v1.0.0
        with:
          path: "docs/locales/es"

      - name: Check outputs
            run: |
                  echo "Outputs - ${{ steps.es_progress.outputs.progress }}"
```

## Want more examples?
Check [multiple cases workflow](.github/workflows/multicases_test.yml)

## TODO
- [ ] Generate/Deploy badges option
- [ ] Show final checks
