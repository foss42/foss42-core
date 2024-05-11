# Contributing Guide

Contributors can add new useful functions to the foss42 core library or new data (check `foss42/data/`) by following the below steps:

**Step 1**: Raise a **new issue** stating that you want to add new function/data. We will assign the issue to you and label it.  
**Step 2**: Star and fork THIS repository.  
**Step 3**: Now in your fork, make the required changes.  
**Step 4**: Raise a PR with your changes.  
**Step 5**: Wait for review and PR merge.  

## Setting up Dev env

- Install the latest version of Python.  
- Clone the repo to your local sytem using `git clone https://github.com/foss42/foss42-core.git`
- Use terminal to navigate inside the folder (`cd foss42-core`).  
- Execute `pip3 install -e .` to install the library locally.  
- Now you can import and use the library in the local enviroment.

```python
>>> import foss42.text.humanize as hz
>>> hz.humanize_bytes(1126,
                      2,
                      prefix = True,
                      trailing_zeros = True)
>>> '1.10 kilobytes'
```

## Testing

Install `pytest` via the following command

```
$ pip3 install pytest
```

Now inside the folder, run the tests using the command:

```
$ pytest
```
