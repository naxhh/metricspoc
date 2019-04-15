# metricspoc

## Usage

```
$ metrics repos --tenant=motor
$ metrics line-report --tenant=motor --reporter=datadog/console
```

## Dev

```
$ virtualenv -p python3 venv
$ source venv/bin/activate

$ pip install --editable .

$ metrics --help
```

## Project structure

### Analyzers

The analyzers are in charge of retrieving the data from different sources.
Here is where you would call the Github API or Datadog API to **retrieve** data.

The final data will be converted to a data object.

### Reporters

Reportes receive a data object and persist that data into a backend.
For development a console reporter will just display the information into the console
To gather metrics a Datadog reporter is also usefull.

Other examples could be kafka reporter or an SQL reporter

### Scripts

Here is where all the commands of the cli are configured.
They act as the entry point of the reporters, `cli.py` is the main command and all the sub-commands are in a separate file.
