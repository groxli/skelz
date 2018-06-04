# -*- coding: utf-8 -*-

function_stub = """def function_stub(arg1, arg2):
    \"""
    Human-readable function title/name.

    Additional description of the function's purpose and usage..

    Parameters
    ----------
    arg1 : int
        Description of arg1
    arg2 : str
        Description of arg2

    Returns
    -------
    int
        Description of return value

    \"""
    return_val = True
    return return_val

"""

main_stub = """def main():
    function_stub(1,2)

if __name__ == "__main__":
    main()

"""

config_import = """import configparser # For loading in job settings.
"""

config_body = """# Configuration Loader:
config = configparser.ConfigParser()
config.read('app.config')
db_name = config['DEFAULT']['db_name']
db_user = config['DEFAULT']['db_user']
db_pass = config['DEFAULT']['db_pass']
load_path = config['DEFAULT']['load_path']

"""

config_file_text = """[DEFAULT]
db_name: your_db_name
db_user: your_db_user
db_pass: your_db_password
load_path: /var/some_path/
"""

file_body = """# File Loader:
with open('some_file.txt') as f:
    for line in f:
        print(line)

"""

pd_import = """import pandas as pd # For output file.
import time # For date/time in output filename.
"""

pd_body = """# Pandas DataFrame and File Writer:
output_filename = "output/name_%s.xlsx" % time.strftime("%Y-%m-%d-%H%M%S")
writer = pd.ExcelWriter(output_filename) # File handle for writing multiple worksheets.

df = pd.DataFrame() # Placeholder DataFrame.

df.to_excel(writer, sheet_name="your_data_title", index=False)
df.to_excel(writer, sheet_name="your_data_title2", index=False)

writer.save()

"""

mpl_import = """import matplotlib.pyplot as plt
"""

mpl_body = """#Matplotlib Scatter Plot:
plt.scatter(x_array, y_array, alpha=1.0, color='k')
plt.xlabel("x Values")
plt.ylabel("y values")

#Matplotlib Histogram:
plt.hist(x_values, bins=20)
plt.xlabel("x value distribution")

"""

mysql_import = """import MySQLdb
"""

mysql_body = """conn = MySQLdb.connect(host="localhost", port=3306, user="username", passwd="pw", db="db_name")

cursor = conn.cursor()

cursor.execute("SELECT col_1, col_2 
FROM table_name 
WHERE col_3=%s 
AND col_4 > %s 
LIMIT 10", 
(parm_1, parm_2))

try:
    for row in iter_row(cursor, 10):
        print(row)
except Error as e:
    print(e)
 
finally:
    cursor.close()

# Close the connection before exiting the application:
conn.close()
    
"""

mongo_import = """from pymongo import MongoClient # For storing data.
"""

mongo_body = """# MongoDB connection and query:
def mongo_connect():
    # Connection to Mongo DB
    try:
        client = MongoClient('localhost', 27017)
        db = client['db_name'] # Select the database.
        collection = db['collection_name']
    except Exception as e:
       print("Could not connect to MongoDB: %s" % e)
    return collection

mdb = mongo_connect()

try:
    mdb.insert_one(
    {
              'field_1': field_1_value,
              'field_2': field_2_value
            })
except Exception as e:
    print("Exception caught:\n", str(e))

# Query MongoDB
r = mdb.find({'field_1': field_1_value, 'field_2':{'$lt': 99.9}})

"""

readme_text = """
# Project Title

One Paragraph of project description goes here

## Getting Started

These instructions will get you a copy of the project up and running on your local machine for development and testing purposes. See deployment for notes on how to deploy the project on a live system.

### Prerequisites

What things you need to install the software and how to install them

```
Give examples
```

### Installing

A step by step series of examples that tell you how to get a development env running

Say what the step will be

```
Give the example
```

And repeat

```
until finished
```

End with an example of getting some data out of the system or using it for a little demo

## Running the tests

Explain how to run the automated tests for this system

### Break down into end to end tests

Explain what these tests test and why

```
Give an example
```

### And coding style tests

Explain what these tests test and why

```
Give an example
```

## Deployment

Add additional notes about how to deploy this on a live system

## Built With

* [Dropwizard](http://www.dropwizard.io/1.0.2/docs/) - The web framework used
* [Maven](https://maven.apache.org/) - Dependency Management
* [ROME](https://rometools.github.io/rome/) - Used to generate RSS Feeds

## Contributing

Please read [CONTRIBUTING.md](https://gist.github.com/PurpleBooth/b24679402957c63ec426) for details on our code of conduct, and the process for submitting pull requests to us.

## Versioning

We use [SemVer](http://semver.org/) for versioning. For the versions available, see the [tags on this repository](https://github.com/your/project/tags). 

## Authors

* **Billie Thompson** - *Initial work* - [PurpleBooth](https://github.com/PurpleBooth)

See also the list of [contributors](https://github.com/your/project/contributors) who participated in this project.

## License

This project is licensed under the MIT License - see the [LICENSE.md](LICENSE.md) file for details

## Acknowledgments

* Hat tip to anyone whose code was used
* Inspiration
* etc
"""