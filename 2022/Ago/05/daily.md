## Clean Architecture on Nestjs

The architecture should tell about the system not the frameworks.

Entities Layer: Contains the bussines entites - This layer is independent
Use cases: the business scenarios - Have two dependecies DatabSe Services and CRM services

Controllers and Presenters - Are the bussiness logic.


## Maybe a other context handle 

Try use Zustand otherwise context or redux.


### Clean Code on React TS

 #### Take the previus state into account while updating the state 
Example:
setIsDisabled((isDisabled) => !isDisabled);

#### Use Enums or Constant Objects for values with multiples states

example:
 `
enum Status {
  Pending = "Pending",
  Success = "Success",
  Error = "Error",
}

  return (
    <div>
      <p>{status}</p>
    
      <button onClick={() => setStatus(Status.Pending)}>
        Pending
      </button>
      <button onClick={() => setStatus(Status.Success)}>
        Success
      </button>
      <button onClick={() => setStatus(Status.Error)}>
        Error
      </button>
    </div>
  );
};

`

### React dev tools

Its good to use besides the see a render component to see the component three and context three





