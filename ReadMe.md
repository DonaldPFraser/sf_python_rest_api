This repository contains a proof-of-concept implementation of a python-based Salesforce REST api integration intended for use with Tecan FluentControl liquid handlers. All it does it count the number of retrieved records and writes that number to a query_output.csv . This is an example implementation and can be adapted for other use.

main.py is intended to be run as a python .exe (prepare it with (e.g. pyinstaller)) and accepts a single command line argument query in the form of (e.g. SELECT-Id-FROM-SObject). The - are stripped during execution and replaced with ' '. This was required for the integration with FluentControl. Unclear why the command line arguments could not be passed otherwise.

prepare a secrets folder (see main.py for the filepath), which contains a config.json containing the following:

{
    "username": "[username]",
    "password": "[password]",
    "security_token": "[securitytoken]",
    "domain": "[test]" (if a sandbox)
}