from agents.drdo_agent import fetch_drdo_updates
from agents.isro_agent import fetch_isro_updates
from database.intel_db import init_db, save_intelligence


def run_intelligence_engine():

    print("\n=== NATIONAL DEFENCE & SPACE INTELLIGENCE FEED ===\n")

    init_db()

    drdo_updates = fetch_drdo_updates() or []
    isro_updates = fetch_isro_updates() or []

    all_updates = drdo_updates + isro_updates

    if len(all_updates) == 0:
        print("No intelligence updates found.")
        return

    save_intelligence(all_updates)

    for i, item in enumerate(all_updates, start=1):

        print(f"[INTEL {i}]")
        print(f"SOURCE: {item['source']}")
        print(f"CATEGORY: {item['category']}")
        print(f"TITLE: {item['title']}")
        print("-" * 60)


if __name__ == "__main__":
    run_intelligence_engine()