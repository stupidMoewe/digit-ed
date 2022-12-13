import piplite
await piplite.install("ipywidgets")

import ipywidgets as widgets
import matplotlib
import matplotlib.pyplot as plt
#%matplotlib inline


nb_rainy_days_slider = widgets.IntSlider(min=0, max=365, step=1, value=10, description='nb rainy days')
rain_forecast_accuracy_slider = widgets.IntSlider(min=0, max=100, step=1, value=20, description='forecast accuracy', style={'description_width': 'initial'})

## Proportion of rainy days graph
def f1(nb_rainy_days):
    SCALE = 19
    FIG_SIZE = 5

    p_rain = nb_rainy_days/365
    p_not_rain = 1 - p_rain

    rainy_days = matplotlib.patches.Rectangle((0, 0),p_rain*SCALE, SCALE, color ='cornflowerblue', alpha = 0.3)
    sunny_days = matplotlib.patches.Rectangle((p_rain*SCALE, 0), p_not_rain*SCALE, SCALE, color = 'orange', alpha = 0.3)

    fig = plt.figure(figsize=(FIG_SIZE,FIG_SIZE))
    ax = fig.add_subplot()
    ax.add_patch(rainy_days)
    ax.add_patch(sunny_days)
    ax.set_xticks([])
    ax.set_yticks([])
    ax.set_xlabel("P(rain)                                                                  P(sun)")

    plt.xlim([0, SCALE])
    plt.ylim([0, SCALE])
    plt.legend(["rainy days ", "sunny days"], loc=(0.65, 0.86))
    plt.show()



## Forecast accuracy graph
def f2(forecast_accuracy, nb_rainy_days):
    SCALE = 19
    FIG_SIZE = 5

    p_rain = nb_rainy_days/365
    p_not_rain = 1 - p_rain

    p_correct = forecast_accuracy/100

    p_forecast_knowing_rain = p_correct
    p_forecast_knowing_not_rain = 1 - p_correct

    p_forecast = p_forecast_knowing_not_rain*p_not_rain + p_forecast_knowing_rain*p_rain
    p_rain_knowing_forecast = p_forecast_knowing_rain*p_rain/p_forecast
    
    correct_forecast = matplotlib.patches.Rectangle((0, 0),p_rain*SCALE, p_forecast_knowing_rain*SCALE, color ='cornflowerblue', )
    wrong_forecast = matplotlib.patches.Rectangle((p_rain*SCALE, 0), p_not_rain*SCALE, p_forecast_knowing_not_rain*SCALE, color = 'orange')
    rainy_days = matplotlib.patches.Rectangle((0, 0), p_rain*SCALE, SCALE, color ='cornflowerblue', alpha = 0.3)
    sunny_days = matplotlib.patches.Rectangle((p_rain*SCALE, 0), p_not_rain*SCALE, SCALE, color ='orange', alpha = 0.3)

    fig = plt.figure(figsize=(FIG_SIZE,FIG_SIZE))
    ax = fig.add_subplot()
    ax.add_patch(rainy_days)
    ax.add_patch(correct_forecast)
    ax.add_patch(sunny_days)
    ax.add_patch(wrong_forecast)

    plt.xlim([0, SCALE])
    plt.ylim([0, SCALE])
    ax.set_xticks([])
    ax.set_yticks([])
    ax.set_xlabel("P(rain)                                                                   P(sun)")
    plt.title("P(rain | rain forecasted) = %.2f" % p_rain_knowing_forecast)
    plt.legend(["rainy day ", "rain forecasted", "sunny day", "rain forecasted :/"], loc=(0.55, 0.75))
    plt.show()
