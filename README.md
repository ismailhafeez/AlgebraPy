# AlgebraPy
Solve algebraic problems in a flash!

AlgebraPy is a personal project developed by me to solve algebraic problems in a single line!

# Examples:

```
import AlgebraPy as AP
solver = AP.Algebra()

print(solver.Equation("x + 5 = 10")

Output: x=5 <string>
-----------------------------------------
print(solver.Equation("x+y+5=20")

Output: y+x=15 <string>
-----------------------------------------
print(solver.Equation("2x2 + 5 = 13")

Output: x=4.0 <string>
```

# FYI

As this is a project still in development, it has many limitations.

> The variable(s) *must* be the first value(s) in the equations (Ex: x + 2 = 4)
> 
> Support for Exponents and Multiples of variables has been added, but only for one variable. As of now, basic addition/subtraction/multiplication/division is also supported.
>
> Several instances of a variable (for example: 4x + 5x = 9 *or* 2x = 10 - 3x) is not supported. Only one instance of a variable can exist.
>
> The equation must *always* be given in the format **Variable** + **Constants** = **A single Constant** (for example: x + 5 = 10)

Updates will be added soon!
