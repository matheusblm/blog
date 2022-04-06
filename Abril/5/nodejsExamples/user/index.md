import { getRepository, Repository } from "typeorm";
import { User } from "../../entities/User";

class UserRepository implements UserRepo {
private ormRepo: Repository;
constructor() {
this.ormRepo = getRepository(User);
}
createUser = async (user: UserInterface) => await this.ormRepo.save(user);
retrieveUsers = async () => await this.ormRepo.find();
}

export default UserRepository;
