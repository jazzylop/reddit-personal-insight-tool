# Reddit Personal Insight Tool

A lightweight, local-only Python script for personal use.  
It helps users better understand subreddit posting norms and recent activity patterns using the official Reddit Data API (read-only).

## Purpose
- Quickly check public subreddit metadata and limited recent posts
- See basic patterns (post frequency, typical engagement) to improve your own submissions
- Reduce rejected posts by understanding community guidelines better
- Strictly personal, no automation, no data sharing

## Features
- Read-only OAuth access
- Limited queries to a small list of subreddits you personally use
- Simple console output with summaries
- Built-in rate limiting and delays
- No posting, voting, or write actions

## Tech Stack
- Python 3.10+
- PRAW (Reddit API wrapper)

## Compliance
Fully read-only. No data is stored persistently. Everything is discarded after each run.  
User-Agent is clearly labeled.  
This project complies with Reddit’s Responsible Builder Policy.

## Setup
1. Install dependencies: `pip install praw`
2. After API approval, create a **script** app at https://www.reddit.com/prefs/apps and fill in the credentials in `main.py`
3. Run `python main.py`

## Status
WIP – awaiting Reddit Data API approval to test live functionality.

Created for u/Physical-Honey-1623
