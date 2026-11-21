# Cosmetology Board Deck

A spaced-repetition flashcard app for the Georgia cosmetology exam.

- `data/cards.jsonl`: 132 questions transcribed from the "Cosmetology GA test" screenshots (IMG_8308–IMG_8374).
- `data/explanations.py`: a short explanation and an optional diagram key for each card.
- `app/template.html`: the app (scheduling, study screen, import, diagrams).
- `app/build.py`: merges the data into the template and writes `app/index.html`.

Scheduling: correct answers come back in 1 day, and the gap grows with each later correct answer. A first wrong answer comes back in 10 minutes; a second wrong answer in a row comes back in 5 minutes.

Rebuild with `python3 app/build.py`.
