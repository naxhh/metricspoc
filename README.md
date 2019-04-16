# metricspoc

## Usage

```
$ metrics --help
$ metrics repos --tenant=motor
$ metrics line-report --tenant=motor --reporter=datadog/console
```

### Datadog reporter

The datadog reporter requires `DATADOG_API_KEY` and `DATADOG_APP_KEY` environmentals in order to report values to datadog

## Dev

```
# Without creating any venv!
$ pip install tox

# This will run codestyle and tests on its own venv
$ tox


# If you want to run the application in local
$ virtualenv -p python3 venv
$ source venv/bin/activate

$ pip install --editable .
$ metrics --help
```

## Project structure

### Analyzers

The analyzers are in charge of retrieving the data from different sources.
Here is where you would call the Github API or Datadog API to **retrieve** data.

The final data will be converted to a data object from **entities** and returned.

### Entities

Objects that represent data, they don't have any behaviour and are JSON serializable.


### Reporters

Reporters receive an entity, they convert that entity to the value they want to report.
For example:

The console reporter always dumps the json as it is.
The Datadog reporter sums the number of endpoints for the *endpoints* analyzer and only reports that.

### Scripts

Here is where all the commands of the cli are configured.
They act as the entry point of the reporters, `cli.py` is the main command and all the sub-commands are in a separate file.


## Tests

Pending to define
