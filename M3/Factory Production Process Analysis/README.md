Mini-Project Brief
Time: 5 minutes introduction during live session
Recommended completion time: 2–4 hours individually

Scenario
A factory manager is worried that scrap is increasing in the production process. You receive a simplified production dataset and must use Pandas to investigate machine and shift performance.

Part 1 — Jupyter Notebook Analysis
Create a notebook that:

Loads the manufacturing dataset
Shows the first rows
Checks data types and missing values
Calculates scrap rate percentage
Finds the batch with the highest scrap rate
Groups results by machine
Groups results by shift
Writes 3–5 observations in markdown
Part 2 — Streamlit Dashboard
Create a simple Streamlit app that includes:

A title and short project description
The raw dataset
A machine-level summary table
A shift-level summary table
A machine filter
A short conclusion section
Part 3 — Business Interpretation
Answer:

Which machine should be investigated first?
Which shift has the highest average scrap rate?
What additional data would help confirm the root cause?
Why should we avoid blaming an operator or machine based only on this small dataset?

Practice Set 1 — Data Inspection
Load a new CSV file
Display the first 10 rows
Show the number of rows and columns
List all column names
Check data types
Find missing values

Practice Set 2 — Filtering
Show only records from Machine M1
Show only night-shift records
Show records where defective units are greater than 20
Show records where scrap rate is above 5%
Show records for Machine M2 during the evening shift

Practice Set 3 — Metrics
Create:

scrap_rate
scrap_rate_percent
good_units — units produced minus defective units
is_high_scrap — True where scrap rate is greater than 5%

Practice Set 4 — Grouping
Calculate:

Total units by machine
Total defective units by machine
Average scrap rate by machine
Average scrap rate by shift
Most common defect type by machine (if the column exists)

Practice Set 5 — Streamlit Extension
Improve your app by adding:

A shift filter
A defect type filter
A chart showing defective units by machine
A chart showing average scrap rate by shift
A warning message when scrap rate is above a chosen threshold