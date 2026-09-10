import pandas as pd

columns_needed = [
    "Country",
    "Government: Country name - conventional long form",
    "Government: Capital - name",
    "Geography: Climate",
    "Geography: Terrain",
    "Geography: Coastline",
    "Environment: Environment - current issues",
    "Environment: Environment - international agreements - party to",
    "Geography: Location",
    "Geography: Map references",
    "Geography: Area - comparative",
    "Government: Government type",
    "Government: Independence",
    "Government: International organization participation",
    "Military and Security: Military expenditures",
    "People and Society: Ethnic groups",
    "People and Society: Languages",
    "People and Society: Religions",
    "People and Society: Infant mortality rate - total",
    "People and Society: Life expectancy at birth - total population",
    "People and Society: Population growth rate",
    "People and Society: Population distribution",
    "People and Society: Literacy - male",
    "People and Society: Literacy - female",
    "People and Society: Median age - total",
    "People and Society: Net migration rate",
    "Transnational Issues: Refugees and internally displaced persons - refugees (country of origin)",
    "Economy: GDP (official exchange rate)",
    "Economy: Real GDP per capita",
    "Geography: Natural resources",
    "Geography: Amount arable land",
    "Economy: Exports - commodities",
    "Economy: Exports - partners",
    "Economy: Imports - commodities",
    "Economy: Imports - partners",
]

# 1. Read the CSV file
df = pd.read_csv("/Users/giwen/projects/code/scripts/auto-cp-web/data/filtered_countries.csv")

# 2. Keep only the columns that match your list and exist in the CSV
valid_columns = [col for col in columns_needed if col in df.columns]
df_filtered = df[valid_columns]

# 3. Save to a new file (or replace the filename to overwrite)
df_filtered.to_csv("/Users/giwen/projects/code/scripts/auto-cp-web/data/filtered_countries_2.csv", index=False)

print(f"Retained {len(valid_columns)} of {len(columns_needed)} requested columns.")
