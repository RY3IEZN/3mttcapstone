/** @format */

const form = document.querySelector("#userForm");

form.addEventListener("submit", async (e) => {
  e.preventDefault();

  const name = document.querySelector("#name").value;
  const email = document.querySelector("#email").value;

  const response = await fetch(
    "https://us-central1-capstone-442608.cloudfunctions.net/save_user_input",
    {
      method: "POST",
      headers: {
        "Content-Type": "application/json",
      },
      body: JSON.stringify({ name, email }),
    }
  );

  const result = await response.json();
  alert(result.message);
});
