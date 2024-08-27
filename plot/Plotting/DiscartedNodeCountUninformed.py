import json
import os
import plotly.graph_objs as go
from plotly.subplots import make_subplots



fig.update_layout(
    title="Optimality of Solutions Across Uninformed Algorithms Grouped By Level",
    xaxis_title="Levels",
    yaxis_title="Steps to solution",
    barmode='group'
)

fig.update_layout(
        font=dict(
            size=32           # Increase this value to make the font bigger
        ),
        title=dict(
            font=dict(size=32)  # Title font size
        ),
        xaxis=dict(
            title_font=dict(size=24),  # X-axis title font size
            tickfont=dict(size=20)     # X-axis labels font size
        ),
        yaxis=dict(
            title_font=dict(size=24),  # Y-axis title font size
            tickfont=dict(size=20)     # Y-axis labels font size
        ),
        legend=dict(
            font=dict(size=20)  # Legend font size
        )
    )

# Mostramos el gráfico
fig.show()