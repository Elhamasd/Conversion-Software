var videoPlayer;
var userCompleteButton;

// Bind events
document.addEventListener('DOMContentLoaded', function () {
	console.log("Player started...")

	// Initialize SCORM connection.
	pipwerks.SCORM.connection.initialize();

	// Register unload event to terminate SCORM connection.
	window.addEventListener("beforeunload", terminateScormConnection);

	// Get element references.
	videoPlayer = document.getElementById("video-player");
	userCompleteButton = document.getElementById("user-complete-button");

	// Add username to completion button.
	userCompleteButton.innerHTML = "I, " + pipwerks.SCORM.data.get('cmi.core.student_name') + ", declare that I have read this document.";

	// Create events.
	videoPlayer.addEventListener("ended", onVideoPlayerEnded);
	userCompleteButton.addEventListener("click", onUserCompleteButtonClick);

}, false);

function onVideoPlayerEnded() {
	sendScormCompletion();
}

function onUserCompleteButtonClick() {
	sendScormCompletion();
}

function sendScormCompletion() {
	console.log("Sending SCORM completion...");

	pipwerks.SCORM.data.set("cmi.core.score.raw", 100);
	pipwerks.SCORM.data.set("cmi.core.lesson_status", "passed");
}

function terminateScormConnection() {
	pipwerks.SCORM.connection.terminate();
}
