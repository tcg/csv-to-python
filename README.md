# CSV-to-Python (WIP)

A simple web-based utility that turns CSV/TSV data into something you can quickly paste into a Python shell and start working with. See: https://docs.python.org/3/library/functions.html#repr

## Description

This project exists to simplify the process of having some kind of textual data (usually CSV file exported from Excel or a database somewhere) and actually working with it in a structured way.

It's specifically for quick cases where it's not necessarily worth writing the boilerplate to read in a CSV, deal with potential Unicode issues; times when getting a Python list of the rows you can immediately paste into a running shell or one-off script would be most helpful.

## Getting Started

This is a minimal Django app that requires Python 3.5.x or higher. You can run it locally via the Django `runserver` command, or deploy it to your favorite Python host. It's currently ready-to-deploy to Heroku.

### Prerequisites

1. Python 3.5.x or higher.
2. pip
3. Basic knowledge of Python and/or Django.

### Installing

This project isn't currently hosted, but it's pretty easy to setup and get running.

For local hacking, clone the repo, then install the requirements via pip or pipenv:

`$ pip install -r requirements.txt` or `$ pipenv install`

That's it!

To run it locally, you can use the Django `runserver` command, like so:

```
$ ./manage.py runserver
```

If you used the default settings, you should be able to open your favorite web browser to `http://127.0.0.1:8000/` and see it working.

Now, grab some CSV data, paste it in the box labeled "CSV Data", and hit the button!

### Usage

You can select whether or not the first row of data contains headers. The output you get will be a little different if this option is selected. For the technical details of what/why, see the [Tablib quickstart](http://docs.python-tablib.org/en/latest/tutorial/#quickstart) docs page. Usually, it's the difference of a list-of-lists (or tuples) without headers, or a list of objects with the header string as the key, and the row/column content as values.

Currently, if the provided data is successfully processed, 3 output formats will be provided for your copy-paste pleasure.

Assuming the following data is provided:

```
cats,dogs,chickens
12,14,24
```

#### A Python "repr"
... or "printable representation of an object". This is usually something you can paste right back into a Python shell and start using.

Without headers:
```
[('cats', 'dogs', 'chickens'), ('12', '14', '24')]
```

With headers:
```
[('12', '14', '24')]
```

#### JSON
Data is turned into an object, and returned as JSON.

Without headers:
```
[["cats", "dogs", "chickens"], ["12", "14", "24"]]
```

With headers:
```
[{"cats": "12", "dogs": "14", "chickens": "24"}]
```

#### YAML
Just in case you're into this sort of thing.

Without headers:
```
- [cats, dogs, chickens]
- ['12', '14', '24']
```

With headers:
```
- {cats: '12', chickens: '24', dogs: '14'}
```

## Deployment

This project should be ready-to-deploy to system like Heroku, etc., and as of this writing will run just fine on one of their free plans.

Assuming you've already got the Heroku CLI tools installed, and you have already run `heroku login`...

1. Clone the repo
2. Run `heroku create`
3. Run `git push heroku master`
4. Profit!

## Built With

* [Django](https://www.djangoproject.com/) - Web framework
* [Pipenv](http://docs.pipenv.org/en/latest/) - Dependency management
* [Tablib](http://docs.python-tablib.org/en/latest/) - Used to read CSV/TSV data.

## Acknowledgments

* The biggest of thanks to [Kenneth Reitz](https://github.com/kennethreitz) for tools like [Tablib](https://github.com/kennethreitz/tablib), and freely sharing.
* All the times this week I needed to quickly mess with CSV data, but didn't want to fiddle with actually putting things on disk, and writing CSV reader/writer boilerplate code.

## Contributing

Oh, man! This thing is basically a toy project and not something I think is
amazing or worth a lot of time. But if you'd like, feel free to fork, create
issues, pull-requests, etc. It's pretty ugly, and barely useful, as-is. =)
