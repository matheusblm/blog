import { Request, Response } from "express";
import UserRepository from "../repositories";
import { UserInterface } from "../repositories/user/interface";

const createUserController = async (req: Request, res: Response) => {
const user: UserInterface = await new UserRepository().createUser(req.body);

return res.status(201).json(user);
};

export default createUserController;
};
