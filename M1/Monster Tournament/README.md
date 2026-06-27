Challenge: Build a “Monster Tournament Analyzer”
A fantasy coding arena is running a tournament of student-designed monsters. Each monster has a name and a list of battle scores from different rounds. Your job is to write a Python program that analyzes the tournament and decides which monsters performed best.

This feels more like a game, but it still forces students to use:

functions
lists
dictionaries
loops
conditionals
exceptions
data processing

And it can still be finished in about one hour.


Story
Each monster fought several rounds. In every round it earned a score.

Scores mean:

positive numbers = strong performance
zero = neutral round
negative numbers = disaster round

Some monsters have missing battle data, so your program must handle that safely.

Your program will process all monsters and generate a tournament report.


Starter data
Use this exact data:

monsters = [
    {"name": "Pyrofang", "scores": [12, 18, -5, 20], "element": "fire"},
    {"name": "Aquanox", "scores": [10, 0, 8, 15], "element": "water"},
    {"name": "Stoneclaw", "scores": [25, -10, 5], "element": "earth"},
    {"name": "Zephyra", "scores": [9, 14, 11, 13, 10], "element": "air"},
    {"name": "Shadowbite", "scores": [], "element": "dark"},
    {"name": "Voltaris", "scores": [30, -20, 25, -5], "element": "lightning"}
]


Your mission
Write a program that builds a full tournament analyzer.
1. Create functions
Your solution must use multiple functions. At minimum, create functions for:

calculating the total score of a monster
calculating the average round score
finding the best round
finding the worst round
assigning a rank label
deciding whether the monster is “stable” or “unstable”
building a processed monster summary
printing the tournament report


Rules for processing
For each monster:
Total score
Add all scores together.

If a monster has no scores:

total score = 0
average = 0
best round = None
worst round = None
Average score
Average of all rounds.
Rank label
Assign a rank based on total score:

Legend if total score >= 40
Elite if total score >= 25
Fighter if total score >= 10
Rookie if total score >= 0
Fallen if total score < 0
Stability
A monster is:

"Stable" if it has no negative round scores
"Unstable" if at least one round score is negative


Output structure
For each monster, create a new dictionary like this:

{
    "name": "Pyrofang",
    "element": "fire",
    "total": 45,
    "average": 11.25,
    "best": 20,
    "worst": -5,
    "rank": "Legend",
    "stability": "Unstable"
}

Store all processed monsters in a new list.


Final report must include
Print all processed monster summaries, then also print:

total number of monsters
average tournament total score
highest scoring monster
lowest scoring monster
how many monsters are in each rank
how many are stable vs unstable
all monsters of a chosen element
all monsters whose best round was at least 20


Extra challenge
Add this function:

def find_monsters_by_rank(processed_monsters, target_rank):
    ...

It should return a list of monster names with that rank.

And this one:

def find_element_team(processed_monsters, target_element):
    ...

It should return all monster names of that element.


Why this works well
It’s more fun because students are analyzing a game tournament instead of school admin data.

But under the hood it still requires exactly the right fundamentals:

functions to split the logic
lists for scores and processed results
dictionaries for structured monster data
loops for processing many monsters
conditionals for ranks and stability
exceptions for safe handling of unexpected values
data processing for totals, averages, filters, and counts


Even better: small constraints
Tell students they may only use:

for loops
if/elif/else
lists
dictionaries
functions
try/except
basic operators

No classes, no imports, no files, no advanced tricks.

That keeps it aligned with the modules.


Hint for AI-assisted students
They should use AI like a debugger and planner, not like a vending machine.

A good workflow:

Ask AI to suggest 6–8 function names.
Implement one function at a time.
Test each function with simple print() calls.
Ask AI to review edge cases like empty score lists.
Only at the end ask AI to help improve the final report formatting.


