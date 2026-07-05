"""
One-time (or occasional) login helper. Launches a visible Chromium window
with a persistent profile stored in .browser-profile/. Log into meetup.com
manually in the window. The script polls until it detects a logged-in state
(presence of an account/avatar menu), then saves the session to the profile
directory for reuse by scrape.py.
"""
import time
from pathlib import Path
from playwright.sync_api import sync_playwright

PROFILE_DIR = Path(__file__).parent / ".browser-profile"
TIMEOUT_SECONDS = 300

def is_logged_in(page) -> bool:
    try:
        return page.locator("[data-testid='member-dropdown']").count() > 0 \
            or page.locator("a[href*='/members/']").count() > 0 \
            or "meetup.com/home" in page.url
    except Exception:
        return False

def main():
    with sync_playwright() as p:
        context = p.chromium.launch_persistent_context(
            str(PROFILE_DIR),
            headless=False,
        )
        page = context.new_page()
        page.goto("https://www.meetup.com/login/")
        print("A browser window has opened. Please log into meetup.com.")
        print(f"Waiting up to {TIMEOUT_SECONDS}s for login to complete...")

        start = time.time()
        while time.time() - start < TIMEOUT_SECONDS:
            if is_logged_in(page):
                print("Login detected.")
                break
            time.sleep(3)
        else:
            print("Timed out waiting for login. Session will still be saved as-is.")

        time.sleep(2)
        context.close()
        print(f"Session saved to {PROFILE_DIR}")

if __name__ == "__main__":
    main()
