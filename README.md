# python-web-flask-mvc-sqlserver-ssl-pop

## Description
Creates a datatable of `pop` for a flask project.

If path is not found, will default to 404 error.

Sql server uses self-signed ssl.

## Tech stack
- python
  - flask
  - sqlalchemy
- bootstrap
- jquery
- dataTable
- mssql

## Docker stack
- alpine:edge
- python:latest
- mcr.microsoft.com/mssql/server:2017-CU17-ubuntu

## To run
`sudo ./install.sh -u`
- [web app](http://localhost)

## To stop (optional)
`sudo ./install.sh -d`

## For help
`sudo ./install.sh -h`

## Credit
- https://stackabuse.com/using-sqlalchemy-with-flask-and-postgresql/
- https://stackoverflow.com/questions/27766794/switching-from-sqlite-to-mysql-with-flask-sqlalchemy
