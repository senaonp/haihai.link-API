# raw data file generator

## generates JSON files with public information from a given list of usernames

<img src="./img/preview.JPG" width="100%" height="auto">

------------------

How to use: 
- set any configurable variables (listed in the "configs" section):
- run `script.py`
- the JSON files should be generated in the set output directory

A video demonstration is also available on: https://fbacarisas.xyz/video/#haihai_link_API_raw_data_file_generator

------------------

How JSON data is structured:

```
{
    "name": _____,
    "description": _____,
    "status": _____,
    "collections": [
        {
            "name": _____,
            "description": _____,
            "urls": [
                {
                    "url": _____,
                    "urlName": _____,
                    "urlDescription": _____
                },
                ...
            ]
        },
        ...
    ]
}
```

------------------

Available configurable variables:
- outputDir - the directory to write the output files (default: './output')
- users - a list of usernames (default: ['senaonp', 'senaonpNian'])