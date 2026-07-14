"""
=========================================================
LoveLens AI
Dashboard Charts
=========================================================
"""

import plotly.express as px


def create_prediction_pie_chart(history):
    """
    Prediction Distribution Pie Chart
    """

    figure = px.pie(

        history,

        names="prediction",

        title="Prediction Distribution"

    )

    return figure


def create_love_score_bar_chart(history):
    """
    Love Score Bar Chart
    """

    figure = px.bar(

        history,

        x="username",

        y="love_score",

        color="prediction",

        title="Love Score by User"

    )

    return figure


def create_confidence_chart(history):
    """
    Confidence Chart
    """

    figure = px.bar(

        history,

        x="username",

        y="confidence",

        color="prediction",

        title="Confidence Score"

    )

    return figure


def create_score_distribution(history):
    """
    Love Score Distribution
    """

    figure = px.histogram(

        history,

        x="love_score",

        nbins=10,

        title="Love Score Distribution"

    )

    return figure