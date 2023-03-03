import axios from "axios"; // HTTP Client

const API_URL = "http://localhost:4000/api"; // The API endpoint to communicate with the server

/**
 * Handles the signup HTTP request to add a new user to the database
 * The data needed for each user is First Name, Last Name, Username, Email, and Password
 */
const signup = ({ firstName, lastName, username, email, password }) => {
  return axios.post(`${API_URL}/signup/`, {
    firstName,
    lastName,
    username,
    email,
    password,
  });
};

/**
 * Handles the login HTTP request to access your user profile
 * The data needed for each user is the username or email along with the password
 */
const login = ({ emailOrUsername, password }) => {
  return axios
    .post(`${API_URL}/login/`, { emailOrUsername, password })
    .then((res) => {
      /**
       * If successfully logged in, store the user data, inlucding the token, in the localStorage
       */
      localStorage.setItem("user", JSON.stringify(res.data));
      return res.data;
    });
};

const logout = () => {
  localStorage.removeItem("user");
};

const getCurrentUser = () => {
  return JSON.parse(localStorage.getItem("user"));
};

const AuthService = {
  signup,
  login,
  logout,
  getCurrentUser,
};

export default AuthService;
