const countdownDuration = 25 * 60 * 1000; // 25 minutes in milliseconds
let endTime;
let timerInterval;
let isRunning = false;

// Function to start the countdown
function startCountdown() {
  if (isRunning) return; // Prevent multiple intervals

  const now = new Date().getTime();
  endTime = localStorage.getItem("endTime")
    ? parseInt(localStorage.getItem("endTime"), 10)
    : now + countdownDuration;

  localStorage.setItem("endTime", endTime);
  isRunning = true;
  updateTimer();
}

// Function to update the timer display
function updateTimer() {
  const now = new Date().getTime();
  const remainingTime = endTime - now;

  if (remainingTime <= 0) {
    document.getElementById("timer").innerText = "00:00";
    localStorage.removeItem("endTime"); // Clear the end time
    clearInterval(timerInterval);
    isRunning = false;
    return;
  }

  const minutes = Math.floor((remainingTime % (1000 * 60 * 60)) / (1000 * 60));
  const seconds = Math.floor((remainingTime % (1000 * 60)) / 1000);
  document.getElementById("timer").innerText = `${String(minutes).padStart(
    2,
    "0"
  )}:${String(seconds).padStart(2, "0")}`;

  timerInterval = setTimeout(updateTimer, 1000);
}

// Function to stop the timer
function stopTimer() {
  clearTimeout(timerInterval);
  isRunning = false;
}

// Function to reset the timer
function resetTimer() {
  localStorage.removeItem("endTime");
  document.getElementById("timer").innerText = "25:00";
  stopTimer();
  isRunning = false;
}

// Check if there's an existing end time in localStorage
const storedEndTime = localStorage.getItem("endTime");
if (storedEndTime) {
  endTime = parseInt(storedEndTime, 10);
  updateTimer();
} else {
  document.getElementById("timer").innerText = "25:00";
}

// Add event listeners to the buttons
document
  .getElementById("startButton")
  .addEventListener("click", startCountdown);
document.getElementById("stopButton").addEventListener("click", stopTimer);
document.getElementById("resetButton").addEventListener("click", resetTimer);
