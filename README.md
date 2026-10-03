# Susceptible-Infected-Recovered* Simulation

This program simulates infection spread from given values

## Dependencies

python 3.x

matplotlib

## How it works

Each generation a number of the healthy population becomes infected determined by the `infection_rate` input

The program tracks the remainder of infections in a remainder variable while displaying whole numbers, `if remainder >= 1`, `infected += 1` and `remainder -= 1`

## Inputs
```
Population: 10000
Infection Rate: 20
Infected Start: 4
Generations to run: 10
```

## Output (Simplified)
```
---------------
Generation: 1
Infected: 2003
Healthy: 7997
Remainder: 0.20000000000004547
---------------

...

---------------
Generation: 10
Infected: 8927
Healthy: 1073
Remainder: 4.547473508864641e-13
---------------
```
## Known limitations

R / Recovered not yet implemented, no function for infected to recover to healthy is in place, therefore more accurately this is a (SI) simulation.

This program assumes infection rate is between 0-100

## Planned Updates
Add "Recovered" variable to complete a full (SIR) model


## Change Log

Changed `infection_rate` from `int` to `float`

Added infection plotting using matplotlib

Changed how generations are printed, now 1-n, previously of n-1
