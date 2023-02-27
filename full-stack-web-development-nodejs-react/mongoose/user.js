// backend/models/user.js

// rest of the code ....

const validate = (user) => {
    const schema = Joi.object({
      firstName: Joi.string().required(),
      lastName: Joi.string().required(),
      username: Joi.string().required(),
      email: Joi.string().email().required(),
      password: Joi.string().required(),
    });
    return schema.validate(user);
  };