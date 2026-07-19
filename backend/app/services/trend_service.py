from pytrends.request import TrendReq


class TrendService:

    @staticmethod
    def get_trend(keyword: str):
        """
        Fetch Google Trend score for a keyword.
        """

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

        if score >= 70:
            trend = "Increasing"

        elif score >= 40:
            trend = "Stable"

        else:
            trend = "Decreasing"

        return {
            "keyword": keyword,
            "trend": trend,
            "trend_score": score
        }

    @staticmethod
    def get_google_trend(keyword: str):
        """
        Backward compatibility.
        """
        return TrendService.get_trend(keyword)