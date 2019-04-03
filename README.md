# metrics-poc

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

$ metrics ...
```
