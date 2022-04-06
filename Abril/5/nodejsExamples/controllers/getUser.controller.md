import { Request, Response } from "express";
import UserRepository from "../repositories";
import { UserInterface } from "../repositories/user/interface";

const getUserController = async (\_: Request, res: Response) => {
const users: UserInterface[] = await new UserRepository().retrieveUsers();

return res.status(200).json(users);
};

export default getUserController;
