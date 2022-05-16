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
