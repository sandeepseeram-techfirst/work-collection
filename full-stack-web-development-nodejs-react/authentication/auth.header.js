export default function authHeader() {
    /**
     * Get the current user stored in the localStorage and parse it as a JSON
     * so we can access the user object easily in JavaScript
     */
    const user = JSON.parse(localStorage.getItem("user"));
  
    /**
     * Check if the user is undefined (exists) and has a token
     * so you can use that token in the authenticated requests to the server
     * If there is no user, then return an empty object and the server should reject the request
     */
    if (user && user.token) {
      return { "x-access-token": user.token };
    } else {
      return {};
    }
  }
  