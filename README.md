# Echo Stress Test

This module simulates real-world load for IdeaMelt's Notifier app.

## Instructions

To run this test, simply run the following command in shell

```python
python search_test.py
```

## Dependencies

```
grequests
libevent
```

## Configuration

To change the scope of the test, change the following parameters in the `settings.py` file

```python
SEARCH_TOTAL_TIME = 20 # seconds
SEARCH_INTERVAL_TIME = 5 # seconds
USERS_TO_TEST = 5 # you can stress test a random sample users (must be less than 1000)
```

## More

Errors are printed out to the console and stored in the log folder

Full JSON data output of the test results are stored in the data folder