### 5 New Killer Features of Next.js 12

Faster builds -
Middleware :
User Authentication
Bot protection
Redirects and rewrites
Handling unsupported browsers
Service-side analytics
Advanced 18n routing
Logging

URL Imports -
Support for React 18 on the server-side
Collaborative Live Coding

### 6 Secrets about “null” and “undefined” that You Should Know

undefined means that the variable has not been defined yet.
null means that the variable is defined but it does not point to any object in memory.
JavaScript creates a read-only undefined in the global environment but does not completely disable the definition of local undefined variables.

### Why React Re-Renders

Every re-render in React starts with a state changee.
And ever happen a re-render the childs componts render again too.
Re-renders only affect the component that owns the state + its descendants (if any)

### Actionless and Stateless Reducers in React

const [isOpen, toggleOpen] = useReducer((prevIsOpen) => !prevIsOpen, false);

// in event handlers or effects
toggleOpen();

const [count, increment] = useReducer(c => c + 1, 0)

increment()

### Applying SOLID principles in React

##### Single responsibility principle (SRP)

break large components that do too much into smaller components
extract code unrelated to the main component functionality into separate utility functions
encapsulate connected functionality into custom hooks

##### Open-closed principle (OCP)

Following the open-closed principle, we can reduce coupling between the components, and make them more extensible and reusable.

Liskov substitution principle (LSP)
Interface segregation principle (ISP)

##### Dependency inversion principle (DIP)

To do that, we’ll create a connected version of the LoginForm that will delegate form submission logic to the api module:
import api from '~/common/api'
const ConnectedLoginForm = () => {
const handleSubmit = async (email, password) => {
await api.login(email, password)
}
return (
<LoginForm onSubmit={handleSubmit} />
)

### Advanced React Hooks

UseContext -
Creats its ow cantext which can be wrapped around elements of your chosing.
UseLayout

useLayout has a very specific use case and is mostly used in conjunction with useRef to effect the DOM

Concurrency - Concurrency allows the programmer to control the priority of state updates in React.

UseTransition

useTransition allows the programmer to differ state update priority.

UseId

useId creates unique ids
