import random # Create coin lists
import matplotlib.pyplot as plt # Use matplotlib for graphs
import matplotlib.patches as mpatches
from matplotlib.ticker import StrMethodFormatter
import statistics # Stdev from built in
from scipy.stats import iqr # IQR from scipy
import timing # Logs program runtime

random.seed(a = None, version=2)

def flipCoins(repetitions, trials): # Flips coins, creates list of proport with len = trials and flips per prop = repetitions
    proportion_list = []
    for i in range(1, trials + 1):
        random_list = []
        for j in range(1, repetitions):
            random_number = random.randint(0,1)  
            random_list.append(random_number)
        proportion = sum(random_list) / repetitions
        proportion_list.append(proportion)
    return(proportion_list) 

proportions_100 = flipCoins(100, 20)
proportions_25 = flipCoins(25, 20)

def logStats(): # Shows other statistics needed for project in terminal
    print('Average of 100:', sum(proportions_100)/len(proportions_100))
    print('Stdev of 100:', statistics.stdev(proportions_100))
    print('IQR of 100:', iqr(proportions_100))

    print('----------------------------------')

    print('Average of 25:', (sum(proportions_25)/len(proportions_25)))  
    print('Stdev of 25:', statistics.stdev(proportions_25))
    print('IQR of 25:', iqr(proportions_25))

def getBins(num_bins): # Gets bin sizes, locations of x tick marks for graph depending on how many bins you want
    sorted_props = sorted(proportions_25)
    difference = sorted_props[-1] - sorted_props[0]
    bin_size = difference / num_bins
    bins = [sorted_props[0]]

    for num in range(1, num_bins + 1):
        bins.append(sorted_props[0] + bin_size * num)

    left_tick = []
    for num in bins:
        left_tick.append(num - bin_size / 2)

    left_tick_label = []
    for num in left_tick:
        left_tick_label.append(round(num, 2))
    return left_tick, bins

def plot(trials, save_file, bins): # Creates graph in save_file (which should be in png format - I used merged.png), bins = number of bins you want
    xmarks, binlocs = getBins(bins)
    plt.title('Sample Proportion Distribution of Coin Flips over ' + str(trials) + ' Trials',fontsize=14)
    plt.xlabel('Sample Proportion (Bin Size = .025)')
    plt.ylabel('Frequency')
    plt.hist(proportions_100, binlocs, align='left', facecolor='navy', alpha=.9, ec='black')
    plt.hist(proportions_25, binlocs, align='left', facecolor='mistyrose', alpha=.8, ec='black')
    patch25 = mpatches.Patch(color='navy', alpha = .9, label='100 Tosses')
    patch100 = mpatches.Patch(color='mistyrose', alpha = .8, label='25 Tosses')
    plt.legend(handles = [patch25, patch100])
    plt.xticks(xmarks)
    plt.gca().xaxis.set_major_formatter(StrMethodFormatter('{x:,.2f}')) # Rounds xticks down
    plt.savefig(save_file)

plot(20, 'merged.png', 8)
logStats()
