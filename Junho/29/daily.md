## Effective Software Testing

This article its a resume of the book Effective Software Testing - Mauricio Aniche

### Specification-Based Testing

1. Understading what the program does
2. identify the types and domains of the inputs and outputs.
3. Find all different partitions
4. go through each input individually, fill with null, empty, string of lengeth X.
5. Go trough each input in combination with the other inputs.
6. Find the boundaries betwwen partitions. Example c < 10, so C need to test with the value 9.
7. Augment the test suite with creativity and experience.

### Structural testing and code coverage

The next step its to veridy the coverage of the source code, to see if there are parts that havent been executed.

The goal is not have 100% of coverage, its cover all the importants stuff.
the author is against using only one assert per test. Frequently it makes sense to use many.

https://henrikwarne.com/2022/06/19/effective-software-testing-a-developers-guide/?utm_source=programmingdigest&utm_medium=email&utm_campaign=478
