# Tallyhold

Offline data management, validation and profiling tool.

> **Status:** Early development. Not ready for use yet.

## What it does

Tallyhold moves large datasets out of Excel into a local SQLite database, so you can:

- Define your own tables and fields, not tied to a single template
- Count unique records
- Validate fields such as phone numbers and tax IDs
- Profile and report on your data
- Update records from periodic Excel/CSV exports
- Enrich a list of tax IDs with your existing data and export it back to Excel

Everything runs on your own computer. No server, no internet connection, no account.

## Running from source (Windows)

Requires Python 3.10 or newer.

```
python -m venv .venv
.venv\Scripts\python.exe -m pip install -r requirements.txt
```

Then double-click `Tallyhold.bat`.

## License

MIT. See [LICENSE](LICENSE).