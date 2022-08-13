# Understanding Airbnb Rental Prices, Property Reviews and Vacancy Rates

## Libraries Used
   * Pandas
   * NLTK
   * Matplotlib/Seaborn
   * GeoPandas
   * Statsmodels
   * Missingno
   * WordCloud

## Skills Used
   * Data Cleaning and the whole ETL process
   * Statistical Modeling
   * Data Visualization
   * Geospatial Data Manipulation
   * Module Development

## Project Motivation
The questions considered in this project are motivated by two primary scenarios:

   1. An price conscious individual who is looking to travel to Boston, MA or
   Seattle, WA and would like to know the quantitative effect that certain
   aspects of the property have on the rental price. In addition, this individual
   would like to how location within each of these cities affects price as they
   perform their search for a property to stay in during their travels. Also, maybe
   this individual is interested to see how does location affect the availability
   of a property.

   2. Imagine yourself as someone who is in the financial position to buy a
   second small property in one of these cities to list on Airbnb in order to
   generate an additional stream of income. You are interested in the above questions
   as well but from a different perspective. For example, now you're interested in
   how location within each of these cities affects the availability of the
   property; a property that has a high vacancy rate (no guests!) is a
   property that is losing money. Or you might interested in how the characteristics
   of a property influence its rental price as you decide how to price your property.

2/3 of the questions proposed in this project is relevant from _both_ of
these scenarios and 1 question is really only relevant from _scenario 2_.

### Questions
  1. How do factors like number of bedrooms/bathrooms, property type (house/apartment)
  affect the rental price of a property?

  2. How does location affect the availability _and_ price of the property?

  3. Can we find recurring themes in comments left in high reviews for a property?
  What about recurring problems in comments left in low reviews for a property?

  These are the main questions that I would like to emphasize in this project. There
  are other smaller questions that are asked and answered in the EDA as well that might
  be of interest.


## File Descriptions

1. data_cleaning.ipynb

   * This is a Jupyter notebook that performs duplicate/missingness analysis and
   cleans the Airbnb data.

2. data_analysis.ipynb
   * This is a Jupyter notebook that conducts the analysis and answers the questions for the _clean_ Airbnb data.

3. pretty_plots (directory)
   * This is a python module written by me that constructs clean customized plots that are specific to this project. The plotting functions in this module do have general application though in that they can be used for other datasets, but other data must be massaged into a similar form.

4. cleaning_utils (directory)
   * This is a python module written by me that cleans the airbnb dataframe as I have clean them in this project. The functions in this module are specific to Airbnb data and can be used for other cities.

5. seattle_data (directory)
   * The original unclean Seattle Airbnb dataset.

6. boston_data (directory)
   * The original unclean Boston Airbnb dataset.

7. venv (directory)
   * Directory containing virtual environment module/packages etc. Unless you want things to break _don't touch this_ except for installing more packages/modules.

8. _____.json (multiple files)
   * These are files that contain feature data type information. These are important for importing the data into python - they tell the pd.read_csv(.) what type to
   assign each feature/variable.

9. seattle_listings.csv
   * The _clean_ Airbnb listings data for _Seattle only_.

10. boston_listings.csv
   * The _clean_ Airbnb listings data for _Boston only_.

11. calendar_listings.csv
   * This is the _seattle_listings.csv_ and _boston_listings.csv_ concatenated row-wise.

12. reviews_concatenated.csv
   * This is the Airbnb reviews dataset for _both_ Seattle and Boston concatenated row-wise.

13. boston_calendar.csv
   * The _clean_ Airbnb calendar dataset for Boston _only_.

14. seattle_calendar.csv
   * The _clean_ Airbnb calendar dataset for Seattle _only_.

15. zip_codes_boundaries (directory)
   * This directory contains the .shp files that contain the zipcode geoemtries necessary to make a map of the Seattle and Boston.

16. requirements.txt
   * A text file listing packages and modules that this project is dependent on.

## How to Interact With This Repository

```bash
git clone 'https'
cd project_1_airbnb
```

## Installations
In case you need to reinstall the dependencies listed in _requirements.txt_ enter the following into the
```bash
pip install -r requirements.txt
```

## License (MIT)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
