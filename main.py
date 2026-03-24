#!/usr/bin/env python3
"""
Reddit Personal Insight Tool
Simple read-only local script for personal subreddit insights.
Strictly for personal use only.
"""

import praw
import time
from datetime import datetime
import sys

# ==================== CONFIGURATION ====================
# AFTER API APPROVAL, REPLACE THESE:
CLIENT_ID = "YOUR_CLIENT_ID_HERE"
CLIENT_SECRET = "YOUR_CLIENT_SECRET_HERE"
USER_AGENT = "PersonalInsightTool/1.0 (by u/Physical-Honey-1623; local personal read-only script)"

# Small fixed list of subreddits you actually use
SUBREDDITS = [
    "programming",
    "dataisbeautiful",
    "technology",
    "AskReddit"
]

MAX_ITEMS = 30      # Keep volume very low
DELAY = 3           # Seconds between requests
# ======================================================

def main():
    print("=== Reddit Personal Insight Tool ===\n")
    print(f"User-Agent: {USER_AGENT}")
    print(f"Target subreddits: {', '.join(SUBREDDITS)}\n")
    
    if CLIENT_ID == "YOUR_CLIENT_ID_HERE":
        print("❌ Please fill in CLIENT_ID and CLIENT_SECRET after API approval.")
        print("Then run the script again.")
        sys.exit(1)

    try:
        reddit = praw.Reddit(
            client_id=CLIENT_ID,
            client_secret=CLIENT_SECRET,
            user_agent=USER_AGENT,
            check_for_async=False
        )
        
        print("✅ Connected to Reddit API (read-only)\n")
        
        for sub_name in SUBREDDITS:
            print(f"Analyzing r/{sub_name} ...")
            subreddit = reddit.subreddit(sub_name)
            
            print(f"   Subscribers: {subreddit.subscribers:,}")
            print(f"   Created: {datetime.fromtimestamp(subreddit.created_utc).strftime('%Y-%m-%d')}")
            
            print(f"   Recent posts (up to {MAX_ITEMS}):")
            post_count = 0
            total_upvotes = 0
            total_comments = 0
            
            for submission in subreddit.new(limit=MAX_ITEMS):
                post_count += 1
                total_upvotes += submission.score
                total_comments += submission.num_comments
                if post_count <= 5:
                    title = submission.title[:80]
                    print(f"     • {title}{'...' if len(submission.title) > 80 else ''}")
            
            if post_count > 0:
                avg_upvotes = total_upvotes / post_count
                avg_comments = total_comments / post_count
                print(f"   Avg upvotes: {avg_upvotes:.1f} | Avg comments: {avg_comments:.1f}")
            
            print(f"   Fetched {post_count} posts.\n")
            time.sleep(DELAY)
        
        print("✅ Run complete. All data processed locally and discarded.")
        print("Tool stayed well under rate limits.")
        
    except Exception as e:
        print(f"❌ Error: {e}")
        print("Check your credentials and ensure you have API approval.")

if __name__ == "__main__":
    main()
