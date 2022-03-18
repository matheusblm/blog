### Code Review Pyramid

Principals questions to ask:

## API semantics

1. Api as small as possible, as large as needed
2. is there one way of doing one thing, not multiple ones?
3. is it consistent does it follow the principle of least surprise
4. Clean split of api/internals, withou internal leaking in the API.

## Implementation Semantics

1. Does it satisfy the original requirements
2. Is it logically correct
3. is there no unnecessary complexity
4. is it robust
5. is it performant
6. is it secure
7. is it observable
8. do newly added dependencies pull their weight?

## Documentation

1. New features reasonably documented
2. are the relevant kinds of docs covered: README
3. Are docs understandable, are there no significant typos and grammar mistakes

## Test

1. Are all test passing ?
2. Are new features reasonably tested?
3. Are corner cases tested?
4. Is it using unit test where possible integration teste where necessary?
5. Are there tests for nfrs?

## Code styles

Some of theses steps, u can automatized.


---
One Way Smart Developers Make Bad Strategic Decisions



