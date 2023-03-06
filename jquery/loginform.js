const login = document.getElementById("login");
const loginMenu = document.getElementById("loginMenu");
login.addEventListener("click", () => {
 if(loginMenu.style.display === "none"){
  loginMenu.style.display = "inline";
 } else {
  loginMenu.style.display = "none";
 }
});