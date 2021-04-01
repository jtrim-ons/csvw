# CSVW tools

So far this is just one simple program to create the outline of a
[CSVW](https://www.w3.org/TR/tabular-data-primer/) metadata file.

## Create metadata

To print a template for `filename.csv-metatdata.json`:

```python
python3 create_csvw_metadata.py filename.csv
```

For example, if `data.csv` is

```csv
"lsoa_name","lsoa_code","pop","pop_pct","age30_44","age30_44_pct","median_age"
"City of London 001A","E01000001",1465,100.0,379,25.9,45.0
"City of London 001B","E01000002",1436,100.0,393,27.4,45.0
```

then the tool prints the following JSON.

```json
{
  "@context": "http://www.w3.org/ns/csvw",
  "url": "countries.csv",
  "tableSchema": {
    "columns": [
      {
        "titles": "lsoa_name",
        "dc:description": "TODO"
      },
      {
        "titles": "lsoa_code",
        "dc:description": "TODO"
      },
      {
        "titles": "pop",
        "dc:description": "TODO"
      },
      {
        "titles": "pop_pct",
        "dc:description": "TODO"
      },
      {
        "titles": "age30_44",
        "dc:description": "TODO"
      },
      {
        "titles": "age30_44_pct",
        "dc:description": "TODO"
      },
      {
        "titles": "median_age",
        "dc:description": "TODO"
      }
    ]
  }
}
```
