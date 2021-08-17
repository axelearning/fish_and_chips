import streamlit as st
from PIL import Image
from fastai.vision.all import *
from fastai.vision.widgets import *
import plotly.graph_objects as go

# Load an Image
@st.cache
def load_image(image_file):
    return PILImage.create(image_file)


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


FILE = "resnet50.pkl"
model = load_learner(FILE)

st.title("Fish Classifier 🐠")
st.write("a simple application to classify  fish from the Reunion Island’s lagoon")
image_file = st.file_uploader("", type=["png", "jpg", "jpeg"])

if image_file:

    image = load_image(image_file)
    st.image(image)

    pred, _, probs = model.predict(image)
    st.title(pred)

    fig = create_barchart(value=probs, index=model.dls.vocab)
    config = dict({"displayModeBar": False})
    st.plotly_chart(fig, use_container_width=True, config=config)
