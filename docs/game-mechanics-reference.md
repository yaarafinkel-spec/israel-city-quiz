# Game Mechanics Reference
Source: GeoGuessr US States game (geoguessr.com/vgp/3003)

## Layout

- **Header bar (dark blue):**
  - Top-left: progress counter (e.g. `2 / 50`) and running % score
  - Top-center: prompt — "Click on **[Location Name]**" + skip button (▶|)
  - Top-right: flag/emblem of the target location, countdown timer, close button (×)
- **Main area:** full-screen interactive map, no labels, clickable regions

## Gameplay Loop

1. A location name (and its flag/emblem) appears in the header
2. User clicks on the map region they think matches
3. Feedback is shown immediately (color-coded, see below)
4. Next location is prompted automatically

## Color Feedback

| Result | Color | Meaning |
|---|---|---|
| Correct on 1st try | White | Perfect |
| Correct on 2nd try | Yellow | One mistake |
| Too many wrong guesses | Red flash → light grey | Gave up / revealed |

- Correct location briefly **flashes red** before settling to light grey when the user fails
- **Concentric circle animation** plays at the correct location on reveal (to implement later)
- Previously answered regions remain colored on the map throughout the game

## Scoring

- Score shown as percentage of correct answers
- Timer counts **up** (time elapsed), not down — no time pressure, just tracking

## Map

- US states game uses **polygon regions** — clicking anywhere inside a state's boundary counts as clicking that state
- For the Israel city quiz we will use **Voronoi regions** (each click assigned to the nearest city) to replicate this feel for point-based locations
- Toggle between Voronoi and fixed-radius modes planned as a future feature

## Data

- US game: 50 states, each with name + state flag
- Israel adaptation: cities only (to start), names in both Hebrew and English, no hints initially
