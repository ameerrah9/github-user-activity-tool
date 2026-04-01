# GitHub User Activity Tool

A simple Python CLI application that fetches and displays recent activity of a GitHub user using the GitHub API.

## Project Overview

This project teaches you how to:

- Work with REST APIs in Python
- Parse JSON responses
- Build a command-line interface (CLI)
- Handle errors gracefully
- Use Python's built-in libraries

## Getting Started

### Prerequisites

- Python 3.6 or higher
- Terminal/Command line access
- Internet connection

### Installation

1. Clone or download this project
2. Navigate to the project directory:
   ```bash
   cd github-activity-tool
   ```

## Usage

```bash
python main.py <github-username>
```

**Example:**

```bash
python main.py kamranahmedse
```

**Expected Output:**

```
- Pushed 3 commits to kamranahmedse/developer-roadmap
- Opened a new issue in kamranahmedse/developer-roadmap
- Starred kamranahmedse/developer-roadmap
- ...
```

## Step-by-Step Implementation Guide

This guide breaks down the implementation into manageable steps. Try each step on your own first, then review the solution before moving to the next step.

### Step 1: Parse Command-Line Arguments

**Objective:** Accept a GitHub username as a command-line argument.

**Guidance:**

- Use Python's built-in `sys` module to access command-line arguments
- `sys.argv` is a list where `sys.argv[0]` is the script name
- Check if a username was provided, else show an error message

**Try it yourself!**

- Write code to check if the user provided an argument
- If no argument, print: "Usage: python main.py <github-username>"
- If an argument is provided, print: "Fetching activity for: <username>"

**When ready to check your work, let me know and I'll show you the solution!**

---

### Step 2: Fetch Data from GitHub API

**Objective:** Make an HTTP request to the GitHub API and retrieve user events.

**Guidance:**

- Use Python's built-in `urllib` module (specifically `urllib.request` and `urllib.error`)
- GitHub API endpoint: `https://api.github.com/users/<username>/events`
- You'll receive a JSON array of events
- **No external libraries allowed!**

**Key points:**

- Set a User-Agent header (GitHub API requires this)
- Handle network errors gracefully
- Handle 404 errors (user not found)

**Try it yourself!**

- Create a function to fetch user activity
- Make the HTTP request using the GitHub username
- Parse the JSON response
- Return the data

**When ready to check your work, let me know!**

---

### Step 3: Parse and Format the Activity

**Objective:** Transform API response into human-readable descriptions.

**Guidance:**

- GitHub events have different types: `PushEvent`, `IssuesEvent`, `StarEvent`, `PullRequestEvent`, etc.
- Each event has a `type` field and `payload` with event-specific details
- We need to format each event into a readable message

**Example event structure:**

```json
{
  "type": "PushEvent",
  "repo": {
    "name": "kamranahmedse/developer-roadmap"
  },
  "payload": {
    "commits": [...],
    "size": 3
  }
}
```

**Try it yourself!**

- Parse each event from the API response
- Create a function to format different event types
- Handle at least these event types: PushEvent, IssuesEvent, StarEvent
- Return formatted strings like "Pushed X commits to owner/repo"

**When ready to check your work, let me know!**

---

### Step 4: Display Results

**Objective:** Print the formatted activity to the terminal.

**Guidance:**

- Iterate through the formatted events
- Print each one with a dash prefix: `- Event description`
- Handle empty results gracefully

**Try it yourself!**

- Combine all previous steps into the main script
- Display the activity nicely
- Test with a real GitHub username (e.g., "torvalds", "gvanrossum")

**When ready to check your work, let me know!**

---

### Step 5: Error Handling (Bonus)

**Objective:** Make the tool robust against errors.

**Guidance:**

- Network errors (no internet, timeout)
- Invalid usernames (404 from API)
- Empty activity (user has no recent events)
- Invalid JSON responses

**Try it yourself!**

- Add try-except blocks
- Provide helpful error messages
- Test with invalid usernames like "xyzabc123notarealuser"

**When ready to check your work, let me know!**

---

## Resources

- [GitHub REST API Documentation](https://docs.github.com/rest)
- [Python urllib Documentation](https://docs.python.org/3/library/urllib.html)
- [Python json Module](https://docs.python.org/3/library/json.html)
- [Python sys Module](https://docs.python.org/3/library/sys.html)

## Next Steps

Once you complete the basic version, consider adding:

- Filter results by event type
- Display limited number of results (newest first)
- Add timestamps to events
- Display activity statistics
- Cache results locally
- Add more detailed event information

## Tips

- Start with Step 1 and work sequentially
- Test each step before moving to the next
- Print intermediate values to debug
- Use realistic GitHub usernames for testing
- Read error messages carefully - they often point to the issue

Good luck! 🚀
