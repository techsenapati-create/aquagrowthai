import joblib
import pandas as pd

classifier = joblib.load(
    "models/fish_growth_classifier.pkl"
)

length_model = joblib.load(
    "models/NextLength_model.pkl"
)

weight_model = joblib.load(
    "models/NextWeight_model.pkl"
)

depth_model = joblib.load(
    "models/NextDepth_model.pkl"
)

dlpl_model = joblib.load(
    "models/NextDLPL_model.pkl"
)

perimeter_model = joblib.load(
    "models/NextPerimeter_model.pkl"
)


def classify_growth(
    length,
    weight,
    depth,
    dlpl,
    perimeter,
    sex
):

    sample = pd.DataFrame([{
        "Length": length,
        "Weight": weight,
        "Depth": depth,
        "DLPL": dlpl,
        "Perimeter": perimeter,
        "Sex": sex
    }])

    prediction = classifier.predict(sample)[0]

    stage_names = {
        0: "Preparatory",
        1: "Pre-spawning",
        2: "Spawning",
        3: "Post-spawning"
    }

    return stage_names.get(
        int(prediction),
        "Unknown"
    )


def forecast_growth(
    month_no,
    length,
    weight,
    depth,
    dlpl,
    perimeter,
    sex
):

    sample = pd.DataFrame([{
        "MonthNo": month_no,
        "Sex": sex,
        "Length": length,
        "Weight": weight,
        "Depth": depth,
        "DLPL": dlpl,
        "Perimeter": perimeter
    }])

    return {
        "NextLength":
            round(
                length_model.predict(sample)[0],
                2
            ),

        "NextWeight":
            round(
                weight_model.predict(sample)[0],
                2
            ),

        "NextDepth":
            round(
                depth_model.predict(sample)[0],
                2
            ),

        "NextDLPL":
            round(
                dlpl_model.predict(sample)[0],
                2
            ),

        "NextPerimeter":
            round(
                perimeter_model.predict(sample)[0],
                2
            )
    }