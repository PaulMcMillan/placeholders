# PyPi Placeholders

Sometimes you need to upload a placeholder package that does
nothing. This creates the minimally acceptable sdist that twine will
upload. Please edit the metadata before using, and consider trying it
out on the test pypi.

Use `make_package.py` like this:

```
$ python make_package.py nflx_jira
Creating new placeholder package:
nflx_jira-0.0.0a0.tar.gz
Upload to pypi? (y/n) y
Uploading distributions to https://upload.pypi.org/legacy/
Uploading nflx_jira-0.0.0a0.tar.gz
100%|██████████████████████████████████████████████████████████████████████████████| 3.08k/3.08k [00:01<00:00, 2.12kB/s]

View at:
https://pypi.org/project/nflx-jira/0.0.0a0/
```

You can also pass a version number as the second argument if you need something different than the default.