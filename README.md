# satnogs_waterfall_plot
Generate scaled SatNOGS waterfall plots

The default SatNOGS `gnuplot` script uses power levels from -100 to -50 dB. Some SatNOGS stations have power levels outside this range, or power levels that fluctuate in time and frequency.

This `python` script uses `matplotlib` to compute the average power level of the waterfall, and uses the standard deviation to scale the dynamic range of the output plot accordingly. The default calculation it uses is a dynamic range ranging from the mean minus twice the standard deviation, upto the mean times six times the standard deviation.

By default it uses the `jet` colormap, but any colormap from the [`matplotlib` library](https://matplotlib.org/examples/color/colormaps_reference.html) can be used.

To use this plotter, adapt the `observer.py` script of `satnogs-client` (located at `/var/lib/satnogs/lib/python2.7/site-packages/satnogsclient/observer/observer.py` on Raspbian) by commenting out the `gnuplot` command and substituting it with the `python` script of this repository. You may have to adjust the path of the `python` script if you're not running Raspbian.

```
#            plot = subprocess.call("gnuplot -e \"inputfile='%s'\" \                                                                                                                                                                                            
#                                   -e \"outfile='%s'\" -e \"height=1600\" \                                                                                                                                                                                    
#                                   /usr/share/satnogs/scripts/satnogs_waterfall.gp" %                                                                                                                                                                          
#                                   (self.observation_waterfall_file,                                                                                                                                                                                           
#                                    self.observation_waterfall_png),                                                                                                                                                                                           
#                                   shell=True)                                                                                                                                                                                                                 
	    plot = subprocess.call("python /home/pi/satnogs_waterfall_plotter.py %s %s" %
                                   (self.observation_waterfall_file,
                                    self.observation_waterfall_png),
                                   shell=True)
