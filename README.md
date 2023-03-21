## Parallel experiment runner

The `run.sh` script creates a pool of processes (of size of POOL\_SIZE)  to execute in parallel.
Each process will run `script_to_run.py` with one configuration YAML file, placed at `configs` directory.

You can install dependencies using:

```
pip install -r requirements.txt
``` 

You must run:

```
./run.sh
```

You can edit this file to change the pool size and the location path to search.

The results will be at `output` directory. Check there!
