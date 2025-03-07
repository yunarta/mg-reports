from datetime import datetime, timedelta

context = {
    "archive_date": (datetime.now() - timedelta(days=1)).strftime('%Y-%m-%d')
}