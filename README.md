# jinja2-template-action
Use Jinja2 template engine on multipe files as a GitHub action.

[![Continuous Testing](https://github.com/fletort/jinja2-template-action/actions/workflows/test.yml/badge.svg)](https://github.com/fletort/jinja2-template-action/actions/workflows/test.yml)
[![Coverage Status](https://coveralls.io/repos/github/fletort/jinja2-template-action/badge.svg?branch=main)](https://coveralls.io/github/fletort/jinja2-template-action?branch=main)
[![Testspace tests count](https://img.shields.io/testspace/total/fletort/fletort%3Ajinja2-template-action/main)](https://fletort.testspace.com/projects/68162/spaces)

This is a very simple version of the action, that is ok for my first need.
Futur enhancement will come.

The actual "simple" version transform all local j2 files (recursively) ('*.j2')
with the jinja2 library.

The new file name is the same filename without the j2 extension.
For exemple, `README.md.j2` becomes `README.md`.

It this version, it can only be used with environment variable, see my [test template file](./test/template.j2).

Environement variable as used as with the jinja2 cli, with a _kind_ of `environ` method :
```
{{ environ('TEST') }}
```

## Usage

### Using Environment Variable

```yaml
- uses: fletort/jinja2-template-action@v1
  env:
    TEST: my_value
```

Environment variables are used as with jinja2 cli:
```
{{ environ('TEST') }}
```
Or as other contextual github information:
```
{{ env.TEST }}
```

### Using Input Variables

```yaml
- uses: fletort/jinja2-template-action@v1
  with:
    variables: |
      TEST1=mytest
      TEST2=isfunny
```

### Using Data Files

```yaml
- uses: fletort/jinja2-template-action@v1
  with:
    data_file: my_data.json
    data_format: json # can be detected automatically (see below)
```

Possible data type are: env, yaml, json, ini

#### 1. env file

```file
EXEMPLE_SMART=yoyo
EXEMPLE_MY_VAR=True
```

#### 2. ini

```file
[EXEMPLE]
SMART=yoyo
MY_VAR=True
```

#### 3. yaml

```file
---
EXEMPLE:
  SMART=yoyo
  MY_VAR=True
```

#### 4. json

```file
{
  "EXEMPLE": {
    "SMART": "yoyo",
    "MY_VAR": True
  }
}
```

#### Related Jinja Template

For previous INI, YAML, JSON examples, jinja template will be:
```
{{ EXEMPLE.SMART }}
{{ EXEMPLE.MY_VAR }}
```

For previous ENV example, jinja template will be:
```
{{ EXEMPLE_SMART }}
{{ EXEMPLE_MY_VAR }}
```


### Using Workflow Github contextual Information

Some of the [contextual information about workflow runs](https://docs.github.com/en/actions/writing-workflows/choosing-what-your-workflow-does/accessing-contextual-information-about-workflow-runs)
are available inside your jinja Template:

- github
- job
- runner
- strategy
- matrix

As part of an expression, you can access context information using one of two syntaxes.
Index syntax: `github['sha']`
Property dereference syntax: `github.sha`

```
{{ github.repository }}
{{ job.status }}
{{ runner.os }}
{{ strategy.job_index }}
{{ matrix.your_matrix_variable_name }}
```

Note: All strategy information key contains dashes that must me marked as underscore in jinja expression: `${{ strategy.job-index }}` becomes `{{ strategy.job_index }}`.


### Actions inputs


| Name | Description | Default |
| ---- | ----------- | ------- |
| `variables` | Variable to substitute in the jinja templates. Must be Key, value pairs in .env file format (key=value). | "" |
| `keep_template` | Put to `true` to keep original template file. | `false` |
| `data_file` | Source file contening inputs variable for the jinja template. | "" |
| `data_format` | Format of the `data_file`. Can be `env`, `ini`, `yaml`, `json` or `automatic` (for automatic detection). The automatic detction is based on the extension then on the content. | `automatic` |



## Code Quality

All unit test executed on each branch/PR are listed/described on
[testspace](https://fletort.testspace.com/projects/68162/spaces).

Coverage information and history is also avalailable on [coveralls](https://coveralls.io/github/fletort/jinja2-template-action).

## License

The scripts and documentation in this project are released under the
[MIT License](LICENSE)
