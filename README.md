# Nexus Maven Migration

This project is a simple tool written in Python to upload Maven local repository to Sonatype Nexus Repository Manage through the [Nexus API](https://help.sonatype.com/repomanager3/rest-and-integration-api).
The script will find dependencies in local repository with a deep search and will upload do Nexus server.

This tool can be useful to migrate different Repository Managers.

# Getting start

You need Python 3 with requests module installed. To install the module use this pip command:

```console
    pip install requests
```

Then, run de main.py Python script:

```console
    python main.py
```
