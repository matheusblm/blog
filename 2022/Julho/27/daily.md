### Books for JS

1. You dont know Js
2. Eloquent JavaScript: A Modern Introduction to Programming
3. JavaScript: The Good Parts
4. JavaScript: The Definitive Guide
5. Effective JavaScript: 68 Specific Ways to Harness the Power of JavaScript
6. JavaScript & JQuery: Interactive Front-End Web Development
7. Node.js In Action

### 10 powerful React Tools Taht you should know in 2022

1. Strorybook
   It's a lib for making components and pages in isolation.
2. React dev tools
   Extesion for chorme, to see react in your page.
3. Reactide
   Ide dedicated to developing React web applications
4. React Three Fiber
   Redenrer toolt for JS 3d
5. Chakra UI
6. Web3-react
7. React Query
8. Why did you render

### 11 Advanced React Interview Questions

1. What is the React Virtual Dom?
2. Why do we need to tranpile React Code?
3. What is the significance of keys in React?
4. What is the significance of refs in React?
5. What are the most common approaches for styling a React application?
6. What are some of the performance optimization strategies for React?
7. What is prop drilling and how to avoid it?
8. What is the StrictMode component and why would you use it?
9. What are synthetic events in React?
10. Why is it not advisable to update state directly, but use the setState call?
11. What are portals in React?

https://tapajyoti-bose.medium.com/11-advanced-react-interview-questions-you-should-absolutely-know-with-detailed-answers-e306083ecb7d

### Automate CI/CD Pipeline

CI is the auto compiling, buildin, analyzing and testing whenver a pr is raised.

Why do we need it?

Longer test cycles
Longer releases cycles
increase in risk of bug leakage to production users

To ensure development discipline.
To ensure the code base is always ready for release and we can receive internal feedback as early as possible in the release cycle

To minimize human errors
To remove friction across teams by standardizing the process.

Android CI Workflow
Once the PR is raised, the CircleCI workflow is created and it waits for manual approval. After the approval various checks are executed,

JIRA check ensures that every PR’s title contains a valid JIRA ID.
Checkout code steps creates the merged code base for further checks to run.
Danger check makes sure that the code in the PR follows a set of predefined rules before it is merged.
Android lint ensures the code follows Android development rules.
Config files validation step ensures that no malformed Xml or Json is pushed.
Size analysis ensures that APK size is not increased by a certain threshold.
APK Analysis ensures that no unwanted change in the app’s metadata is pushed.
Espresso tests are also triggered to make sure that the pushed code passes a predefined set of sanity checks.

##### CD - Continues delivery

Building, testing and making the app delivery-reedy for the realeases candidate.

Client side aplplication security is applied
Successful exectuin of calidations checks.
Version/taggin.

To ensure the application is ready for realaes

##### tools for CI/CD

Jenkins, Circle CI, Fastlane
