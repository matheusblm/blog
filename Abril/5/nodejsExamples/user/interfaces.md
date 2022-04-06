interface UserInterface {
id?: number
firstName: string
lastName: string
age: number
}

interface UserRepo {
createUser: (user: UserInterface) => Promise
retrieveUsers: () => Promise
}

export { UserInterface, UserRepo }
