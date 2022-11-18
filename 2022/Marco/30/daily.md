## Write code is not the same to be a Software engineer

Write code is a easy thing, its easy to learn and do.
But be a real software engineer, its hard. Because you need to improve your skills, as hard as soft skills, every day.
The world change every minute, and new realese are post every time. So if you want to be a real software engineer, its required o become better every day.

---

## React 18 changes

The first change its on the assynchourns call.
The new att bring the Concurrency definition, now the React can interrupt, pause, resume, or abandon a render.

The other big change is about bacthing, in the react above versions, when you have more than one change state, and them not be in a handle function, then will have re-render for each change state. But now this batching its automatic.


### New Feature

Transitions:
Its a feature for you to tell react that that change of state is not a property and because it is done later.
Example:

setInputValue(input);

// Mark any non-urgent state updates inside as transitions
startTransition(() => {
  // Transition: Show the results
  setSearchQuery(input);
});

--------

## A article about the key element in React

We need to use unique keys for the elements in react, because the react identify this key when gone render and re-render the elements in the page.
If we dont passa a unique key, you can have a error because two elements can have the same key and they with "work together", example: u change the props of one of this two elements, than will render, but have the chance the both dont render too.
So the basic idea is the react need the key props for localize the right element in the page.
-----

## The major difference between useCallback and UseMemo

Usecallback memoize a function
Usememo memoize a value




https://recoiljs.org/docs/introduction/getting-started
