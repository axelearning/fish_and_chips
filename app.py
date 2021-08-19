import streamlit as st
import pandas as pd
import plotly.graph_objects as go
from fastai.vision.all import PILImage, load_learner


MODEL_FILE_NAME = "resnet50.pkl"


@st.cache
def load_image(image_file): return PILImage.create(image_file)


@st.cache
def load_model(): return load_learner(MODEL_FILE_NAME)


def create_barchart(value, index):
    df = pd.Series(value, index=index)
    df.sort_values(inplace=True)

    fig = go.Figure(
        [
            go.Bar(
                x=df.values,
                y=df.index,
                hovertemplate="%{x:.1%}<extra></extra>",
            ),
        ]
    )
    fig.update_layout(hovermode="y", showlegend=False, barmode="overlay")
    fig.update_traces(orientation="h")
    fig.update_xaxes(
        showgrid=False,
        showticklabels=False,
        zeroline=False,
        showline=False,
        fixedrange=True,
    )
    fig.update_yaxes(showgrid=False, showline=False, fixedrange=True)
    return fig


st.title("Fish Classifier 🐠")
st.write("a simple application to classify  fish from the Reunion Island’s lagoon")
image_file = st.file_uploader("", type=["png", "jpg", "jpeg"])

if image_file:

    image = load_image(image_file)
    model = load_learner(MODEL_FILE_NAME)

    pred, _, probs = model.predict(image)

    st.image(image)
    st.title(pred)

    fig = create_barchart(value=probs, index=model.dls.vocab)
    config = dict({"displayModeBar": False})
    st.plotly_chart(fig, use_container_width=True, config=config)
