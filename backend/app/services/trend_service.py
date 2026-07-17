from pytrends.request import TrendReq


class TrendService:

    @staticmethod
    def get_google_trend(keyword: str):

        pytrends = TrendReq(
            hl="en-US",
            tz=330
        )

        pytrends.build_payload(
            [keyword],
            timeframe="today 3-m"
        )

        data = pytrends.interest_over_time()

        if data.empty:
            return {
                "keyword": keyword,
                "trend_score": 0
            }

        score = int(data[keyword].iloc[-1])

        return {
            "keyword": keyword,
            "trend_score": score
        }