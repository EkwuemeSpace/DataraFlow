# Streamlit: From Beginner to Professional

> **Level:** Absolute beginner to professional | **Code language:** Python | **Estimated study time:** 20–25 hours

## Table of Contents

- [How to Use This Course](#how-to-use-this-course)
- [Part 1: Foundations (Beginner)](#part-1-foundations-beginner)
  - [Lesson 1.1: Your First Streamlit App](#lesson-11-your-first-streamlit-app)
  - [Lesson 1.2: Displaying Text and Data](#lesson-12-displaying-text-and-data)
  - [Lesson 1.3: Interactive Widgets](#lesson-13-interactive-widgets)
  - [Lesson 1.4: Session State (Memory Across Reruns)](#lesson-14-session-state-memory-across-reruns)
  - [Project 1: Personal Expense Tracker](#project-1-personal-expense-tracker)
- [Part 2: Core Skills (Intermediate)](#part-2-core-skills-intermediate)
  - [Lesson 2.1: Layouts and Containers](#lesson-21-layouts-and-containers)
  - [Lesson 2.2: DataFrames and Charts](#lesson-22-dataframes-and-charts)
  - [Lesson 2.3: Caching for Speed](#lesson-23-caching-for-speed)
  - [Lesson 2.4: Forms and Callbacks](#lesson-24-forms-and-callbacks)
  - [Project 2: Interactive Sales Dashboard](#project-2-interactive-sales-dashboard)
- [Part 3: Advanced Patterns](#part-3-advanced-patterns)
  - [Lesson 3.1: Multipage Apps (st.Page and st.navigation)](#lesson-31-multipage-apps-stpage-and-stnavigation)
  - [Lesson 3.2: Database Connections and Secrets](#lesson-32-database-connections-and-secrets)
  - [Lesson 3.3: Fragments and Performance](#lesson-33-fragments-and-performance)
  - [Lesson 3.4: Authentication (st.login)](#lesson-34-authentication-stlogin)
  - [Project 3: Authenticated Customer Analytics Portal](#project-3-authenticated-customer-analytics-portal)
- [Part 4: Professional Level](#part-4-professional-level)
  - [Lesson 4.1: Testing Streamlit Apps](#lesson-41-testing-streamlit-apps)
  - [Lesson 4.2: Custom Components (v2)](#lesson-42-custom-components-v2)
  - [Lesson 4.3: Production Deployment (Docker + Nginx)](#lesson-43-production-deployment-docker--nginx)
  - [Project 4: AI-Powered Document Q&A App](#project-4-ai-powered-document-qa-app)
- [Glossary](#glossary)
- [Answer Key](#answer-key)

## How to Use This Course

- **Run every code cell.** Streamlit apps must run from a terminal, not inside a notebook. Each code block is a complete `app.py` file. Save it and run `streamlit run app.py`.
- **Do not skip the Projects.** They combine skills from every lesson before them.
- **The course is cumulative.** Lesson 3.1 (multipage apps) requires the dashboard from Project 2.
- **Version note:** This course targets Streamlit **1.66.0+**. Some features (like `st.navigation`, `st.login`, and `st.fragment`) are recent and will not work on older versions[reference:1].
- **Installation:** Run this once before starting:
  ```bash
  pip install streamlit pandas plotly
  ```

---

## Part 1: Foundations (Beginner)

**Part goal:** Build and run your first Streamlit app, display data, use widgets, and manage state.
**You need before this part:** Basic Python (variables, functions, lists, dictionaries).

### Lesson 1.1: Your First Streamlit App

#### What You Will Learn
- How to install Streamlit and run an app.
- The basic structure of a Streamlit script.
- How Streamlit reruns your script on every interaction.

#### Key Terms
| Term | Simple meaning |
|---|---|
| **Streamlit** | A Python library that turns scripts into interactive web apps. |
| **script** | A Python file that Streamlit runs from top to bottom. |
| **rerun** | Streamlit runs your whole script again when a user interacts. |
| **widget** | An interactive element like a button or slider. |

#### The Idea in Plain Words

Think of a whiteboard. Every time someone asks a question, you wipe the board and redraw everything with the new answer. Streamlit works the same way. Every time a user moves a slider or clicks a button, Streamlit reruns your script and redraws the page.

You write normal Python. Streamlit handles the web server, the HTML, and the browser updates for you.

#### Tool Card: streamlit
- **What it is:** A Python library for building data web apps.
- **What it does:** Turns Python scripts into interactive web applications with widgets and charts.
- **Why we use it here:** It is the fastest way to share data analysis and machine learning models as web apps.
- **Install:** `pip install streamlit`
- **Run:** `streamlit run app.py`
- **Other options:** Gradio (for ML demos), Dash (more complex, more control), FastAPI + HTML (full custom).

#### See It in Code

Save this as `app.py`.

```python
# app.py
# Import the Streamlit library.
import streamlit as st

# Set the page title that appears in the browser tab.
st.set_page_config(page_title="My First App", page_icon="🚀")

# Display a large title on the page.
st.title("Hello, Streamlit!")

# Display some text.
st.write("This is my first Streamlit app.")

# Display a button. When clicked, it returns True for one rerun.
if st.button("Click me"):
    st.write("You clicked the button!")
```

Run it from the terminal:

```bash
streamlit run app.py
```

**Expected output:** A browser window opens at `http://localhost:8501` showing the title, the text, and a button. Clicking the button shows the message.

**What happened:** `st.title()` and `st.write()` displayed content. `st.button()` created a widget. When clicked, Streamlit reran the script, and the `if` condition became true.

#### Common Mistakes

1. **Running the script with `python app.py`.**
   - Streamlit apps must run with `streamlit run app.py`. Running with Python executes the script once but does not start the web server.

2. **Putting Streamlit commands inside a `if __name__ == "__main__":` block.**
   - Streamlit reruns the script, but the `__name__` is always `"__main__"` in a Streamlit app. It works, but it is unnecessary. Just write the code at the top level.

#### Quick Check
1. What command starts a Streamlit app?
2. What happens when a user clicks a button?
3. Where does Streamlit run your script?

#### Lesson Recap
- Streamlit turns Python scripts into web apps.
- Run with `streamlit run app.py`.
- The script reruns on every interaction.

---

### Lesson 1.2: Displaying Text and Data

#### What You Will Learn
- How to display titles, headers, text, and markdown.
- How to display a pandas DataFrame with `st.dataframe`.
- How to display a static table with `st.table`.
- The difference between `st.write` and specialised display functions.

#### Key Terms
| Term | Simple meaning |
|---|---|
| **markdown** | A simple way to format text with symbols like `#` for headers and `**` for bold. |
| **DataFrame** | A pandas table with rows and columns. |
| **st.dataframe** | A scrollable, sortable table. |
| **st.table** | A small static table. |

#### The Idea in Plain Words

Think of a presentation. You have a title slide (`st.title`), section headers (`st.header`), bullet points (`st.write` or `st.markdown`), and data tables (`st.dataframe`).

`st.write` is a general-purpose tool. It can display text, numbers, DataFrames, and more. `st.dataframe` is specialised for large tables. It adds sorting and scrolling.

#### See It in Code

```python
# app.py
import streamlit as st
import pandas as pd

st.title("Data Display Demo")
st.header("Text Elements")

st.write("This is plain text.")
st.markdown("This is **bold** and *italic* using Markdown.")
st.code("print('Hello, world!')", language="python")

st.header("DataFrames")

# Create a small DataFrame.
data = {
    "Product": ["Apple", "Banana", "Cherry"],
    "Price": [1.20, 0.50, 3.00],
    "Stock": [100, 250, 30],
}
df = pd.DataFrame(data)

# A scrollable, interactive table.
st.subheader("st.dataframe (interactive)")
st.dataframe(df, use_container_width=True)

# A small static table.
st.subheader("st.table (static)")
st.table(df)

# Display a single metric.
st.metric(label="Total Stock", value=df["Stock"].sum())
```

**Expected output:** The page shows a title, headers, formatted text, a code block, two tables (one interactive, one static), and a metric card.

**What happened:** Each Streamlit command added one element to the page. `st.dataframe` rendered a pandas DataFrame as an interactive table.

#### Common Mistakes

1. **Using `st.table` for large DataFrames.**
   - `st.table` renders every row. For more than about 20 rows, it slows down the app. Use `st.dataframe` instead.

2. **Forgetting to import pandas.**
   - `st.dataframe` needs a pandas DataFrame. Import pandas first.

#### Quick Check
1. What is the difference between `st.dataframe` and `st.table`?
2. Which function displays a large title?
3. How do you display a single number with a label?

#### Lesson Recap
- `st.title`, `st.header`, and `st.write` display text.
- `st.dataframe` is for interactive tables. `st.table` is for small static tables.
- `st.metric` shows a single value.

---

### Lesson 1.3: Interactive Widgets

#### What You Will Learn
- How to add sliders, text inputs, select boxes, and checkboxes.
- How to read widget values into variables.
- How widgets trigger reruns.

#### Key Terms
| Term | Simple meaning |
|---|---|
| **widget** | An interactive UI element. |
| **key** | A unique name for a widget, used to access it in session state. |
| **value** | The current setting of a widget. |

#### The Idea in Plain Words

Think of a control panel. Each knob and switch is a **widget**. Turning a knob changes a value. Streamlit reads that value and reruns the script with the new number.

Each widget function returns its current value. You store that value in a variable and use it in your code.

#### See It in Code

```python
# app.py
import streamlit as st
import pandas as pd
import numpy as np

st.title("Widget Playground")

# A slider that returns an integer between 0 and 100.
number = st.slider("Pick a number", min_value=0, max_value=100, value=50)
st.write("You picked:", number)

# A text input that returns a string.
name = st.text_input("What is your name?", value="Guest")
st.write("Hello,", name)

# A select box that returns one of the options.
color = st.selectbox("Favourite colour", ["Red", "Green", "Blue"])
st.write("Your colour is", color)

# A checkbox that returns True or False.
show_data = st.checkbox("Show random data")

if show_data:
    # Generate 5 random numbers.
    random_data = pd.DataFrame(
        np.random.randn(5, 2),
        columns=["A", "B"]
    )
    st.dataframe(random_data)
```

**Expected output:** The page shows a slider, a text input, a select box, and a checkbox. Changing any widget updates the page immediately.

**What happened:** Each widget returned a value. The `if` block used the checkbox value to decide whether to show the DataFrame.

#### Common Mistakes

1. **Using the same `key` for two widgets.**
   - Streamlit raises a `DuplicateWidgetID` error. Give each widget a unique `key`.

2. **Forgetting that widgets return values.**
   - `st.slider(...)` returns the number. `st.button(...)` returns `True` or `False`.

#### Quick Check
1. What does `st.slider` return?
2. How do you make a widget unique when you have two of the same type?
3. What type of value does `st.checkbox` return?

#### Lesson Recap
- Widgets return their current value.
- Each widget triggers a rerun when changed.
- Use `key` to give widgets unique names.

---

### Lesson 1.4: Session State (Memory Across Reruns)

#### What You Will Learn
- Why normal variables reset on every rerun.
- How to store values in `st.session_state`.
- How to build a counter that survives reruns.

#### Key Terms
| Term | Simple meaning |
|---|---|
| **session state** | A dictionary-like store that persists across reruns for one user. |
| **rerun** | The script restarting from top to bottom. |
| **callback** | A function that runs before the rerun when a widget changes. |

#### The Idea in Plain Words

Think of a notebook. Every time you turn a page (rerun), you start writing on a fresh page. Normal variables are lost. **Session state** is a separate notepad that stays with you. You can write a value on it and read it again on the next page.

#### See It in Code

```python
# app.py
import streamlit as st

st.title("Session State Counter")

# Initialise the counter only once.
if "count" not in st.session_state:
    st.session_state.count = 0

# Two buttons that change the counter.
col1, col2 = st.columns(2)

with col1:
    if st.button("➕ Add 1"):
        st.session_state.count += 1

with col2:
    if st.button("➖ Subtract 1"):
        st.session_state.count -= 1

# Display the current count.
st.metric(label="Current Count", value=st.session_state.count)

# A reset button.
if st.button("Reset"):
    st.session_state.count = 0
```

**Expected output:** A counter that increases or decreases when you click the buttons. The value persists across reruns.

**What happened:** `st.session_state.count` stored the value. Without session state, the count would reset to zero on every button click.

#### Common Mistakes

1. **Trying to use a normal variable.**
```python
# Wrong: this resets to 0 on every rerun.
count = 0
if st.button("Add"):
    count += 1
st.write(count)  # Always 0 or 1.
```
Fix: Use `st.session_state`.

2. **Accessing a key that does not exist.**
   - Use `if "key" not in st.session_state:` before reading it.

#### Quick Check
1. Why do normal variables reset on every rerun?
2. How do you initialise a session state variable?
3. What is a callback used for?

#### Lesson Recap
- Session state persists values across reruns.
- Initialise keys before reading them.
- Callbacks run before the rerun.

---

### Project 1: Personal Expense Tracker

**Difficulty:** Easy | **Time:** 30 minutes

**Skills used:**
- From this part: Widgets (Lesson 1.3), session state (Lesson 1.4), DataFrames (Lesson 1.2).
- From earlier parts: None. This is your first project.

**The task:** Build a single-page app that lets a user add expenses and see the total.

Requirements:
1. A text input for the expense name.
2. A number input for the amount.
3. An "Add Expense" button.
4. A list that stores each expense in `st.session_state`.
5. A table showing all expenses.
6. A metric showing the total amount spent.

**Expected output:** The app shows an input form. Each added expense appears in a table, and the total updates automatically.

---

## Part 2: Core Skills (Intermediate)

**Part goal:** Learn layouts, charts, caching, forms, and build a complete dashboard.
**You need before this part:** Part 1.

### Lesson 2.1: Layouts and Containers

#### What You Will Learn
- How to use columns with `st.columns`.
- How to use the sidebar with `st.sidebar`.
- How to use tabs and expanders.

#### Key Terms
| Term | Simple meaning |
|---|---|
| **column** | A vertical section of the page. |
| **sidebar** | A panel on the left side for controls. |
| **tab** | A clickable label that shows one section at a time. |
| **expander** | A collapsible box. |

#### The Idea in Plain Words

Think of a newspaper. It has columns, a sidebar with quick links, and sections you can flip to. Streamlit gives you the same layout tools.

#### See It in Code

```python
# app.py
import streamlit as st

st.title("Layout Demo")

# Two columns.
col1, col2 = st.columns(2)

with col1:
    st.header("Left Column")
    st.write("This is on the left.")

with col2:
    st.header("Right Column")
    st.write("This is on the right.")

# Sidebar.
with st.sidebar:
    st.header("Controls")
    option = st.selectbox("Choose a section", ["A", "B", "C"])
    st.write("You chose:", option)

# Tabs.
tab1, tab2 = st.tabs(["Chart", "Data"])

with tab1:
    st.write("Chart goes here.")

with tab2:
    st.write("Data goes here.")

# Expander.
with st.expander("Click to see hidden details"):
    st.write("These details are hidden until you click.")
```

**Expected output:** A page with two columns, a sidebar, two tabs, and an expander.

**What happened:** `st.columns` created side-by-side sections. `st.sidebar` created a left panel. `st.tabs` and `st.expander` organised content.

#### Common Mistakes

1. **Using `st.sidebar` inside a column.**
   - The sidebar is separate from the main page. Do not nest it inside a column.

#### Quick Check
1. How do you create two columns?
2. Where does `st.sidebar` appear?
3. What is an expander used for?

#### Lesson Recap
- `st.columns` creates side-by-side layout.
- `st.sidebar` creates a control panel.
- `st.tabs` and `st.expander` organise content.

---

### Lesson 2.2: DataFrames and Charts

#### What You Will Learn
- How to display charts with Plotly.
- How to add interactive filters that update charts.
- How to use `st.metric` for KPIs.

#### Key Terms
| Term | Simple meaning |
|---|---|
| **Plotly** | A charting library that makes interactive charts. |
| **KPI** | Key Performance Indicator. A single important number. |
| **filter** | A widget that narrows the data shown. |

#### The Idea in Plain Words

Think of a dashboard in a car. You have a speedometer (a KPI), a fuel gauge (a chart), and controls (filters). Streamlit lets you build all three.

#### See It in Code

```python
# app.py
import streamlit as st
import pandas as pd
import plotly.express as px

st.title("Sales Dashboard")

# Load sample data.
@st.cache_data
def load_data():
    return pd.DataFrame({
        "Month": ["Jan", "Feb", "Mar", "Apr", "May"],
        "Sales": [100, 150, 120, 200, 180],
        "Region": ["North", "South", "North", "South", "North"],
    })

df = load_data()

# Sidebar filter.
region = st.sidebar.selectbox("Choose region", df["Region"].unique())

# Filter the data.
filtered = df[df["Region"] == region]

# KPIs.
st.metric("Total Sales", f"{filtered['Sales'].sum():,}")

# Chart.
fig = px.bar(filtered, x="Month", y="Sales", title=f"Sales in {region}")
st.plotly_chart(fig, use_container_width=True)

# Data table.
st.dataframe(filtered)
```

**Expected output:** A dashboard with a region filter, a total sales metric, a bar chart, and a data table. Changing the filter updates everything.

**What happened:** `@st.cache_data` loaded the data once. The filter narrowed the DataFrame. Plotly created the chart. `st.metric` displayed the KPI.

#### Common Mistakes

1. **Forgetting `use_container_width=True`.**
   - The chart may not fill the column. Use this argument to make it responsive.

2. **Recomputing heavy data inside the app on every rerun.**
   - Use caching (Lesson 2.3).

#### Quick Check
1. What does `st.metric` display?
2. How do you make a Plotly chart fill the container?
3. What is a KPI?

#### Lesson Recap
- Plotly makes interactive charts.
- Filters narrow data.
- `st.metric` shows KPIs.

---

### Lesson 2.3: Caching for Speed

#### What You Will Learn
- Why Streamlit reruns the script and why that is slow.
- The difference between `@st.cache_data` and `@st.cache_resource`.
- How to use caching correctly.

#### Key Terms
| Term | Simple meaning |
|---|---|
| **cache** | A store of results so you do not recompute them. |
| **st.cache_data** | Caches functions that return data (DataFrames, lists, dicts). |
| **st.cache_resource** | Caches long-lived objects (database connections, ML models). |
| **TTL** | Time To Live. How long a cache entry stays valid. |

#### The Idea in Plain Words

Think of a coffee shop. The barista remembers your usual order (cache). When you come back, they do not ask again. **Cache data** is the order. **Cache resource** is the coffee machine, which stays on and ready.

#### See It in Code

```python
# app.py
import streamlit as st
import pandas as pd
import time

st.title("Caching Demo")

# This function is slow the first time and fast afterwards.
@st.cache_data(ttl="10m", show_spinner="Loading data...")
def load_data():
    time.sleep(2)  # Simulate a slow database query.
    return pd.DataFrame({"A": [1, 2, 3], "B": [4, 5, 6]})

df = load_data()
st.dataframe(df)

# A resource cache for a database connection (example object).
@st.cache_resource
def get_connection():
    return {"status": "connected"}

conn = get_connection()
st.write("Connection status:", conn["status"])
```

**Expected output:** The first run shows a spinner for 2 seconds. The second run is instant because the data is cached.

**What happened:** `@st.cache_data` stored the DataFrame. `@st.cache_resource` stored the connection object.

#### Common Mistakes

1. **Caching a function with side effects.**
   - Cached functions should be pure: same input, same output, no side effects like writing files.

2. **Using `@st.cache_resource` for a DataFrame.**
   - DataFrames should use `@st.cache_data`. Resource caching is for objects like models and connections.

#### Quick Check
1. What is the difference between `st.cache_data` and `st.cache_resource`?
2. Why does Streamlit rerun the script?
3. What does `ttl` control?

#### Lesson Recap
- Caching stops repeated slow work.
- Data uses `@st.cache_data`. Resources use `@st.cache_resource`.
- `ttl` expires cached data after a time.

---

### Lesson 2.4: Forms and Callbacks

#### What You Will Learn
- How to group widgets into a form with `st.form`.
- How to use callbacks with `on_click` and `on_change`.
- Why forms reduce reruns.

#### Key Terms
| Term | Simple meaning |
|---|---|
| **form** | A group of widgets that submit together. |
| **callback** | A function that runs before the rerun. |
| **on_click** | A callback that runs when a button is clicked. |

#### The Idea in Plain Words

Think of a paper form. You fill in all the fields, then sign and submit once. Without a form, every field change is a submission. `st.form` groups widgets so the app reruns only when the submit button is pressed.

#### See It in Code

```python
# app.py
import streamlit as st

st.title("Form Demo")

# A form with two inputs and a submit button.
with st.form("my_form"):
    name = st.text_input("Name")
    age = st.number_input("Age", min_value=0, max_value=120, value=25)
    submitted = st.form_submit_button("Submit")

if submitted:
    st.write(f"Hello, {name}. You are {age} years old.")

# A callback example.
if "clicks" not in st.session_state:
    st.session_state.clicks = 0

def increment():
    st.session_state.clicks += 1

st.button("Click me (callback)", on_click=increment)
st.write("Clicks:", st.session_state.clicks)
```

**Expected output:** The form does not rerun on each keystroke. It reruns only when "Submit" is clicked. The second button uses a callback.

**What happened:** `st.form` grouped the inputs. The callback `increment` ran before the rerun, updating the state.

#### Common Mistakes

1. **Putting a button inside a form that is not a submit button.**
   - Use `st.form_submit_button`, not `st.button`, inside a form.

2. **Using a callback that modifies a widget’s value.**
   - Callbacks run before the rerun. Modifying a widget value in a callback can cause unexpected behaviour.

#### Quick Check
1. What is the benefit of `st.form`?
2. When does a callback run?
3. What is the difference between `st.button` and `st.form_submit_button`?

#### Lesson Recap
- Forms group widgets and reduce reruns.
- Callbacks run before the rerun.
- Use `st.form_submit_button` inside forms.

---

### Project 2: Interactive Sales Dashboard

**Difficulty:** Medium | **Time:** 45 minutes

**Skills used:**
- From this part: Layouts (Lesson 2.1), charts (Lesson 2.2), caching (Lesson 2.3), forms (Lesson 2.4).
- From earlier parts: Widgets (Lesson 1.3), session state (Lesson 1.4).

**The task:** Build a dashboard for a fictional retail company.

Requirements:
1. Load a CSV file with columns `Date`, `Product`, `Region`, `Sales`, `Quantity`.
2. Add a sidebar with filters for `Region` and `Product`.
3. Show three KPIs: total sales, total quantity, and average sale value.
4. Show a line chart of sales over time and a bar chart of sales by product.
5. Use `@st.cache_data` to load the data once.

**Expected output:** A responsive dashboard with filters, KPIs, and two charts.

---

## Part 3: Advanced Patterns

**Part goal:** Build multipage apps, connect to databases, optimise with fragments, and add authentication.
**You need before this part:** Part 2.

### Lesson 3.1: Multipage Apps (st.Page and st.navigation)

#### What You Will Learn
- How to structure a multipage app.
- How to use `st.Page` and `st.navigation`.
- How to share common elements across pages.

#### Key Terms
| Term | Simple meaning |
|---|---|
| **multipage app** | An app with more than one page. |
| **st.Page** | Defines one page. |
| **st.navigation** | Creates the navigation menu and routes to pages. |
| **entrypoint** | The file you pass to `streamlit run`. |

#### The Idea in Plain Words

Think of a book. The entrypoint is the table of contents. Each page is a chapter. `st.navigation` lets the reader jump between chapters without reloading the whole book.

`st.Page` and `st.navigation` are the preferred way to build multipage apps. The older `pages/` directory still works, but `st.navigation` gives you more control[reference:2].

#### See It in Code

Create this folder structure:

```text
my_app/
├── streamlit_app.py   (entrypoint)
├── page_home.py
└── page_settings.py
```

`streamlit_app.py`:

```python
# streamlit_app.py
import streamlit as st

# Define the pages.
home = st.Page("page_home.py", title="Home", icon="🏠")
settings = st.Page("page_settings.py", title="Settings", icon="⚙️")

# Create the navigation.
pg = st.navigation([home, settings])

# Run the selected page.
pg.run()
```

`page_home.py`:

```python
# page_home.py
import streamlit as st

st.title("Home Page")
st.write("Welcome to the home page.")
```

`page_settings.py`:

```python
# page_settings.py
import streamlit as st

st.title("Settings")
theme = st.selectbox("Theme", ["Light", "Dark"])
st.write("You chose:", theme)
```

Run `streamlit run streamlit_app.py`.

**Expected output:** A sidebar navigation menu with "Home" and "Settings". Clicking a page shows its content.

**What happened:** `st.Page` defined each page. `st.navigation` created the menu. `pg.run()` executed the selected page.

#### Common Mistakes

1. **Calling `st.navigation` more than once.**
   - It must be called exactly once per app run, in the entrypoint file.

2. **Forgetting `pg.run()`.**
   - Without `.run()`, the page content does not appear.

#### Quick Check
1. What is the entrypoint file?
2. How many times can you call `st.navigation`?
3. What does `st.Page` define?

#### Lesson Recap
- `st.Page` defines a page. `st.navigation` creates the menu.
- Call `st.navigation` once in the entrypoint.
- Use `.run()` to execute the selected page.

---

### Lesson 3.2: Database Connections and Secrets

#### What You Will Learn
- How to connect to a SQL database with `st.connection`.
- How to store passwords in `.streamlit/secrets.toml`.
- How to query data safely with parameters.

#### Key Terms
| Term | Simple meaning |
|---|---|
| **st.connection** | A Streamlit function that creates and manages database connections. |
| **secrets** | A secure way to store passwords and API keys. |
| **secrets.toml** | A local file that holds secrets. |
| **SQL injection** | An attack where user input changes the meaning of a query. |

#### The Idea in Plain Words

Think of a safe. Your database password is valuable. You do not write it on a sticky note on your desk (in the code). You put it in a safe (`secrets.toml`). Streamlit opens the safe and uses the password without showing it.

`st.connection` handles the safe, the connection, and caching. It is the recommended way to connect to databases[reference:3].

#### See It in Code

Create `.streamlit/secrets.toml`:

```toml
[connections.mydb]
dialect = "sqlite"
database = "my_database.db"
```

`app.py`:

```python
# app.py
import streamlit as st

st.title("Database Demo")

# Create a connection. Streamlit reads secrets.toml.
conn = st.connection("mydb", type="sql")

# Run a query. The result is a DataFrame.
df = conn.query("SELECT * FROM users LIMIT 10")
st.dataframe(df)

# Safe parameterised query (prevents SQL injection).
name = st.text_input("Search name")
if name:
    df = conn.query("SELECT * FROM users WHERE name = :name", params={"name": name})
    st.dataframe(df)
```

**Expected output:** The app connects to the SQLite database, shows the first 10 users, and filters by name safely.

**What happened:** `st.connection("mydb", type="sql")` created a cached connection. `conn.query()` ran the SQL. Parameters prevented SQL injection.

#### Common Mistakes

1. **Hardcoding the password in the script.**
   - Never put secrets in code. Use `secrets.toml` or environment variables.

2. **Using f-strings to build SQL.**
```python
# Wrong: SQL injection risk.
conn.query(f"SELECT * FROM users WHERE name = '{name}'")
```
Fix: Use `params={"name": name}`.

#### Quick Check
1. Where do you store secrets locally?
2. What does `st.connection` do?
3. Why are parameters safer than f-strings?

#### Lesson Recap
- `st.connection` manages database connections.
- Secrets go in `secrets.toml`.
- Use parameters to prevent SQL injection.

---

### Lesson 3.3: Fragments and Performance

#### What You Will Learn
- How to rerun only part of the app with `st.fragment`.
- How to use `run_every` for auto-refreshing sections.
- When to use fragments instead of full reruns.

#### Key Terms
| Term | Simple meaning |
|---|---|
| **fragment** | A part of the app that can rerun on its own. |
| **run_every** | Automatically rerun a fragment on a timer. |
| **full rerun** | The whole script restarts. |

#### The Idea in Plain Words

Think of a news ticker at the bottom of a TV screen. The rest of the screen stays the same, but the ticker updates every few seconds. `st.fragment` lets you build that ticker. Only the fragment reruns, not the whole app.

#### See It in Code

```python
# app.py
import streamlit as st
import time

st.title("Fragment Demo")

# A static section that does not rerun.
st.write("This section stays the same.")

# A fragment that updates every 2 seconds.
@st.fragment(run_every="2s")
def live_clock():
    st.metric("Current time", time.strftime("%H:%M:%S"))

live_clock()

# A fragment triggered by a button.
@st.fragment
def counter():
    if "count" not in st.session_state:
        st.session_state.count = 0
    if st.button("Increment"):
        st.session_state.count += 1
    st.write("Count:", st.session_state.count)

counter()
```

**Expected output:** The clock updates every 2 seconds without rerunning the whole page. The counter updates only its own section.

**What happened:** `@st.fragment` isolated the clock and counter. Only those sections reran.

#### Common Mistakes

1. **Putting a fragment around the whole app.**
   - Fragments are for small sections. Wrapping everything defeats the purpose.

2. **Using `run_every` for expensive operations.**
   - Auto-refreshing fragments can waste resources. Use them for lightweight updates.

#### Quick Check
1. What does `st.fragment` do?
2. What does `run_every` control?
3. When should you use a fragment?

#### Lesson Recap
- Fragments rerun independently.
- `run_every` refreshes on a timer.
- Use fragments for small, frequent updates.

---

### Lesson 3.4: Authentication (st.login)

#### What You Will Learn
- How to add login with an OIDC provider.
- How to access user information with `st.user`.
- How to log out with `st.logout`.

#### Key Terms
| Term | Simple meaning |
|---|---|
| **OIDC** | OpenID Connect. A standard for logging in with Google, Microsoft, and others. |
| **st.login** | Starts the login flow. |
| **st.user** | Contains the logged-in user's information. |
| **st.logout** | Logs the user out. |

#### The Idea in Plain Words

Think of a building with a security desk. You show your ID (login), the guard checks it (OIDC provider), and you get a visitor badge (cookie). `st.login` sends you to the security desk. `st.user` is your badge.

Streamlit 1.42+ has native OIDC authentication[reference:4].

#### See It in Code

Create `.streamlit/secrets.toml`:

```toml
[auth]
redirect_uri = "http://localhost:8501/oauth2callback"
cookie_secret = "your-random-secret"
client_id = "your-client-id"
client_secret = "your-client-secret"
server_metadata_url = "https://accounts.google.com/.well-known/openid-configuration"
```

`app.py`:

```python
# app.py
import streamlit as st

st.title("Authenticated App")

# Check if the user is logged in.
if not st.user.is_logged_in:
    st.write("Please log in to continue.")
    st.login()  # Redirects to the OIDC provider.
else:
    st.write(f"Welcome, {st.user.name}!")
    st.write(f"Your email is {st.user.email}.")
    if st.button("Log out"):
        st.logout()
```

**Expected output:** Unauthenticated users see a "Log in" prompt. Logged-in users see their name and email.

**What happened:** `st.login()` redirected to the provider. `st.user` held the user data. `st.logout()` cleared the session.

> **Going deeper:** Install `streamlit[auth]` to get the required `Authlib` dependency[reference:5].

#### Common Mistakes

1. **Using OAuth instead of OIDC.**
   - Streamlit requires OIDC. Generic OAuth is not supported.

2. **Hardcoding the `redirect_uri`.**
   - When deploying, update the `redirect_uri` to the production URL.

#### Quick Check
1. What does `st.login()` do?
2. Where is user information stored?
3. What is OIDC?

#### Lesson Recap
- `st.login()` starts OIDC authentication.
- `st.user` holds user details.
- `st.logout()` ends the session.

---

### Project 3: Authenticated Customer Analytics Portal

**Difficulty:** Hard | **Time:** 60 minutes

**Skills used:**
- From this part: Multipage apps (Lesson 3.1), database connections (Lesson 3.2), fragments (Lesson 3.3), authentication (Lesson 3.4).
- From earlier parts: Caching (Lesson 2.3), charts (Lesson 2.2).

**The task:** Build a multipage analytics portal.

Requirements:
1. A login page using `st.login`.
2. Two pages: "Overview" (KPIs and charts) and "Data Explorer" (a searchable table).
3. The Overview page uses `@st.cache_data` to load data from a SQLite database.
4. The Data Explorer page uses `st.fragment` to filter the table without rerunning the whole page.
5. Only logged-in users can access the pages.

**Expected output:** A secure app with login, navigation, KPIs, and an interactive data explorer.

---

## Part 4: Professional Level

**Part goal:** Test apps, build custom components, deploy to production, and build an AI app.
**You need before this part:** Part 3.

### Lesson 4.1: Testing Streamlit Apps

#### What You Will Learn
- How to use `AppTest` to test your app without a browser.
- How to simulate user input.
- How to assert on the output.

#### Key Terms
| Term | Simple meaning |
|---|---|
| **AppTest** | Streamlit's testing class. It runs the app in memory. |
| **pytest** | A Python testing framework. |
| **assertion** | A check that a condition is true. |

#### The Idea in Plain Words

Think of a crash test dummy. You do not crash a real car to test safety. You use a dummy. `AppTest` is the dummy for your Streamlit app. It runs the app in memory and lets you click buttons and check results without opening a browser.

#### See It in Code

Create `test_app.py`:

```python
# test_app.py
from streamlit.testing.v1 import AppTest

def test_counter():
    # Load the app.
    at = AppTest.from_file("app.py")
    at.run()

    # Check the initial state.
    assert at.session_state.count == 0

    # Click the "Add 1" button.
    at.button[0].click().run()

    # Check the new state.
    assert at.session_state.count == 1
```

Run the test:

```bash
pytest test_app.py
```

**Expected output:**
```text
test_app.py .                                                       [100%]
```

**What happened:** `AppTest` loaded `app.py`, simulated a button click, and checked the session state.

#### Common Mistakes

1. **Testing UI details instead of logic.**
   - Test that the correct data and state are produced, not the exact HTML.

2. **Forgetting to call `.run()` after `.click()`.**
   - The app does not update until you call `.run()`.

#### Quick Check
1. What does `AppTest` do?
2. How do you simulate a button click?
3. What should you assert in a test?

#### Lesson Recap
- `AppTest` tests apps without a browser.
- Simulate input with `.click()` and `.run()`.
- Assert on state and data.

---

### Lesson 4.2: Custom Components (v2)

#### What You Will Learn
- When to build a custom component.
- How to register a component with `st.components.v2.component`.
- How to mount it.

#### Key Terms
| Term | Simple meaning |
|---|---|
| **custom component** | A UI element built with HTML, CSS, or JavaScript. |
| **v2 component** | The modern component API with better performance. |
| **registration** | Defining the component. |
| **mounting** | Placing an instance of the component in the app. |

#### The Idea in Plain Words

Think of a power strip. Streamlit gives you several sockets (built-in widgets). If you need a socket that does not exist, you build one (custom component) and plug it in.

Custom Components v2 are the modern way. They do not use iframes and support multiple callbacks[reference:6].

#### See It in Code

```python
# app.py
import streamlit as st

# Register the component with HTML and CSS.
my_component = st.components.v2.component(
    name="my_badge",
    html="""
        <div class="badge">
            {{ text }}
        </div>
    """,
    css="""
        .badge {
            background: #0066cc;
            color: white;
            padding: 8px 16px;
            border-radius: 20px;
            display: inline-block;
        }
    """,
)

st.title("Custom Component Demo")

# Mount the component and pass data.
my_component(text="Hello from a custom component!")
```

**Expected output:** A blue badge with white text appears on the page.

**What happened:** `st.components.v2.component` registered the component. Calling it mounted it with the `text` value.

#### Common Mistakes

1. **Using the v1 API (`components.declare_component`).**
   - v2 is the current standard. v1 uses iframes and is slower.

2. **Forgetting to register before mounting.**
   - The component must be registered with `st.components.v2.component` before you call it.

#### Quick Check
1. When should you build a custom component?
2. What is the difference between registration and mounting?
3. Why is v2 better than v1?

#### Lesson Recap
- Custom components extend Streamlit with custom UI.
- v2 is the modern API.
- Register, then mount.

---

### Lesson 4.3: Production Deployment (Docker + Nginx)

#### What You Will Learn
- How to containerise a Streamlit app with Docker.
- How to put Nginx in front as a reverse proxy.
- How to use Docker Compose.

#### Key Terms
| Term | Simple meaning |
|---|---|
| **Docker** | A tool that packages an app and its dependencies into a container. |
| **container** | A lightweight, isolated runtime environment. |
| **Nginx** | A web server used as a reverse proxy. |
| **reverse proxy** | A server that sits in front of your app and forwards requests. |
| **Docker Compose** | A tool for running multiple containers together. |

#### The Idea in Plain Words

Think of a shipping container. It holds everything the app needs: Python, libraries, and code. You can move it to any server and it runs the same way. **Docker** builds the container. **Nginx** is the port authority that directs traffic to the right container.

#### See It in Code

Create `Dockerfile`:

```dockerfile
# Dockerfile
FROM python:3.12-slim

WORKDIR /app

# Copy requirements and install.
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy the rest of the app.
COPY . .

# Expose the Streamlit port.
EXPOSE 8501

# Run Streamlit.
HEALTHCHECK CMD curl --fail http://localhost:8501/_stcore/health || exit 1
ENTRYPOINT ["streamlit", "run", "app.py", "--server.port=8501", "--server.address=0.0.0.0"]
```

Create `docker-compose.yml`:

```yaml
# docker-compose.yml
version: "3.9"

services:
  streamlit:
    build: .
    container_name: streamlit_app
    restart: unless-stopped
    ports:
      - "8501"

  nginx:
    image: nginx:alpine
    container_name: nginx_proxy
    restart: unless-stopped
    ports:
      - "80:80"
    volumes:
      - ./nginx.conf:/etc/nginx/nginx.conf:ro
    depends_on:
      - streamlit
```

Create `nginx.conf`:

```nginx
# nginx.conf
events {}

http {
    server {
        listen 80;

        location / {
            proxy_pass http://streamlit:8501;
            proxy_http_version 1.1;
            proxy_set_header Upgrade $http_upgrade;
            proxy_set_header Connection "upgrade";
            proxy_set_header Host $host;
        }
    }
}
```

Build and run:

```bash
docker compose up -d --build
```

**Expected output:** The app is available at `http://localhost` (port 80), proxied by Nginx to the Streamlit container.

**What happened:** Docker built the app image. Compose started the Streamlit and Nginx containers. Nginx forwarded requests.

> **Version note:** For production with more than 3 concurrent users, use a load balancer or a managed platform. Community Cloud is free for demos but has resource limits[reference:7].

#### Common Mistakes

1. **Not setting `--server.address=0.0.0.0`.**
   - The app binds to localhost inside the container and is not reachable from outside.

2. **Forgetting the WebSocket headers in Nginx.**
   - Streamlit uses WebSockets. Without `Upgrade` and `Connection` headers, the app will not connect.

#### Quick Check
1. What does Docker package?
2. What is a reverse proxy?
3. Why does Nginx need WebSocket headers?

#### Lesson Recap
- Docker packages the app and dependencies.
- Nginx proxies traffic to Streamlit.
- Use Compose to run both.

---

### Project 4: AI-Powered Document Q&A App

**Difficulty:** Capstone | **Time:** 90 minutes

**Skills used:**
- From this part: Testing (Lesson 4.1), custom components (Lesson 4.2), deployment (Lesson 4.3).
- From earlier parts: Caching (Lesson 2.3), secrets (Lesson 3.2), fragments (Lesson 3.3), authentication (Lesson 3.4).

**The task:** Build and deploy an AI app.

Requirements:
1. A chat interface using `st.chat_message` and `st.chat_input`.
2. A sidebar for uploading PDF documents.
3. An OpenAI API key stored in `secrets.toml`.
4. A cached function that embeds the document (use `@st.cache_resource` for the model).
5. An answer generated with the OpenAI API.
6. A test using `AppTest` that checks the chat input exists.
7. A Dockerfile and Nginx configuration for deployment.

**Expected output:** A secure, deployable app where a user uploads a PDF and asks questions about it.

---

## Glossary

| Term | Simple meaning |
|---|---|
| **AppTest** | Streamlit's testing class that runs the app in memory. |
| **cache** | A store of results to avoid recomputation. |
| **callback** | A function that runs before the rerun. |
| **container** | An isolated runtime environment. |
| **custom component** | A UI element built with HTML, CSS, or JavaScript. |
| **Docker** | A tool for packaging apps into containers. |
| **entrypoint** | The file passed to `streamlit run`. |
| **fragment** | A part of the app that reruns independently. |
| **KPI** | Key Performance Indicator. A single important metric. |
| **markdown** | A simple text formatting language. |
| **multipage app** | An app with more than one page. |
| **Nginx** | A web server used as a reverse proxy. |
| **OIDC** | OpenID Connect. A standard for authentication. |
| **Plotly** | An interactive charting library. |
| **rerun** | Streamlit restarting the script from the top. |
| **reverse proxy** | A server that forwards requests to another server. |
| **secrets** | A secure store for passwords and API keys. |
| **session state** | A dictionary-like store that persists across reruns. |
| **st.cache_data** | A cache for functions that return data. |
| **st.cache_resource** | A cache for long-lived objects. |
| **st.connection** | A Streamlit function that manages database connections. |
| **st.fragment** | A decorator that isolates part of the app. |
| **st.login** | Starts the OIDC login flow. |
| **st.navigation** | Creates the navigation menu in a multipage app. |
| **st.Page** | Defines a page in a multipage app. |
| **st.session_state** | The session state object. |
| **Streamlit** | A Python library for building data web apps. |
| **ttl** | Time To Live. How long a cache entry stays valid. |
| **widget** | An interactive UI element. |

## Answer Key

### Lesson 1.1
1. `streamlit run app.py`.
2. Streamlit reruns the script from top to bottom.
3. On the Streamlit server, in the browser.

### Lesson 1.2
1. `st.dataframe` is interactive and scrollable. `st.table` is static and best for small tables.
2. `st.title`.
3. `st.metric`.

### Lesson 1.3
1. The current number on the slider.
2. Give each widget a unique `key`.
3. `True` or `False`.

### Lesson 1.4
1. Streamlit reruns the whole script, so variables are recreated from scratch.
2. `if "key" not in st.session_state: st.session_state.key = value`.
3. A callback runs before the rerun to update state or perform an action.

### Lesson 2.1
1. `st.columns(2)`.
2. On the left side of the page.
3. To hide details until the user clicks to expand.

### Lesson 2.2
1. A single KPI value with a label.
2. `use_container_width=True`.
3. Key Performance Indicator. A single important number.

### Lesson 2.3
1. `st.cache_data` is for data (DataFrames, lists). `st.cache_resource` is for objects (models, connections).
2. Streamlit reruns the script on every interaction.
3. How long a cache entry stays valid before it is recomputed.

### Lesson 2.4
1. It groups widgets so the app reruns only when the submit button is clicked.
2. Before the rerun.
3. `st.form_submit_button` is used inside forms. `st.button` is used outside forms.

### Lesson 3.1
1. The file passed to `streamlit run`, which defines the navigation.
2. Exactly once per app run.
3. One page in a multipage app.

### Lesson 3.2
1. `.streamlit/secrets.toml`.
2. It creates and manages a database connection with caching.
3. Parameters prevent user input from changing the SQL structure.

### Lesson 3.3
1. It allows part of the app to rerun without rerunning the whole script.
2. How often a fragment reruns automatically.
3. For small, frequently updated sections.

### Lesson 3.4
1. It redirects the user to the OIDC provider for login.
2. In `st.user`.
3. OpenID Connect. An authentication standard.

### Lesson 4.1
1. It runs the app in memory for testing without a browser.
2. `at.button[0].click().run()`.
3. The state and data the app produces, not the exact HTML.

### Lesson 4.2
1. When built-in widgets do not meet your needs.
2. Registration defines the component. Mounting places an instance in the app.
3. v2 does not use iframes, is faster, and supports multiple callbacks.

### Lesson 4.3
1. The app and all its dependencies.
2. A server that forwards requests to another server.
3. Streamlit uses WebSockets, which require these headers to connect.