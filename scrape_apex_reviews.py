import json
import steamreviews
import pandas as pd


APP_ID = 1172470  # Apex Legends
REQUEST_PARAMS = {
    "language": "english",
    "filter": "recent",
    "day_range": "90",
}


def main():
    review_dict, _ = steamreviews.download_reviews_for_app_id(
        APP_ID,
        chosen_request_params=REQUEST_PARAMS,
    )

    # Save raw scraped JSON
    raw_json_path = f"data/review_{APP_ID}.json"
    with open(raw_json_path, "w", encoding="utf-8") as f:
        json.dump(review_dict, f, ensure_ascii=False, indent=2)

    # Transform into tabular format for analysis
    records = []
    for _, review in review_dict.get("reviews", {}).items():
        records.append(
            {
                "name": review.get("author", {}).get("steamid"),
                "language": review.get("language"),
                "text": review.get("review"),
                "label": bool(review.get("voted_up")),
            }
        )

    df = pd.DataFrame(records)
    csv_path = f"review_{APP_ID}.csv"
    df.to_csv(csv_path, index=False, encoding="utf-8")

    print(f"Saved raw JSON: {raw_json_path}")
    print(f"Saved CSV: {csv_path}")
    print(f"Total reviews: {len(df):,}")


if __name__ == "__main__":
    main()
