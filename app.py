import pandas as pd
from flask import Flask, render_template, request
from country_io import get_country_info, country_name_converter
from data.info import columns_needed

app = Flask(__name__)

# Load data once at startup
df = pd.read_csv("data/filtered_countries.csv")
df["Country"] = df["Country"].str.lower()

@app.route("/", methods=["GET", "POST"])
def index():
    country_data = None
    searched_country = None
    error = None

    if request.method == "POST":
        # Get country name submitted via HTML form
        searched_country = request.form.get("country", "").strip().lower()

        searched_country = country_name_converter(searched_country)

        if not searched_country:
            error = "Please enter a country name."
        elif searched_country not in df["Country"].values:
            error = f"'{searched_country.title()}' could not be found. Please check the spelling."
        else:
            try:
                country_data = get_country_info(df, searched_country, columns_needed)
            except Exception as e:
                error = f"An unexpected error occurred: {str(e)}"

    return render_template(
        "index.html",
        country=searched_country,
        country_data=country_data,
        error=error
    )

if __name__ == "__main__":
    app.run(debug=True)
