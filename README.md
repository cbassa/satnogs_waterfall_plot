# satnogs_waterfall_plot
Generate scaled SatNOGS waterfall plots

The default SatNOGS `gnuplot` script uses power levels from -100 to -50 dB. Some SatNOGS stations have power levels outside this range, or power levels that fluctuate in time and frequency.

This `python` script uses `matplotlib` to compute the average power level of the waterfall, and uses the standard deviation to scale the dynamic range of the output plot accordingly. The default calculation it uses is a dynamic range ranging from the mean minus twice the standard deviation, upto the mean times six times the standard deviation.

By default it uses the `jet` colormap, but any colormap from the [`matplotlib` library](https://matplotlib.org/examples/color/colormaps_reference.html) can be used.
