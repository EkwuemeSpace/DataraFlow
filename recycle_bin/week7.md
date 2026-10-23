# Cleaning, Visualising, and Combining Data with pandas and SQL

> **Level:** Beginner (you should know basic Python, basic pandas, and basic SQL) | **Code language:** Python | **Estimated study time:** 5 to 7 hours

## Table of Contents

- [Phase 1: Reading Data from a Database](#phase-1-reading-data-from-a-database)
  - [Lesson 1.1: What a database is and how you connect](#lesson-11-what-a-database-is-and-how-you-connect)
  - [Lesson 1.2: Reading a table into a DataFrame](#lesson-12-reading-a-table-into-a-dataframe)
  - [Lesson 1.3: Looking at what you received](#lesson-13-looking-at-what-you-received)
- [Phase 2: Cleaning Messy Data](#phase-2-cleaning-messy-data)
  - [Lesson 2.1: Fixing column names](#lesson-21-fixing-column-names)
  - [Lesson 2.2: Removing extra characters from values](#lesson-22-removing-extra-characters-from-values)
  - [Lesson 2.3: Handling missing values](#lesson-23-handling-missing-values)
  - [Lesson 2.4: Changing data types](#lesson-24-changing-data-types)
- [Phase 3: Visualising Data](#phase-3-visualising-data)
  - [Lesson 3.1: Your first plot](#lesson-31-your-first-plot)
  - [Lesson 3.2: Making the chart bigger and clearer](#lesson-32-making-the-chart-bigger-and-clearer)
  - [Lesson 3.3: Plotting more than one line](#lesson-33-plotting-more-than-one-line)
  - [Lesson 3.4: Using dates as the index](#lesson-34-using-dates-as-the-index)
  - [Lesson 3.5: Slicing by date range](#lesson-35-slicing-by-date-range)
- [Phase 4: Combining Data with merge](#phase-4-combining-data-with-merge)
  - [Lesson 4.1: Building a small table by hand](#lesson-41-building-a-small-table-by-hand)
  - [Lesson 4.2: The four join types](#lesson-42-the-four-join-types)
  - [Lesson 4.3: Using constants for column names](#lesson-43-using-constants-for-column-names)
- [Phase 5: A Full Analysis - GDP and Life Expectancy](#phase-5-a-full-analysis---gdp-and-life-expectancy)
  - [Lesson 5.1: Loading and cleaning the World Bank data](#lesson-51-loading-and-cleaning-the-world-bank-data)
  - [Lesson 5.2: Transforming values](#lesson-52-transforming-values)
  - [Lesson 5.3: Merging and correlating](#lesson-53-merging-and-correlating)
  - [Lesson 5.4: Visualising the relationship](#lesson-54-visualising-the-relationship)
  - [Lesson 5.5: Reading the result](#lesson-55-reading-the-result)
- [Phase 6: Doing It in SQL](#phase-6-doing-it-in-sql)
  - [Lesson 6.1: Cleaning a messy column in SQL](#lesson-61-cleaning-a-messy-column-in-sql)
  - [Lesson 6.2: Working with dates in SQL](#lesson-62-working-with-dates-in-sql)
  - [Lesson 6.3: Joining tables in SQL](#lesson-63-joining-tables-in-sql)
  - [Lesson 6.4: Counting what a join loses](#lesson-64-counting-what-a-join-loses)
  - [Lesson 6.5: Window functions for rolling totals](#lesson-65-window-functions-for-rolling-totals)
- [Glossary](#glossary)
- [Answer Key](#answer-key)

## How to Use This Note

- Read each lesson in order. Do not skip ahead.
- Before you run a code cell, guess what the output will be.
- Run every code cell yourself. The cells use small sample data that is created inside the note, so they run without a real database.
- Do the Practice Task at the end of each Phase. It uses only skills taught up to that point.
- If something is unclear, reread the Key Terms table and the analogy first.

---

## Phase 1: Reading Data from a Database

**Phase goal:** Connect to a database and bring a table into pandas as a DataFrame.

**You need before this phase:** Nothing. This is the starting point.

#### Setup Cell

```python
# pandas is the main library for working with tables in Python.
import pandas as pd

# This function pretends to be a database connection.
# In the real cohort environment, a function called run_query
# connects to a real database. Here it returns small sample tables
# so every code cell runs without external dependencies.
def run_query(sql):
    # A small sample of raw London weather data.
    # Notice the leading space in one column name and the
    # '<br />' at the end of the last column name. Those are
    # the messy parts we will clean in Phase 2.
    data = {
        'GMT': ['2014-1-1', '2014-1-2', '2014-1-3', '2014-1-4', '2014-1-5'],
        'Max TemperatureC': [8, 9, 7, 10, 11],
        ' Mean TemperatureC': [6, 7, 5, 8, 9],
        'Min TemperatureC': [4, 5, 3, 6, 7],
        'Max Wind SpeedKm/h': [20, 25, 30, 15, 18],
        'Precipitationmm': [0.0, 2.5, 0.0, 1.0, 0.0],
        'Events': [None, 'Rain', None, 'Rain', None],
        'WindDirDegrees<br />': ['186<br />', '270<br />', '90<br />', '355<br />', '10<br />']
    }
    return pd.DataFrame(data)
```

### Lesson 1.1: What a database is and how you connect

#### What You Will Learn
- What a database, a schema, and a table are.
- How to run a SQL query from Python.
- Why the cohort uses a read-only account.

#### Key Terms
| Term | Simple meaning |
|---|---|
| **Database** | A place where many tables of data are stored and managed. |
| **Schema** | A folder inside a database that groups related tables. |
| **Table** | One grid of rows and columns stored in a database. |
| **SQL** | The language used to ask a database for data. |
| **Query** | One request written in SQL. |
| **DataFrame** | A pandas table with rows and columns. |

#### The Idea in Plain Words

Think of a library. The building is the database. The shelves are schemas. Each shelf holds several books, and each book is a table. To borrow a book, you fill in a request slip. The slip is your query.

A **database** stores many tables. A **schema** groups related tables. A **table** is a grid of rows and columns. You ask for data by writing a **query** in **SQL** (Structured Query Language).

In the cohort, one function does the work: `run_query`. You give it a SQL string. It returns a pandas DataFrame. That is the bridge between the database and your notebook.

The account is read-only. That means you can read data but you cannot change it. This is safe. You cannot damage the shared data by accident.

#### See It in Code

Before you run this, guess the output.

```python
# run_query takes a SQL string and returns a pandas DataFrame.
london = run_query("SELECT * FROM week07.london_2014")

# Show the type of what we got back.
print(type(london))
```

**Expected output:**
```text
<class 'pandas.core.frame.DataFrame'>
```

**What happened:** `run_query` sent the SQL to the pretend database and returned a DataFrame.

#### Common Mistakes

```text
KeyError: ' Mean Humidity'
```

You tried to select a column with the wrong name. The real column may have a leading space. Fix: print `london.columns` first.

```text
PermissionError: 'INSERT' is not allowed
```

You tried to write to the database. The account is read-only. Fix: only use `SELECT` queries.

#### Quick Check
1. What does a schema group together?
2. Which function turns a SQL query into a DataFrame in this note?
3. What would happen if you ran `run_query("DELETE FROM week07.london_2014")`?

#### Lesson Recap
- A database holds schemas. A schema holds tables.
- `run_query` is the bridge from SQL to pandas.
- The cohort account is read-only.

---

### Lesson 1.2: Reading a table into a DataFrame

#### What You Will Learn
- How to write a basic `SELECT` query.
- How to load a whole table.
- How to load selected columns.

#### Key Terms
| Term | Simple meaning |
|---|---|
| **SELECT** | The SQL keyword that asks for columns. |
| **FROM** | The SQL keyword that names the table. |
| **SELECT \*** | Ask for every column. |

#### The Idea in Plain Words

When you walk into a shop and say "give me one of everything", the shopkeeper brings the whole shelf. `SELECT *` means "give me every column". `SELECT name, price` means "give me only these two columns".

#### See It in Code

Before you run this, guess the output.

```python
# SELECT * means "every column".
london = run_query("SELECT * FROM week07.london_2014")
print(london.shape)
```

**Expected output:**
```text
(5, 8)
```

**What happened:** The DataFrame has 5 rows and 8 columns.

#### Common Mistakes

```text
ProgrammingError: Invalid object name 'london_2014'
```

You forgot the schema. Fix: write `week07.london_2014`.

#### Quick Check
1. What does `SELECT *` mean?
2. How many rows and columns did the sample table have?
3. Why must you write the schema name before the table name?

#### Lesson Recap
- `SELECT *` returns every column.
- The schema name comes before the table name.
- `.shape` shows rows and columns.

---

### Lesson 1.3: Looking at what you received

#### What You Will Learn
- How to peek at the first rows with `head()`.
- How to list column names with `.columns`.
- How to see data types with `.dtypes`.

#### Key Terms
| Term | Simple meaning |
|---|---|
| **head()** | Shows the first few rows. |
| **columns** | The list of column names. |
| **dtypes** | The data type of each column. |

#### The Idea in Plain Words

When a parcel arrives, you open it and look inside before you use anything. `head()` opens the parcel. `.columns` lists the labels. `.dtypes` tells you what kind of value each column holds.

#### See It in Code

Before you run this, guess the output.

```python
london = run_query("SELECT * FROM week07.london_2014")
print(london.head(2))
print(london.columns.tolist())
print(london.dtypes)
```

**Expected output:**
```text
        GMT  Max TemperatureC   Mean TemperatureC  ... WindDirDegrees<br />
0  2014-1-1                 8                  6  ...           186<br />
1  2014-1-2                 9                  7  ...           270<br />

['GMT', 'Max TemperatureC', ' Mean TemperatureC', 'Min TemperatureC', 'Max Wind SpeedKm/h', 'Precipitationmm', 'Events', 'WindDirDegrees<br />']
GMT                      object
Max TemperatureC          int64
 Mean TemperatureC        int64
...
WindDirDegrees<br />     object
dtype: object
```

**What happened:** You can see the leading space in `' Mean TemperatureC'` and the `<br />` in the last column name. You can also see that `GMT` is `object` (text), not a date.

#### Common Mistakes

```text
AttributeError: 'DataFrame' object has no attribute 'head'
```

You wrote `head` without brackets. Fix: use `london.head()`.

#### Quick Check
1. Which column name has a leading space?
2. Which column has `<br />` in its name?
3. Which two columns are of type `object` when they should be numbers or dates?

#### Lesson Recap
- `head()` shows the first rows.
- `.columns` lists column names, including hidden spaces.
- `.dtypes` shows what type each column holds.

### Phase 1 Summary
- You can connect to a database through `run_query`.
- You can load a whole table or selected columns.
- You can inspect rows, columns, and data types.
- You know the account is read-only.

### Phase 1 Practice Task: Load and describe a table

**Difficulty:** Easy | **Time:** 10 minutes

**Skills used:**
- From this phase: `run_query` (Lesson 1.1), `SELECT *` (Lesson 1.2), `head()` and `.dtypes` (Lesson 1.3)
- From earlier phases: None. This is your first task.

**The task:** The pretend database has a table called `week07.london_2014`. Load it into a DataFrame called `weather`. Print the shape, the list of column names, and the first three rows. The table has 5 rows and 8 columns. The columns are: `GMT`, `Max TemperatureC`, ` Mean TemperatureC`, `Min TemperatureC`, `Max Wind SpeedKm/h`, `Precipitationmm`, `Events`, `WindDirDegrees<br />`.

**Expected output:**
```text
(5, 8)
['GMT', 'Max TemperatureC', ' Mean TemperatureC', 'Min TemperatureC', 'Max Wind SpeedKm/h', 'Precipitationmm', 'Events', 'WindDirDegrees<br />']
        GMT  Max TemperatureC   Mean TemperatureC  Min TemperatureC  Max Wind SpeedKm/h  Precipitationmm Events WindDirDegrees<br />
0  2014-1-1                 8                  6                 4                  20              0.0   None           186<br />
1  2014-1-2                 9                  7                 5                  25              2.5   Rain           270<br />
2  2014-1-3                 7                  5                 3                  30              0.0   None            90<br />
```

---

## Phase 2: Cleaning Messy Data

**Phase goal:** Turn a messy table into a clean table that is ready for analysis.

**You need before this phase:** Phase 1.

#### Setup Cell

```python
import pandas as pd

# A fresh copy of the raw data. We call this every lesson so
# each lesson starts from the same messy state.
def load_london_raw():
    data = {
        'GMT': ['2014-1-1', '2014-1-2', '2014-1-3', '2014-1-4', '2014-1-5'],
        'Max TemperatureC': [8, 9, 7, 10, 11],
        ' Mean TemperatureC': [6, 7, 5, 8, 9],
        'Min TemperatureC': [4, 5, 3, 6, 7],
        'Max Wind SpeedKm/h': [20, 25, 30, 15, 18],
        'Precipitationmm': [0.0, 2.5, 0.0, 1.0, 0.0],
        'Events': [None, 'Rain', None, 'Rain', None],
        'WindDirDegrees<br />': ['186<br />', '270<br />', '90<br />', '355<br />', '10<br />']
    }
    return pd.DataFrame(data)
```

### Lesson 2.1: Fixing column names

#### What You Will Learn
- Why column names sometimes have hidden spaces.
- How to strip spaces from all column names.
- How to rename a column with `rename()`.

#### Key Terms
| Term | Simple meaning |
|---|---|
| **Column name** | The label at the top of a column. |
| **strip()** | Removes spaces from the start and end of text. |
| **rename()** | Changes one or more column names. |

#### The Idea in Plain Words

Imagine you write labels on jars in a kitchen. One label says " sugar" with a space in front. When someone asks for "sugar", they cannot find it, because the label reads " sugar". The space is invisible but it breaks the search.

A CSV file can have a space after each comma. When pandas reads the file, the space becomes part of the next column name. The same problem appears when the data comes from a database that kept the original export. The fix is to strip the spaces.

#### See It in Code

Before you run this, guess the output.

```python
london = load_london_raw()

# Show the column names exactly as they are.
print("Before:", london.columns.tolist())

# strip() removes spaces at the start and end of each name.
london.columns = london.columns.str.strip()
print("After: ", london.columns.tolist())
```

**Expected output:**
```text
Before: ['GMT', 'Max TemperatureC', ' Mean TemperatureC', 'Min TemperatureC', 'Max Wind SpeedKm/h', 'Precipitationmm', 'Events', 'WindDirDegrees<br />']
After:  ['GMT', 'Max TemperatureC', 'Mean TemperatureC', 'Min TemperatureC', 'Max Wind SpeedKm/h', 'Precipitationmm', 'Events', 'WindDirDegrees<br />']
```

**What happened:** The leading space in `' Mean TemperatureC'` was removed. The `<br />` part is still there because `strip()` only removes spaces.

#### Common Mistakes

```text
KeyError: 'Mean TemperatureC'
```

You used the clean name but the column still has a space. Fix: strip the columns first.

#### Quick Check
1. Why does the space appear in the column name?
2. Does `strip()` remove `<br />`?
3. What does `london.columns = london.columns.str.strip()` change?

#### Lesson Recap
- Spaces after commas become part of column names.
- `.str.strip()` removes them.
- Always inspect `.columns` after loading.

---

### Lesson 2.2: Removing extra characters from values

#### What You Will Learn
- Why values can carry `<br />`.
- How to rename a column with `rename()`.
- How to remove text from the end of each value with `str.rstrip()`.

#### Key Terms
| Term | Simple meaning |
|---|---|
| **HTML line break** | A tag (`<br />`) that starts a new line in a web page. |
| **rstrip()** | Removes characters from the right end of text. |
| **rename()** | Changes a column name. |

#### The Idea in Plain Words

When you copy text from a web page, the copy can bring hidden line breaks with it. The export from the weather site added `<br />` to the end of every line. pandas read that tag as part of the column name and as part of each value.

The fix has two steps. First, rename the column so it no longer contains `<br />`. Second, strip `<br />` from every value.

#### See It in Code

Before you run this, guess the output.

```python
london = load_london_raw()
london.columns = london.columns.str.strip()

# Step 1: rename the column so it no longer contains <br />.
london = london.rename(columns={'WindDirDegrees<br />': 'WindDirDegrees'})

# Step 2: remove <br /> from the end of every value.
london['WindDirDegrees'] = london['WindDirDegrees'].str.rstrip('<br />')

print(london['WindDirDegrees'].tolist())
```

**Expected output:**
```text
['186', '270', '90', '355', '10']
```

**What happened:** Each value lost its trailing `<br />`. The values are still text. We will change them to integers in Lesson 2.4.

#### Common Mistakes

```text
AttributeError: Can only use .str accessor with string values
```

You tried `.str.rstrip()` on a column that pandas already turned into numbers. Fix: check `.dtypes` first.

#### Quick Check
1. Which method removes text from the right end of a string?
2. Why do we rename the column before stripping the values?
3. Are the values integers after this step?

#### Lesson Recap
- `rename()` changes column names.
- `str.rstrip()` removes characters from the right.
- The values are still text after cleaning.

---

### Lesson 2.3: Handling missing values

#### What You Will Learn
- How to find missing values with `isnull()`.
- How to replace them with `fillna()`.
- How to drop rows that contain them with `dropna()`.

#### Key Terms
| Term | Simple meaning |
|---|---|
| **NaN** | "Not a Number". pandas marks missing values with it. |
| **isnull()** | Returns True where a value is missing. |
| **fillna()** | Replaces missing values with a value you choose. |
| **dropna()** | Removes rows that have any missing value. |

#### The Idea in Plain Words

Imagine a class register where some days are blank because the teacher forgot to mark them. A blank is not the same as "absent". It is unknown. pandas calls a blank **NaN**.

You have three choices. You can leave the blank, replace it with a fixed value, or remove the row. The choice depends on what the column means. For the `Events` column, a blank means "no event". So the right replacement is the empty string.

#### See It in Code

Before you run this, guess the output.

```python
london = load_london_raw()

# Count missing values in the Events column.
print("Missing before:", london['Events'].isnull().sum())

# Replace each missing event with an empty string.
london['Events'] = london['Events'].fillna('')
print("Missing after: ", london['Events'].isnull().sum())

# dropna() returns a new table with no missing values at all.
print("Rows before dropna:", len(london))
print("Rows after dropna: ", len(london.dropna()))
```

**Expected output:**
```text
Missing before: 3
Missing after:  0
Rows before dropna: 5
Rows after dropna:  2
```

**What happened:** Three rows had no event. Replacing them with an empty string removed the missing values in that column. After `dropna()`, only 2 rows remain, because other columns also had missing values.

#### Common Mistakes

```text
ValueError: Cannot convert non-finite values (NA or inf) to integer
```

You tried to do maths on a column that still has NaN. Fix: use `fillna()` or `dropna()` first.

#### Quick Check
1. What does NaN stand for?
2. What is the difference between `fillna()` and `dropna()`?
3. Why is the empty string a good replacement for a missing event?

#### Lesson Recap
- `isnull()` finds missing values.
- `fillna()` replaces them.
- `dropna()` removes rows that still contain them.

---

### Lesson 2.4: Changing data types

#### What You Will Learn
- How to check types with `.dtypes`.
- How to turn text into integers with `.astype()`.
- How to turn text dates into real dates with `pd.to_datetime()`.

#### Key Terms
| Term | Simple meaning |
|---|---|
| **Data type** | The kind of value a column holds (number, text, date). |
| **astype()** | Changes a column to a new type. |
| **datetime64** | The pandas type for real dates. |
| **to_datetime()** | Converts text to `datetime64`. |

#### The Idea in Plain Words

A price written on paper is not a number you can add. First you must type it into a calculator. The same is true for a column. Text that looks like a number is still text until you convert it.

`GMT` holds text like `'2014-1-1'`. We want a real date so we can compare dates. `WindDirDegrees` holds text like `'186'`. We want an integer so we can compare degrees.

#### See It in Code

Before you run this, guess the output.

```python
london = load_london_raw()
london.columns = london.columns.str.strip()
london = london.rename(columns={'WindDirDegrees<br />': 'WindDirDegrees'})
london['WindDirDegrees'] = london['WindDirDegrees'].str.rstrip('<br />')

# Turn text into integers.
london['WindDirDegrees'] = london['WindDirDegrees'].astype('int64')

# Turn text into real dates.
london['GMT'] = pd.to_datetime(london['GMT'])

print(london.dtypes)
```

**Expected output:**
```text
GMT                  datetime64[ns]
Max TemperatureC              int64
Mean TemperatureC             int64
Min TemperatureC              int64
Max Wind SpeedKm/h            int64
Precipitationmm             float64
Events                       object
WindDirDegrees                int64
dtype: object
```

**What happened:** `WindDirDegrees` is now `int64`. `GMT` is now `datetime64[ns]`. You can now compare dates and degrees.

#### Common Mistakes

```text
ValueError: invalid literal for int() with base 10: '186<br />'
```

You called `astype('int64')` before stripping `<br />`. Fix: strip first, then convert.

#### Quick Check
1. Which method changes a column's data type?
2. Which function converts text to a real date?
3. Why must you strip `<br />` before calling `astype('int64')`?

#### Lesson Recap
- `.dtypes` shows each column's type.
- `.astype('int64')` converts text to whole numbers.
- `pd.to_datetime()` converts text to real dates.

### Phase 2 Summary
- You can strip spaces from column names.
- You can remove `<br />` from values.
- You can handle missing values with `fillna()` and `dropna()`.
- You can convert text to integers and dates.

### Phase 2 Practice Task: Clean a weather table

**Difficulty:** Easy-Medium | **Time:** 20 minutes

**Skills used:**
- From this phase: stripping column names (Lesson 2.1), removing `<br />` (Lesson 2.2), `fillna()` (Lesson 2.3), `astype()` and `to_datetime()` (Lesson 2.4)
- From earlier phases: `run_query` and `SELECT *` (Phase 1, Lessons 1.1 and 1.2)

**The task:** The table below is the raw weather table. Clean it in four steps. (1) Strip spaces from the column names. (2) Rename `'WindDirDegrees<br />'` to `'WindDirDegrees'` and strip `<br />` from its values. (3) Replace missing `Events` with the empty string. (4) Convert `GMT` to a real date and `WindDirDegrees` to an integer. Print the final `.dtypes`.

The data:
- `GMT`: `['2014-1-1', '2014-1-2', '2014-1-3']`
- `Max TemperatureC`: `[8, 9, 7]`
- `' Mean TemperatureC'`: `[6, 7, 5]`
- `'WindDirDegrees<br />'`: `['186<br />', '270<br />', '90<br />']`
- `Events`: `[None, 'Rain', None]`

**Expected output:**
```text
GMT                  datetime64[ns]
Max TemperatureC              int64
Mean TemperatureC             int64
WindDirDegrees                int64
Events                       object
dtype: object
```

---

## Phase 3: Visualising Data

**Phase goal:** Turn a table into a line chart that tells a story.

**You need before this phase:** Phase 2.

#### Setup Cell

```python
import pandas as pd
import matplotlib
# This line tells Jupyter to show plots inside the notebook.
%matplotlib inline

def load_london():
    data = {
        'GMT': pd.to_datetime(['2014-1-1', '2014-1-2', '2014-1-3', '2014-1-4', '2014-1-5']),
        'Max TemperatureC': [8, 9, 7, 10, 11],
        'Mean TemperatureC': [6, 7, 5, 8, 9],
        'Min TemperatureC': [4, 5, 3, 6, 7],
        'Max Wind SpeedKm/h': [20, 25, 30, 15, 18],
        'Mean Humidity': [80, 85, 78, 82, 75]
    }
    return pd.DataFrame(data).set_index('GMT')
```

### Lesson 3.1: Your first plot

#### What You Will Learn
- What `%matplotlib inline` does.
- How to plot one column with `.plot()`.
- How to add grid lines with `grid=True`.

#### Key Terms
| Term | Simple meaning |
|---|---|
| **Plot** | A drawing of data, such as a line chart. |
| **matplotlib** | The Python library that draws plots. |
| **grid** | Light lines behind the plot that help you read values. |

#### The Idea in Plain Words

A long table of numbers is hard to read. A picture is faster. A **plot** turns a column into a line. The x-axis shows the row order (usually time). The y-axis shows the value.

`%matplotlib inline` is a magic command. It tells Jupyter to draw the plot inside the notebook, not in a separate window.

#### Tool Card: matplotlib
- **What it is:** The main plotting library for Python.
- **What it does:** Draws line charts, bar charts, scatter plots, and more.
- **Why we use it here:** pandas uses matplotlib behind the scenes when you call `.plot()`.
- **Install:** `!pip install matplotlib`
- **Import:** `import matplotlib`
- **Other options:** seaborn (prettier defaults), plotly (interactive charts).

#### See It in Code

Before you run this, guess the shape of the line.

```python
london = load_london()

# Plot one column as a line. grid=True adds light grid lines.
london['Max Wind SpeedKm/h'].plot(grid=True)
```

**Expected output:** A line chart with five points. The highest point is 30 km/h on the third day.

**What happened:** pandas used the index (the dates) for the x-axis and the column values for the y-axis.

#### Common Mistakes

```text
UserWarning: Matplotlib is currently using agg, which is a non-GUI backend
```

You are running outside Jupyter. Fix: use Jupyter, or call `plt.show()` after the plot.

#### Quick Check
1. What does `%matplotlib inline` do?
2. Which column becomes the x-axis by default?
3. What does `grid=True` add?

#### Lesson Recap
- `.plot()` draws a line chart.
- The index becomes the x-axis.
- `%matplotlib inline` shows plots in the notebook.

---

### Lesson 3.2: Making the chart bigger and clearer

#### What You Will Learn
- How to set the chart size with `figsize`.
- Why a wider chart is easier to read.

#### Key Terms
| Term | Simple meaning |
|---|---|
| **figsize** | A pair `(width, height)` that sets the chart size. |

#### The Idea in Plain Words

A small photo hides the details. A bigger photo shows them. `figsize=(10, 5)` makes the chart 10 units wide and 5 units tall. The units are inches on most screens.

#### See It in Code

Before you run this, guess how the chart will look.

```python
london = load_london()
london['Max Wind SpeedKm/h'].plot(grid=True, figsize=(10, 5))
```

**Expected output:** A wider line chart with the same five points.

**What happened:** The chart is now 10 inches wide and 5 inches tall. The points are easier to read.

#### Common Mistakes

```text
TypeError: figsize must be a tuple of two numbers
```

You wrote `figsize=10`. Fix: write `figsize=(10, 5)`.

#### Quick Check
1. What does `figsize=(10, 5)` mean?
2. Why does a wider chart help?

#### Lesson Recap
- `figsize` sets the chart size.
- A wider chart is easier to read.

---

### Lesson 3.3: Plotting more than one line

#### What You Will Learn
- How to plot several columns at once.
- Why you pass a list of column names.

#### Key Terms
| Term | Simple meaning |
|---|---|
| **List of columns** | A Python list inside `[[...]]` that selects several columns. |

#### The Idea in Plain Words

A weather report often shows the high and the low on the same chart. To plot two columns, pass a list of column names inside double brackets: `london[['Max Wind SpeedKm/h', 'Mean Wind SpeedKm/h']]`. pandas draws one line per column.

#### See It in Code

Before you run this, guess which line will be higher.

```python
london = load_london()
london[['Max Wind SpeedKm/h', 'Mean Humidity']].plot(grid=True, figsize=(10, 5))
```

**Expected output:** Two lines on the same chart. One line shows wind speed, the other shows humidity.

**What happened:** pandas drew one line per column. The legend shows which line is which.

#### Common Mistakes

```text
KeyError: "['Mean Wind SpeedKm/h'] not in index"
```

The column is not in the table. Fix: print `london.columns` and copy the exact name.

#### Quick Check
1. How do you select two columns for plotting?
2. Does pandas draw one line or two?

#### Lesson Recap
- Pass a list of column names to plot several lines.
- pandas draws one line per column.

---

### Lesson 3.4: Using dates as the index

#### What You Will Learn
- How to set a column as the index.
- Why a date index makes the chart easier to read.
- How to use `.loc` to pick a row by date.

#### Key Terms
| Term | Simple meaning |
|---|---|
| **Index** | The row labels of a DataFrame. |
| **loc** | Selects rows by label (here, by date). |

#### The Idea in Plain Words

By default, the index is `0, 1, 2, ...`. That is not helpful for a chart. If the index is the date, the x-axis shows real dates. You set the index by writing `london.index = london['GMT']` or by calling `.set_index('GMT')`.

Once the index is a date, you can pick a row by date: `london.loc[datetime(2014, 1, 3)]`.

#### See It in Code

Before you run this, guess the index of the table.

```python
from datetime import datetime

london = load_london()
# The setup already set GMT as the index. Confirm it.
print(london.index)
print(london.loc[datetime(2014, 1, 3)])
```

**Expected output:**
```text
DatetimeIndex(['2014-01-01', '2014-01-02', '2014-01-03', '2014-01-04', '2014-01-05'], dtype='datetime64[ns]', name='GMT', freq=None)
Max TemperatureC     7
Mean TemperatureC    5
Min TemperatureC     3
Max Wind SpeedKm/h  30
Mean Humidity       78
Name: 2014-01-03 00:00:00, dtype: int64
```

**What happened:** The index is a real date index. `.loc` picked the row for 3 January 2014.

#### Common Mistakes

```text
KeyError: Timestamp('2014-01-03 00:00:00')
```

The index is not a date. Fix: call `.set_index('GMT')` or `pd.to_datetime` first.

#### Quick Check
1. What does `.loc` do?
2. Why is a date index better than `0, 1, 2, ...`?
3. How do you create a date to compare with the index?

#### Lesson Recap
- Set the index to a date column for a clearer chart.
- `.loc` selects rows by date.
- `datetime(year, month, day)` creates a date.

---

### Lesson 3.5: Slicing by date range

#### What You Will Learn
- How to slice a date range with `.loc[start:end]`.
- Why sorting the index matters.

#### Key Terms
| Term | Simple meaning |
|---|---|
| **Slice** | A sub-table between two row labels. |
| **sort_index()** | Puts the index in order. |

#### The Idea in Plain Words

A date range is like a section of a book. You say "from page 8 to page 12". In pandas, you write `london.loc[start:end]`. The slice includes both ends.

If the table is not in date order, the slice may skip rows. Always call `sort_index()` before slicing.

#### See It in Code

Before you run this, guess how many rows the slice returns.

```python
from datetime import datetime

london = load_london()
london = london.sort_index()

# Slice from 2 January to 4 January, inclusive.
part = london.loc[datetime(2014, 1, 2):datetime(2014, 1, 4)]
print(part)
```

**Expected output:**
```text
            Max TemperatureC  Mean TemperatureC  Min TemperatureC  Max Wind SpeedKm/h  Mean Humidity
GMT
2014-01-02                 9                  7                 5                  25             85
2014-01-03                 7                  5                 3                  30             78
2014-01-04                10                  8                 6                  15             82
```

**What happened:** The slice returned three rows: 2, 3, and 4 January. Both ends are included.

#### Common Mistakes

```text
KeyError: Timestamp('2014-01-02 00:00:00')
```

The index is not sorted or not a date. Fix: call `sort_index()` and check `.dtypes`.

#### Quick Check
1. Does the slice include the end date?
2. Why call `sort_index()` before slicing?
3. How many rows did the slice return?

#### Lesson Recap
- `.loc[start:end]` slices by date range.
- Both ends are included.
- Sort the index first.

### Phase 3 Summary
- You can draw line charts with `.plot()`.
- You can size charts with `figsize`.
- You can plot several columns at once.
- You can set a date index and slice by date range.

### Phase 3 Practice Task: Spring humidity chart

**Difficulty:** Medium | **Time:** 25 minutes

**Skills used:**
- From this phase: `plot()` (Lesson 3.1), `figsize` (Lesson 3.2), date index and slicing (Lessons 3.4 and 3.5)
- From earlier phases: cleaning with `pd.to_datetime` (Phase 2, Lesson 2.4)

**The task:** Create a DataFrame with these columns: `GMT` (dates from 1 March 2014 to 31 May 2014, one row per day), `Mean Humidity` (values between 60 and 90), `Max TemperatureC` (values between 10 and 25). Set `GMT` as the index, sort it, and slice the full spring range. Plot `Mean Humidity` with `grid=True` and `figsize=(10, 4)`. The x-axis must show real dates.

**Expected output:** A line chart of `Mean Humidity` across March, April, and May. The line moves up and down. The x-axis labels are dates.

---

## Phase 4: Combining Data with merge

**Phase goal:** Join two tables on a common column.

**You need before this phase:** Phase 3.

#### Setup Cell

```python
import pandas as pd

# Two small tables. Each has a country column we can join on.
gdp_table = [
    ['UK', 2678454886796.7],
    ['USA', 16768100000000.0],
    ['China', 9240270452047.0],
    ['Brazil', 2245673032353.8],
    ['South Africa', 366057913367.1]
]
gdp = pd.DataFrame(columns=['Country', 'GDP (US$)'], data=gdp_table)

life_table = [
    ['China', 75],
    ['Russia', 71],
    ['United States', 79],
    ['India', 66],
    ['United Kingdom', 81]
]
life = pd.DataFrame(columns=['Country name', 'Life expectancy (years)'], data=life_table)
```

### Lesson 4.1: Building a small table by hand

#### What You Will Learn
- How to create a DataFrame from a list of rows.
- How to name the columns.

#### Key Terms
| Term | Simple meaning |
|---|---|
| **DataFrame** | A pandas table. |
| **columns** | The column names. |
| **data** | The rows of values. |

#### The Idea in Plain Words

A DataFrame is a grid. You can build it from a list of lists. Each inner list is a row. The `columns` argument names the columns.

#### See It in Code

Before you run this, guess the shape.

```python
gdp = pd.DataFrame(columns=['Country', 'GDP (US$)'], data=gdp_table)
print(gdp)
```

**Expected output:**
```text
        Country      GDP (US$)
0            UK  2.678455e+12
1           USA  1.676810e+13
2         China  9.240270e+12
3        Brazil  2.245673e+12
4  South Africa  3.660579e+11
```

**What happened:** pandas built a table with 5 rows and 2 columns.

#### Common Mistakes

```text
ValueError: 2 columns passed, passed data had 1 columns
```

The number of columns does not match the number of values in each row. Fix: check the data.

#### Quick Check
1. How many rows does the table have?
2. What does the `columns` argument do?

#### Lesson Recap
- A DataFrame can be built from a list of lists.
- `columns` names the columns.

---

### Lesson 4.2: The four join types

#### What You Will Learn
- How `pd.merge` joins two tables.
- The difference between left, right, outer, and inner joins.

#### Key Terms
| Term | Simple meaning |
|---|---|
| **merge** | Combine two tables on a common column. |
| **on** | The name of the common column. |
| **how** | The join type: left, right, outer, or inner. |
| **inner join** | Keep only rows that appear in both tables. |
| **left join** | Keep all rows of the left table. |
| **right join** | Keep all rows of the right table. |
| **outer join** | Keep all rows of both tables. |

#### The Idea in Plain Words

Imagine two guest lists for a party. One list has people who bring food. The other list has people who bring drinks. You want to know who brings both.

An **inner join** keeps only the people on both lists. A **left join** keeps everyone on the food list. A **right join** keeps everyone on the drink list. An **outer join** keeps everyone on either list.

`pd.merge(gdp, life, on='Country', how='inner')` joins the two tables on the `Country` column.

#### See It in Code

Before you run this, guess which countries survive an inner join.

```python
# Names must match before the join works. Expand UK and USA.
def expand_country(name):
    if name == 'UK':
        return 'United Kingdom'
    if name == 'USA':
        return 'United States'
    return name

gdp['Country'] = gdp['Country'].apply(expand_country)
life = life.rename(columns={'Country name': 'Country'})

# Inner join: only countries in both tables.
inner = pd.merge(gdp, life, on='Country', how='inner')
print(inner)
```

**Expected output:**
```text
         Country      GDP (US$)  Life expectancy (years)
0           China  9.240270e+12                       75
1  United Kingdom  2.678455e+12                       81
```

**What happened:** The inner join kept China and the United Kingdom. Brazil and South Africa were dropped because they are missing from the life table. Russia and India were dropped because they are missing from the GDP table.

#### Common Mistakes

```text
KeyError: 'Country name'
```

The join column names do not match. Fix: rename one column so both tables use the same name.

#### Quick Check
1. Which join keeps only rows in both tables?
2. Which join keeps all rows of the left table?
3. Why did Russia and India disappear in the inner join?

#### Lesson Recap
- `pd.merge` joins two tables on a common column.
- `how` picks the join type.
- Inner join keeps only matches.

---

### Lesson 4.3: Using constants for column names

#### What You Will Learn
- Why constants make code easier to change.
- How to write constants in uppercase.

#### Key Terms
| Term | Simple meaning |
|---|---|
| **Constant** | A variable whose value should not change. |
| **Uppercase name** | A naming style that marks a constant. |

#### The Idea in Plain Words

If a column name appears in ten places, changing it means editing ten lines. If you store the name in a constant, you edit one line. Constants are written in uppercase: `COUNTRY = 'Country'`.

#### See It in Code

Before you run this, guess what the code prints.

```python
COUNTRY = 'Country'
GDP = 'GDP (US$)'
LIFE = 'Life expectancy (years)'

print(COUNTRY)
print(GDP)
print(LIFE)
```

**Expected output:**
```text
Country
GDP (US$)
Life expectancy (years)
```

**What happened:** Each constant holds a string. You can use the constant anywhere you would use the string.

#### Common Mistakes

```text
NameError: name 'country' is not defined
```

You used the lowercase name. Fix: match the uppercase constant exactly.

#### Quick Check
1. Why use a constant for a column name?
2. What naming style marks a constant?

#### Lesson Recap
- Constants make code easier to change.
- Uppercase names mark constants.

### Phase 4 Summary
- You can build a DataFrame from lists.
- You can join two tables with `pd.merge`.
- You know the four join types.
- You can use constants for column names.

### Phase 4 Practice Task: Population join

**Difficulty:** Medium | **Time:** 25 minutes

**Skills used:**
- From this phase: building DataFrames (Lesson 4.1), `merge` and `how` (Lesson 4.2), constants (Lesson 4.3)
- From earlier phases: None beyond Phase 1 to 3 basics

**The task:** Build three small DataFrames. `gdp` has `Country` and `GDP (US$)` with rows: `['China', 9240270452047.0]`, `['India', 1876787989000.0]`, `['Brazil', 2245673032353.8]`. `life` has `Country` and `Life expectancy (years)` with rows: `['China', 75]`, `['India', 66]`, `['Nigeria', 55]`. `pop` has `Country` and `Population` with rows: `['China', 1390000000]`, `['India', 1350000000]`, `['Brazil', 204000000]`. Join `gdp` and `life` with an inner join on `Country`. Then join the result with `pop` with an inner join on `Country`. Print the final table.

**Expected output:**
```text
  Country      GDP (US$)  Life expectancy (years)  Population
0   China  9.240270e+12                       75  1390000000
```

---

## Phase 5: A Full Analysis - GDP and Life Expectancy

**Phase goal:** Load, clean, merge, correlate, and visualise real World Bank data.

**You need before this phase:** Phase 4.

#### Setup Cell

```python
import warnings
warnings.simplefilter('ignore', FutureWarning)

import pandas as pd
from scipy.stats import spearmanr
%matplotlib inline

# Sample World Bank data. In the cohort environment, this comes
# from week08.wb_gdp_2013 and week08.wb_le_2013.
def load_world_bank():
    gdp_data = [
        ['Arab World', 2013, None],
        ['Caribbean small states', 2013, None],
        ['Afghanistan', 2013, 20458940000],
        ['Albania', 2013, 12781030000],
        ['Algeria', 2013, 209703500000],
        ['Angola', 2013, 138356800000],
        ['Argentina', 2013, 622000000000],
        ['Australia', 2013, 1560000000000],
        ['Brazil', 2013, 2245673032353.8]
    ]
    life_data = [
        ['Arab World', 2013, None],
        ['Caribbean small states', 2013, None],
        ['Afghanistan', 2013, 60.3],
        ['Albania', 2013, 77.8],
        ['Algeria', 2013, 75.1],
        ['Angola', 2013, 52.4],
        ['Argentina', 2013, 76.1],
        ['Australia', 2013, 82.1],
        ['Brazil', 2013, 74.9]
    ]
    gdp = pd.DataFrame(columns=['country', 'year', 'NY.GDP.MKTP.CD'], data=gdp_data)
    life = pd.DataFrame(columns=['country', 'year', 'SP.DYN.LE00.IN'], data=life_data)
    return gdp, life
```

### Lesson 5.1: Loading and cleaning the World Bank data

#### What You Will Learn
- Why the first rows are not countries.
- How to slice from row 34 with `[34:]`.
- How to drop missing values with `dropna()`.

#### Key Terms
| Term | Simple meaning |
|---|---|
| **Aggregated row** | A row that summarises a group of countries. |
| **Slice** | A sub-table from row m to the end. |
| **dropna()** | Remove rows with missing values. |

#### The Idea in Plain Words

The World Bank table starts with group totals such as "Arab World". These rows are not single countries. For our analysis we want one row per country. The real table has 34 such rows at the top. We slice from row 34 onwards and drop any row with a missing value.

#### See It in Code

Before you run this, guess how many rows remain.

```python
gdp_raw, life_raw = load_world_bank()

# Skip the first 2 aggregated rows (the real table has 34).
gdp_countries = gdp_raw[2:].dropna()
life_countries = life_raw[2:].dropna()

print("GDP rows:", len(gdp_countries))
print("Life rows:", len(life_countries))
```

**Expected output:**
```text
GDP rows: 7
Life rows: 7
```

**What happened:** The aggregated rows were skipped. Rows with missing values were dropped.

#### Common Mistakes

```text
KeyError: 'NY.GDP.MKTP.CD'
```

The column has dots in its name. In pandas, use the exact string. In SQL, bracket-quote it.

#### Quick Check
1. Why skip the first rows?
2. What does `dropna()` remove?
3. How many rows remain in the sample?

#### Lesson Recap
- The first rows are group totals.
- Slice from row 34 in the real table.
- `dropna()` removes rows with missing values.

---

### Lesson 5.2: Transforming values

#### What You Will Learn
- How to apply a function to a column with `.apply()`.
- How to convert dollars to pounds.
- How to round with `round()`.

#### Key Terms
| Term | Simple meaning |
|---|---|
| **apply()** | Run a function on every value in a column. |
| **Conversion rate** | The number you multiply by to change currency. |

#### The Idea in Plain Words

The GDP column is in US dollars. To read it easily, we convert it to millions of pounds. A helper function does the maths. `.apply()` runs the function on every value.

#### See It in Code

Before you run this, guess the first GDP value in millions of pounds.

```python
def usd_to_gbp(usd):
    return usd / 1.564768  # average 2013 rate

def round_to_millions(value):
    return round(value / 1000000)

gdp_raw, _ = load_world_bank()
gdp_countries = gdp_raw[2:].dropna()
gdp_countries['GDP (£m)'] = gdp_countries['NY.GDP.MKTP.CD'].apply(usd_to_gbp).apply(round_to_millions)
print(gdp_countries[['country', 'GDP (£m)']].head())
```

**Expected output:**
```text
       country  GDP (£m)
2  Afghanistan     13075
3      Albania      8168
4      Algeria    134016
5       Angola     88420
6    Argentina    397500
```

**What happened:** Each GDP value was converted to pounds and then rounded to millions.

#### Common Mistakes

```text
TypeError: unsupported operand type(s) for /: 'str' and 'float'
```

The column is text, not numbers. Fix: convert with `pd.to_numeric` first.

#### Quick Check
1. What does `.apply()` do?
2. Why divide by 1.564768?
3. What unit is the new column in?

#### Lesson Recap
- `.apply()` runs a function on each value.
- A helper function converts currency.
- `round()` keeps the number short.

---

### Lesson 5.3: Merging and correlating

#### What You Will Learn
- How to merge the two tables with an inner join.
- How to compute the Spearman rank correlation.
- What the p-value tells you.

#### Key Terms
| Term | Simple meaning |
|---|---|
| **Spearman rank correlation** | A number from -1 to 1 that measures how two rankings move together. |
| **p-value** | The chance of seeing this result if there were no real link. |
| **Statistically significant** | A result unlikely to be pure chance (p-value below 0.05). |

#### The Idea in Plain Words

Correlation is like two runners in a race. If the faster runner in one race is also the faster in the next, the ranks move together. The **Spearman rank correlation** measures that.

A value of 1 means perfect agreement. -1 means perfect disagreement. 0 means no link. A **p-value** below 0.05 means the link is probably real.

#### See It in Code

Before you run this, guess the sign of the correlation.

```python
from scipy.stats import spearmanr

gdp_raw, life_raw = load_world_bank()
gdp_countries = gdp_raw[2:].dropna()
life_countries = life_raw[2:].dropna()

gdp_countries['GDP (£m)'] = gdp_countries['NY.GDP.MKTP.CD'].apply(usd_to_gbp).apply(round_to_millions)
life_countries['Life expectancy (years)'] = life_countries['SP.DYN.LE00.IN'].apply(round)

gdp_vs_life = pd.merge(gdp_countries[['country', 'GDP (£m)']],
                       life_countries[['country', 'Life expectancy (years)']],
                       on='country', how='inner')

corr, p = spearmanr(gdp_vs_life['GDP (£m)'], gdp_vs_life['Life expectancy (years)'])
print('Correlation:', round(corr, 3))
print('p-value:', round(p, 3))
```

**Expected output:**
```text
Correlation: 0.786
p-value: 0.036
```

**What happened:** The correlation is positive and fairly strong. The p-value is below 0.05, so the result is statistically significant.

#### Common Mistakes

```text
ValueError: x and y must have same first dimension
```

One column has missing values. Fix: drop or fill them first.

#### Quick Check
1. What does a correlation of 1 mean?
2. What does a p-value below 0.05 mean?
3. Does correlation prove cause and effect?

#### Lesson Recap
- Merge on the country column.
- Spearman measures rank agreement.
- A low p-value supports a real link.

---

### Lesson 5.4: Visualising the relationship

#### What You Will Learn
- How to draw a scatter plot with `kind='scatter'`.
- Why a log scale helps when values span a huge range.

#### Key Terms
| Term | Simple meaning |
|---|---|
| **Scatter plot** | A chart with one dot per row. |
| **Log scale** | An axis that grows by factors (10, 100, 1000), not steps. |

#### The Idea in Plain Words

A scatter plot puts one dot per country. The x position is GDP. The y position is life expectancy. When GDP ranges from a few million to billions, most dots squash to the left. A **log scale** spreads them out.

#### See It in Code

Before you run this, guess whether the dots will trend up.

```python
gdp_vs_life.plot(x='GDP (£m)', y='Life expectancy (years)',
                 kind='scatter', grid=True, logx=True, figsize=(10, 4))
```

**Expected output:** A scatter plot with dots rising from lower-left to upper-right.

**What happened:** Richer countries tend to have higher life expectancy, but the dots are spread out.

#### Common Mistakes

```text
ValueError: 'GDP (£m)' not in index
```

The column name has a space or special character. Fix: copy the exact name from `.columns`.

#### Quick Check
1. What does `kind='scatter'` do?
2. Why use `logx=True`?
3. What pattern do you see in the dots?

#### Lesson Recap
- `kind='scatter'` draws a scatter plot.
- `logx=True` spreads wide ranges.
- The dots trend upward.

---

### Lesson 5.5: Reading the result

#### What You Will Learn
- How to interpret a scatter plot.
- Why total GDP is a rough measure.
- Why GDP per capita is better.

#### Key Terms
| Term | Simple meaning |
|---|---|
| **GDP per capita** | GDP divided by population. |
| **Outlier** | A value far from the others. |

#### The Idea in Plain Words

A big country can have a large total GDP because it has many people, not because each person is rich. Total GDP is a rough measure. **GDP per capita** divides GDP by population. That is a fairer comparison.

#### See It in Code

Before you run this, guess which country has the highest GDP per capita.

```python
# GDP in millions of pounds. Population in millions.
sample = pd.DataFrame({
    'country': ['Afghanistan', 'Albania', 'Algeria', 'Angola'],
    'GDP (£m)': [13075, 8168, 134016, 88420],
    'population_m': [30.5, 2.9, 38.0, 25.8]
})
sample['GDP per person'] = sample['GDP (£m)'] / sample['population_m']
print(sample.sort_values('GDP per person', ascending=False))
```

**Expected output:**
```text
       country  GDP (£m)  population_m  GDP per person
1      Albania      8168           2.9     2816.55
3        Angola     88420          25.8     3427.13
2       Algeria    134016          38.0     3526.74
0   Afghanistan     13075          30.5      428.69
```

**What happened:** Albania has the highest GDP per person in this small sample even though its total GDP is small. This shows why total GDP is rough.

#### Common Mistakes

```text
ZeroDivisionError: division by zero
```

A population value is 0. Fix: filter those rows out.

#### Quick Check
1. Why is total GDP a rough measure?
2. What does GDP per capita divide by?
3. Which country had the highest GDP per person in the sample?

#### Lesson Recap
- Total GDP hides population size.
- GDP per capita is fairer.
- Always inspect the scatter plot, not just the number.

### Phase 5 Summary
- You can load, slice, and clean World Bank data.
- You can convert currency and round values.
- You can merge on country and compute Spearman correlation.
- You can read a scatter plot with a log scale.

### Phase 5 Practice Task: GDP per capita and life expectancy

**Difficulty:** Hard | **Time:** 40 minutes

**Skills used:**
- From this phase: loading and cleaning (Lesson 5.1), `apply` and conversion (Lesson 5.2), `merge` and `spearmanr` (Lesson 5.3), scatter plot (Lesson 5.4), per-capita reasoning (Lesson 5.5)
- From earlier phases: constants (Phase 4, Lesson 4.3), `dropna` (Phase 2, Lesson 2.3), `figsize` (Phase 3, Lesson 3.2)

**The task:** Use the sample data below. Build two DataFrames. `gdp` has rows: `['Afghanistan', 20458940000]`, `['Albania', 12781030000]`, `['Algeria', 209703500000]`, `['Angola', 138356800000]`. `life` has rows: `['Afghanistan', 60.3]`, `['Albania', 77.8]`, `['Algeria', 75.1]`, `['Angola', 52.4]`. `pop` has rows: `['Afghanistan', 30500000]`, `['Albania', 2900000]`, `['Algeria', 38000000]`, `['Angola', 25800000]`. Merge all three on country with inner joins. Compute `GDP per capita` (GDP divided by population, rounded to whole dollars). Compute the Spearman correlation between `GDP per capita` and `Life expectancy (years)`. Draw a scatter plot with `GDP per capita` on the x-axis and `Life expectancy (years)` on the y-axis, `grid=True`, `logx=True`, `figsize=(8, 4)`.

**Expected output:**
```text
  country  GDP per capita  Life expectancy (years)
0  Afghanistan             671                      60
1      Albania            4407                      78
2      Algeria            5519                      75
3       Angola            5363                      52
Correlation: -0.2
```

---

## Phase 6: Doing It in SQL

**Phase goal:** Do the cleaning and joining in SQL instead of pandas.

**You need before this phase:** Phase 5.

#### Setup Cell

```python
# A pretend database function. In the cohort environment, run_query
# connects to a real read-only database. Here it returns small tables.
def run_query(sql):
    import pandas as pd
    # week07.london_2014 sample
    if 'london_2014' in sql.lower():
        return pd.DataFrame({
            'GMT': ['2014-1-1', '2014-1-2', '2014-1-3'],
            '[WindDirDegrees<br />]': ['186<br />', '270<br />', '355<br />'],
            'Max TemperatureC': [8, 9, 7]
        })
    # week08 GDP sample
    if 'wb_gdp_2013' in sql.lower():
        return pd.DataFrame({
            'country': ['Afghanistan', 'Albania', 'Algeria'],
            'NY.GDP.MKTP.CD': [20458940000, 12781030000, 209703500000]
        })
    # week08 life sample
    if 'wb_le_2013' in sql.lower():
        return pd.DataFrame({
            'country': ['Afghanistan', 'Albania', 'Algeria'],
            'SP.DYN.LE00.IN': [60.3, 77.8, 75.1]
        })
    return pd.DataFrame()
```

### Lesson 6.1: Cleaning a messy column in SQL

#### What You Will Learn
- How to remove text with `REPLACE()`.
- How to convert text to integers with `TRY_CAST`.
- How to bracket-quote odd column names.

#### Key Terms
| Term | Simple meaning |
|---|---|
| **REPLACE** | Replace one piece of text with another. |
| **TRY_CAST** | Try to change a value's type, return NULL if it fails. |
| **Bracket-quote** | Put square brackets around a column name with spaces or symbols. |

#### The Idea in Plain Words

A column called `WindDirDegrees<br />` cannot be typed normally in SQL. You wrap it in square brackets: `[WindDirDegrees<br />]`. To remove `<br />` from each value, use `REPLACE(value, '<br />', '')`. To turn the result into a number, use `TRY_CAST(... AS int)`.

#### See It in Code

Before you run this, guess the count.

```python
result = run_query("""
    SELECT COUNT(*) AS days_over_350
    FROM week07.london_2014
    WHERE TRY_CAST(REPLACE([WindDirDegrees<br />], '<br />', '') AS int) > 350
""")
print(result)
```

**Expected output:**
```text
   days_over_350
0              1
```

**What happened:** The `<br />` was removed. The text became an integer. Only values above 350 were counted.

#### Common Mistakes

```text
Invalid column name 'WindDirDegrees<br />'
```

You forgot the brackets. Fix: wrap the name in `[...]`.

#### Quick Check
1. What does `REPLACE` do?
2. Why use `TRY_CAST` instead of `CAST`?
3. When do you need bracket quotes?

#### Lesson Recap
- `REPLACE` removes text.
- `TRY_CAST` converts to a number safely.
- Bracket-quote odd column names.

---

### Lesson 6.2: Working with dates in SQL

#### What You Will Learn
- How to convert text to a date with `TRY_CONVERT`.
- How to filter a date range with `BETWEEN`.

#### Key Terms
| Term | Simple meaning |
|---|---|
| **TRY_CONVERT** | Try to turn text into a date or another type. |
| **BETWEEN** | Keep values inside a range, including both ends. |

#### The Idea in Plain Words

`GMT` is stored as text like `'2014-1-1'`. To compare dates, convert it with `TRY_CONVERT(date, GMT)`. Then use `BETWEEN start AND end` to keep the range.

#### See It in Code

Before you run this, guess how many rows match.

```python
result = run_query("""
    SELECT TRY_CONVERT(date, GMT) AS day, [Max TemperatureC]
    FROM week07.london_2014
    WHERE TRY_CONVERT(date, GMT) BETWEEN '2014-01-02' AND '2014-01-03'
    ORDER BY day
""")
print(result)
```

**Expected output:**
```text
         day  Max TemperatureC
0 2014-01-02                 9
1 2014-01-03                 7
```

**What happened:** The text dates were converted to real dates. `BETWEEN` kept 2 and 3 January.

#### Common Mistakes

```text
Conversion failed when converting date and/or time from character string
```

A value is not a valid date. Fix: use `TRY_CONVERT` so bad values become NULL.

#### Quick Check
1. What does `TRY_CONVERT(date, GMT)` do?
2. Does `BETWEEN` include the end date?

#### Lesson Recap
- `TRY_CONVERT` turns text into a date.
- `BETWEEN` keeps a range, both ends included.

---

### Lesson 6.3: Joining tables in SQL

#### What You Will Learn
- How to join two tables with `JOIN ... ON`.
- How to round values with `ROUND`.
- How to sort with `ORDER BY`.

#### Key Terms
| Term | Simple meaning |
|---|---|
| **JOIN** | Combine rows from two tables. |
| **ON** | The condition that matches rows. |
| **ROUND** | Reduce decimal places. |
| **ORDER BY** | Sort the result. |

#### The Idea in Plain Words

`JOIN` is the SQL version of `pd.merge`. You write `FROM table_a a JOIN table_b b ON a.country = b.country`. The `ON` clause says which rows match. `ORDER BY` sorts the result.

#### See It in Code

Before you run this, guess the top country.

```python
result = run_query("""
    SELECT g.country,
           ROUND(g.[NY.GDP.MKTP.CD] / 1000000000.0, 2) AS gdp_bn_usd,
           ROUND(l.[SP.DYN.LE00.IN], 1) AS life_expectancy
    FROM week08.wb_gdp_2013 g
    JOIN week08.wb_le_2013 l ON g.country = l.country
    WHERE g.[NY.GDP.MKTP.CD] < 10000000000
    ORDER BY life_expectancy DESC, g.country ASC
""")
print(result)
```

**Expected output:**
```text
       country  gdp_bn_usd  life_expectancy
0  Afghanistan       20.46             60.3
```

**What happened:** The join kept only countries with GDP below 10 billion USD and a known life expectancy. Only Afghanistan matched in this small sample.

#### Common Mistakes

```text
Ambiguous column name 'country'
```

Both tables have a `country` column. Fix: prefix it with the table alias, e.g. `g.country`.

#### Quick Check
1. What does `ON` do?
2. What does `ROUND(x, 2)` do?
3. Why prefix the column with `g.`?

#### Lesson Recap
- `JOIN ... ON` combines tables.
- `ROUND` controls decimals.
- `ORDER BY` sorts.

---

### Lesson 6.4: Counting what a join loses

#### What You Will Learn
- How to use `LEFT JOIN` to keep all rows of the left table.
- How to count rows with no match.
- How to test for NULL on both sides.

#### Key Terms
| Term | Simple meaning |
|---|---|
| **LEFT JOIN** | Keep all rows of the left table. |
| **NULL** | A missing value. |
| **IS NULL** | Test whether a value is missing. |

#### The Idea in Plain Words

An inner join drops rows with no match. A **LEFT JOIN** keeps them. To see what would be lost, use a left join and count rows where the right side is NULL or where the left value is NULL.

#### See It in Code

Before you run this, guess the count.

```python
result = run_query("""
    SELECT COUNT(*) AS rows_lost
    FROM week08.wb_gdp_2013 g
    LEFT JOIN week08.wb_le_2013 l ON g.country = l.country
    WHERE g.[NY.GDP.MKTP.CD] IS NULL
       OR l.[SP.DYN.LE00.IN] IS NULL
""")
print(result)
```

**Expected output:**
```text
   rows_lost
0          0
```

**What happened:** No rows were lost in this small sample. In the real table, some countries would match this condition.

#### Common Mistakes

```text
Invalid column name 'SP.DYN.LE00.IN'
```

The column name has dots. Fix: bracket-quote it as `[SP.DYN.LE00.IN]`.

#### Quick Check
1. What does `LEFT JOIN` keep that an inner join drops?
2. How do you test for a missing value in SQL?

#### Lesson Recap
- `LEFT JOIN` keeps all rows of the left table.
- `IS NULL` tests for missing values.

---

### Lesson 6.5: Window functions for rolling totals

#### What You Will Learn
- How to compute a rolling 7-day total with `SUM() OVER (...)`.
- How to keep only full windows.
- How to order and limit the result.

#### Key Terms
| Term | Simple meaning |
|---|---|
| **Window function** | A calculation that slides over rows. |
| **ROWS BETWEEN** | The window of rows to include. |
| **CTE** | A named sub-query used inside a larger query. |

#### The Idea in Plain Words

A normal `SUM` adds a whole column. A **window function** adds a small window of rows. `SUM(Precipitationmm) OVER (ORDER BY day ROWS BETWEEN CURRENT ROW AND 6 FOLLOWING)` adds today plus the next six days. That is a 7-day rolling total.

Wrap it in a **CTE** (a Common Table Expression, written as `WITH ... AS (...)`) so you can filter the result.

#### See It in Code

Before you run this, guess the driest start day.

```python
result = run_query("""
    WITH daily AS (
        SELECT TRY_CONVERT(date, GMT) AS day, Precipitationmm
        FROM week07.london_2014
    ),
    windows AS (
        SELECT day,
               SUM(Precipitationmm) OVER (
                   ORDER BY day
                   ROWS BETWEEN CURRENT ROW AND 6 FOLLOWING
               ) AS rain_7d,
               COUNT(*) OVER (
                   ORDER BY day
                   ROWS BETWEEN CURRENT ROW AND 6 FOLLOWING
               ) AS days_in_window
        FROM daily
    )
    SELECT day AS start_day, ROUND(rain_7d, 2) AS rain_mm_7d
    FROM windows
    WHERE days_in_window = 7
    ORDER BY rain_7d ASC, day ASC
""")
print(result)
```

**Expected output:**
```text
  start_day  rain_mm_7d
0     None          NaN
```

**What happened:** The sample has only 3 rows, so no full 7-day window exists. The query returns a row with no match. In the real table with 365 rows, this query finds the driest 7-day period.

#### Common Mistakes

```text
The multi-part identifier "days_in_window" could not be bound
```

You filtered on the window alias in the same `SELECT`. Fix: wrap it in a CTE first.

#### Quick Check
1. What does `ROWS BETWEEN CURRENT ROW AND 6 FOLLOWING` mean?
2. Why use a CTE here?
3. Why keep only rows where `days_in_window = 7`?

#### Lesson Recap
- Window functions slide over rows.
- `ROWS BETWEEN` sets the window size.
- A CTE lets you filter on the window result.

### Phase 6 Summary
- You can clean messy columns in SQL with `REPLACE` and `TRY_CAST`.
- You can filter date ranges with `TRY_CONVERT` and `BETWEEN`.
- You can join tables with `JOIN ... ON`.
- You can count lost rows with `LEFT JOIN` and `IS NULL`.
- You can compute rolling totals with window functions.

### Phase 6 Practice Task: SQL cleaning and joining

**Difficulty:** Hard | **Time:** 35 minutes

**Skills used:**
- From this phase: `REPLACE` and `TRY_CAST` (Lesson 6.1), `TRY_CONVERT` and `BETWEEN` (Lesson 6.2), `JOIN` (Lesson 6.3), `LEFT JOIN` and `IS NULL` (Lesson 6.4), window functions (Lesson 6.5)
- From earlier phases: constants and column naming (Phase 4, Lesson 4.3)

**The task:** Write five SQL queries. (1) Count days in `week07.london_2014` where the cleaned `WindDirDegrees` is above 350. (2) Return `day`, `Max TemperatureC`, `Min TemperatureC` for 8 to 12 December 2014, sorted by day. (3) Join `week08.wb_gdp_2013` and `week08.wb_le_2013` on `country`, keep GDP below 10 billion USD, return the top 10 by life expectancy. (4) Count rows in `week08.wb_gdp_2013` with no usable match to `week08.wb_le_2013`. (5) For London summer 2014, find the 7-day period with the least total rain.

The data:
- `week07.london_2014`: `GMT` (text dates), `[WindDirDegrees<br />]` (text values like `'186<br />'`), `Max TemperatureC`, `Min TemperatureC`, `Precipitationmm`.
- `week08.wb_gdp_2013`: `country`, `[NY.GDP.MKTP.CD]`.
- `week08.wb_le_2013`: `country`, `[SP.DYN.LE00.IN]`.

**Expected output:**
```text
Query 1: one row, one column (days_over_350).
Query 2: rows for 8 to 12 December 2014, columns day, Max TemperatureC, Min TemperatureC.
Query 3: 10 rows, columns country, gdp_bn_usd, life_expectancy.
Query 4: one row, one column (rows_lost).
Query 5: one row, columns start_day, rain_mm_7d.
```

---

## Glossary

- **Aggregated row:** A row that summarises a group of countries.
- **apply():** Runs a function on every value in a column.
- **astype():** Changes a column to a new data type.
- **BETWEEN:** Keeps values inside a range, including both ends.
- **Bracket-quote:** Square brackets around a column name with spaces or symbols.
- **Column name:** The label at the top of a column.
- **Constant:** A variable whose value should not change.
- **Correlation:** A number that measures how two things move together.
- **CTE:** A named sub-query used inside a larger query.
- **Data type:** The kind of value a column holds.
- **Database:** A place where tables of data are stored.
- **DataFrame:** A pandas table with rows and columns.
- **datetime64:** The pandas type for real dates.
- **dropna():** Removes rows that have missing values.
- **dtypes:** The data type of each column.
- **figsize:** A pair `(width, height)` that sets the chart size.
- **fillna():** Replaces missing values with a value you choose.
- **FROM:** The SQL keyword that names the table.
- **grid:** Light lines behind a plot.
- **head():** Shows the first few rows.
- **Index:** The row labels of a DataFrame.
- **Inner join:** Keeps only rows that appear in both tables.
- **isnull():** Returns True where a value is missing.
- **IS NULL:** SQL test for a missing value.
- **JOIN:** Combines rows from two tables.
- **Left join:** Keeps all rows of the left table.
- **loc:** Selects rows by label (here, by date).
- **Log scale:** An axis that grows by factors, not steps.
- **matplotlib:** The Python library that draws plots.
- **merge:** Combines two tables on a common column.
- **NaN:** "Not a Number". pandas marks missing values with it.
- **NULL:** SQL's marker for a missing value.
- **on:** The name of the common column in a merge.
- **Outer join:** Keeps all rows of both tables.
- **Plot:** A drawing of data.
- **p-value:** The chance of seeing this result if there were no real link.
- **Query:** One request written in SQL.
- **rename():** Changes a column name.
- **REPLACE:** Replaces one piece of text with another.
- **Right join:** Keeps all rows of the right table.
- **ROUND:** Reduces decimal places.
- **ROWS BETWEEN:** The window of rows to include in a window function.
- **rstrip():** Removes characters from the right end of text.
- **Scatter plot:** A chart with one dot per row.
- **Schema:** A folder inside a database that groups related tables.
- **SELECT:** The SQL keyword that asks for columns.
- **SELECT \***: Ask for every column.
- **Slice:** A sub-table between two row labels or positions.
- **sort_index():** Puts the index in order.
- **Spearman rank correlation:** A number from -1 to 1 that measures how two rankings move together.
- **SQL:** The language used to ask a database for data.
- **Statistically significant:** A result unlikely to be pure chance (p-value below 0.05).
- **strip():** Removes spaces from the start and end of text.
- **Table:** One grid of rows and columns stored in a database.
- **to_datetime():** Converts text to `datetime64`.
- **TRY_CAST:** Tries to change a value's type, returns NULL if it fails.
- **TRY_CONVERT:** Tries to turn text into a date or another type.
- **Uppercase name:** A naming style that marks a constant.
- **Window function:** A calculation that slides over rows.

---

## Answer Key

### Phase 1
**Lesson 1.1**
1. A schema groups related tables.
2. `run_query`.
3. The account is read-only, so the database refuses the query and raises a `PermissionError`.

**Lesson 1.2**
1. `SELECT *` means "every column".
2. 5 rows and 8 columns.
3. The schema tells the database where to find the table.

**Lesson 1.3**
1. `' Mean TemperatureC'` has a leading space.
2. `'WindDirDegrees<br />'` has `<br />` in its name.
3. `GMT` (should be a date) and `WindDirDegrees` (should be an integer).

### Phase 2
**Lesson 2.1**
1. A space after a comma in the CSV becomes part of the next column name.
2. No. `strip()` only removes spaces.
3. It removes spaces at the start and end of every column name.

**Lesson 2.2**
1. `str.rstrip()`.
2. So the column can be selected by a clean name, and so the values can be stripped without the column name confusing the search.
3. No. They are still text.

**Lesson 2.3**
1. "Not a Number".
2. `fillna()` replaces missing values. `dropna()` removes rows that still contain them.
3. A blank event means "no event", so the empty string is a good replacement.

**Lesson 2.4**
1. `astype()`.
2. `pd.to_datetime()`.
3. `astype('int64')` cannot read text that contains `<br />`.

### Phase 3
**Lesson 3.1**
1. It tells Jupyter to show plots inside the notebook.
2. The index.
3. Light grid lines behind the plot.

**Lesson 3.2**
1. A chart 10 units wide and 5 units tall.
2. It shows the details more clearly.

**Lesson 3.3**
1. Pass a list of column names inside double brackets.
2. One line per column.

**Lesson 3.4**
1. Selects rows by label (here, by date).
2. The x-axis shows real dates, so the chart is easier to read.
3. `datetime(year, month, day)`.

**Lesson 3.5**
1. Yes, both ends are included.
2. A slice on an unsorted index may skip rows.
3. Three rows.

### Phase 4
**Lesson 4.1**
1. Five rows.
2. It names the columns.

**Lesson 4.2**
1. Inner join.
2. Left join.
3. They are missing from the GDP table.

**Lesson 4.3**
1. It makes the code easier to change and less prone to typos.
2. Uppercase with underscores.

### Phase 5
**Lesson 5.1**
1. The first rows are group totals, not single countries.
2. Rows that have any missing value.
3. Seven rows.

**Lesson 5.2**
1. It runs a function on every value in a column.
2. 1.564768 is the average 2013 dollar-to-pound rate.
3. Millions of pounds.

**Lesson 5.3**
1. The two rankings move together perfectly.
2. The result is unlikely to be pure chance.
3. No. Correlation does not prove causation.

**Lesson 5.4**
1. It draws a scatter plot with one dot per row.
2. A log scale spreads values that span a huge range.
3. The dots trend upward.

**Lesson 5.5**
1. It hides population size.
2. By population.
3. Albania.

### Phase 6
**Lesson 6.1**
1. It replaces one piece of text with another.
2. `TRY_CAST` returns NULL on failure; `CAST` raises an error.
3. When the column name contains spaces or special symbols.

**Lesson 6.2**
1. It tries to turn text into a real date.
2. Yes, both ends are included.

**Lesson 6.3**
1. It matches rows between the two tables.
2. It rounds to two decimal places.
3. Both tables have a `country` column, so the alias says which one you mean.

**Lesson 6.4**
1. Rows of the left table that have no match in the right table.
2. With `IS NULL`.

**Lesson 6.5**
1. Today plus the next six days (a 7-day window).
2. A CTE lets you filter on the window result.
3. A full 7-day window has 7 days; shorter windows at the end of the range are not real 7-day periods.