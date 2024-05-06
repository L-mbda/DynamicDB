# 🧨 DynamicDB - A Simple Toy Database System

This is a simple toy database system that I made within 3 class periods at school within a modified CSV format, with it being written in Python aswell.

## Table of Contents

- [Installation](#installation)
- [Usage](#usage)
- [License](#license)

## Installation

Just install Python, and you are good to go!

## Usage

Example code can be located at the example.py file.

There are 3 functions within the database system.

### Creating a Database
```py
CreateDB(FILE_NAME, schema)
```
This function requires a FILE_NAME for what you want the database to be called and also the relevant location, as well as a schema.

The example schema can be seen below:

```
data
fields username, password,balance fields
joe,pass!,2000
zen,yingyang1!,30
end_data
```

Just input that into the CreateDB function, and you will be good.

### Reading from a Database
```py
ReadDB(FILE_NAME)
```

The function allows you to read, with the headers and all the body information from the file.
You will get a return with a list in [header_fields, r_data], version

with version being the version of the database

### Writing to a Database with body
```py
WriteDB(FILE_NAME, data)
```

This function allows you to write to the database with the data that you want to input.

The data should be in the format of:

```
username,password,field
```

with the field being the field that you want to input.

## License

The license for this project is under the Mozilla Public License Version 2.0.

The license can be located ![here](https://github.com/de-y/DynamicDB/blob/main/LICENSE)
