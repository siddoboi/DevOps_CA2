document.getElementById("feedbackForm").addEventListener("submit", function (e) {
  e.preventDefault();
  const msg = document.getElementById("message");
  const name = document.getElementById("name").value.trim();
  const email = document.getElementById("email").value.trim();
  const mobile = document.getElementById("mobile").value.trim();
  const dept = document.getElementById("department").value;
  const gender = document.querySelector('input[name="gender"]:checked');
  const feedback = document.getElementById("feedback").value.trim();

  let error = "";
  if (!name) error = "Name is required.";
  else if (!/^\S+@\S+\.\S+$/.test(email)) error = "Enter a valid email.";
  else if (!/^\d{10}$/.test(mobile)) error = "Mobile must be 10 digits.";
  else if (!dept) error = "Select a department.";
  else if (!gender) error = "Select a gender.";
  else if (feedback.split(/\s+/).filter(Boolean).length < 10) error = "Feedback must be at least 10 words.";

  msg.className = error ? "error" : "success";
  msg.textContent = error || "Feedback submitted successfully!";
  if (!error) this.reset();
});
