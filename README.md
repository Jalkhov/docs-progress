[![Test multiple cases](https://github.com/Jalkhov/docs-pro/actions/workflows/multicases_test.yml/badge.svg)](https://github.com/Jalkhov/docs-pro/actions/workflows/multicases_test.yml) [![Basic usage example](https://github.com/Jalkhov/docs-pro/actions/workflows/simple_example.yml/badge.svg)](https://github.com/Jalkhov/docs-pro/actions/workflows/simple_example.yml) [![Lint](https://github.com/Jalkhov/docs-pro/actions/workflows/lint.yml/badge.svg)](https://github.com/Jalkhov/docs-pro/actions/workflows/lint.yml)

# Docspro

Calculate the translation percentage of your project, whether it is a single language or several languages. You will be able to get both the percentage of each language separately and the progress of the project in general, you will also have the opportunity to omit the languages you want from the final progress.

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
        uses: actions/checkout@master

      - name: Get Spanish translation progress
        id: es_progress
        uses: Jalkhov/docs-pro@master
        with:
          path: "docs/locales/es"
```

### Inputs

| Input                           | Description                                               | Type     |
| ------------------------------- | --------------------------------------------------------- | -------- |
| `path`                          | Path to the `.po` files                                   | `string` |
| `multilang` _(optional)_        | The project have multiple languages                       | `bool`   |
| `ignore-languages` _(optional)_ | Check all languages expect this one, comma separated list | `string` |

### Outputs

| Output     | Description                                  |
| ---------- | -------------------------------------------- |
| `progress` | Return total progress of the given languages |

## Examples

### Using the optional input

This is how to use the optional input.

```yaml
with:
  path: "docs/locales"
  multilang: true
  ignore-languages: "zh_CN"
```

### Using outputs

Show people how to use your outputs in another action.

```yaml
name: Calculate translation progress
on: [push, pull_request]
jobs:
  progress-check:
    runs-on: ubuntu-latest
    steps:
      - name: Checkout
        uses: actions/checkout@master

      - name: Get Spanish translation progress
        id: es_progress
        uses: Jalkhov/docs-pro@master
        with:
          path: "docs/locales/es"

      - name: Check outputs
            run: |
            echo "Outputs - ${{ steps.es_progress.outputs.progress }}"
```
