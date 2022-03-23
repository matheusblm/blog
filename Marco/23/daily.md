### Big-O?

Big O is the way we analyze how efficient algorithms (or code in this case) without getting too mired in the details. We can model how much any function is going to take given n inputs (thinking an array of length n), but in reality we’re interested in the order of magnitude of the number and not necessarily of the exact figure.

### Solid Principles

**S**ingle Responsibility Principle
**O**pen-Closed Principle
**L**iskov Substitution Principle
**I**nterface Segregation Principle
**D**ependency Inversion Principle

### Single Responsibility

the root of this principle, is each function or class, must have just one job.
If something its get to big or hard to understand, make a method of this.

**Mehotd**

1.  Constructors - Create objects.
2.  Setters/Getters - Each one, have one responsibility.
3.  Built-in object methods or Frameworks methods - have clear responsibilities.

Have two type of task method:

1. Atomic
2. Coordinative - Cordenate the atomic task, to make sense together

https://towardsdev.com/solid-principles-explained-635ad3608b20
