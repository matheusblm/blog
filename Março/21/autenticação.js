// banco de dados simulado
const users = [];

app.use(express.json());

app.post("/users", async (req, res) => {
  try {
    const data = {
      username: req.body.username,
      password: req.body.password,
    };

    users.push(data);

    const { password: data_password, ...dataWithoutPassword } = data;

    return res.status(201).json(dataWithoutPassword);
  } catch (e) {
    return res.json({
      message: "Error while creating an user",
    });
  }
});

// SEM O HASH DO PASSWORD

//COM O HASH

const users = [];

app.use(express.json());

app.post("/users", async (req, res) => {
  try {
    const hashedPassword = await bcrypt.hash(req.body.password, 10);

    const data = {
      username: req.body.username,
      password: hashedPassword,
    };

    users.push(data);

    const { password: data_password, ...dataWithoutPassword } = data;

    return res.status(201).json(dataWithoutPassword);
  } catch (e) {
    return res.json({
      message: "Error while creating an user",
    });
  }
});

// LOGIN COM O HASH

const config = {
  secret: "secret_key",
  expiresIn: "1h",
};

app.post("/login", async (req, res) => {
  // Descontruímos o body para obter os dados de login.
  const { username, password } = req.body;

  const user = users.find((user) => {
    return user.username === username;
  });

  try {
    // Ira retornar true/false
    const match = await bcrypt.compare(password, user.password);

    const token = jwt.sign(
      {
        username: username,
        password: user.password,
      },
      config.secret,
      { expiresIn: config.expiresIn }
    );

    if (match) {
      return res.json({ accessToken: token });
    } else {
      return res.json({ message: "Invalid Credentials" });
    }
  } catch (e) {
    return res.json({ message: "Invalid Credentials" });
  }
});
