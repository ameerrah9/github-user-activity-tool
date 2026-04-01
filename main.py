#!/usr/bin/env python3
"""
GitHub User Activity Tool
Fetches and displays recent activity of a GitHub user.

Usage: python main.py <github-username>
Example: python main.py kamranahmedse
"""

# Your implementation goes here!
import sys
import urllib.request
import urllib.error
import json
from datetime import datetime

def format_timestamp(timestamp_str):
    dt = datetime.strptime(timestamp_str, "%Y-%m-%dT%H:%M:%SZ")
    return dt.strftime("%I:%M %p, %m/%d/%Y")

def display_activity(activity_data):
    result = []
    for event in activity_data:
        if 'PushEvent' in event['type']:
            result.append(f"  Pushed {len(event['payload']['commits'])} commit(s) to {event['repo']['name']} at {format_timestamp(event['created_at'])}")
        elif 'IssuesEvent' in event['type']:
            result.append(f"  {event['payload']['action']} issue #{event['payload']['issue']['number']} in {event['repo']['name']} at {format_timestamp(event['created_at'])}")
        elif 'StarEvent' in event['type']:
            result.append(f"  Starred {event['repo']['name']} at {format_timestamp(event['created_at'])}")
        elif 'CreateEvent' in event['type']:
            result.append(f"  Created {event['payload']['ref_type']} {event['payload']['ref']} in {event['repo']['name']} at {format_timestamp(event['created_at'])}")
        elif 'DeleteEvent' in event['type']:
            result.append(f"  Deleted {event['payload']['ref_type']} {event['payload']['ref']} in {event['repo']['name']} at {format_timestamp(event['created_at'])}")
        elif 'PullRequestEvent' in event['type']:
            result.append(f"  {event['payload']['action']} pull request #{event['payload']['number']} in {event['repo']['name']} at {format_timestamp(event['created_at'])}")
        elif 'WatchEvent' in event['type']:
            result.append(f"  Starred {event['repo']['name']} at {format_timestamp(event['created_at'])}")
        else:
            result.append(f"  {event['type']} in {event['repo']['name']} at {format_timestamp(event['created_at'])}")
    return result

def fetch_github_activity(username):
    # This function will fetch the recent activity of the specified GitHub user.
    # You can use the GitHub API to get this information.
    # For example, you can use the endpoint: https://api.github.com/users/{username}/events

    # Send a GET request to the GitHub API
    req = urllib.request.Request(f"https://api.github.com/users/{username}/events", headers={'User-Agent': 'GitHub-Activity-Tool'})

    try:
        response = urllib.request.urlopen(req)
        data = json.load(response)
        return data
    except urllib.error.HTTPError as e:
        print(f"HTTP Error: {e.code} - {e.reason}")
        sys.exit(1)
    except urllib.error.URLError as e:
        print(f"URL Error: {e.reason}")
        sys.exit(1)
    except Exception as e:
        print(f"An error occurred: {e}")
        sys.exit(1)

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python main.py <github-username>")
        sys.exit(1)

    username = sys.argv[1]
    print(f"Fetching recent activity for GitHub user: {username}")
    activity_data = fetch_github_activity(username)

    try:
        activities = display_activity(activity_data)
    except KeyError as e:
        print(f"Unexpected data format: missing key {e}")
        sys.exit(1)

    if not activities:
        print("No activity found.")
    else:
        for activity in activities:
            print(activity)
