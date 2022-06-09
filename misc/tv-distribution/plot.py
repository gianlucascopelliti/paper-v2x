import re

import matplotlib.pyplot as plt
import tikzplotlib

def save_tikz(file, width="15cm", height="8cm"):
    tikzplotlib.save(file, strict=True, axis_width=width, axis_height=height)

    with open(file, "r") as f:
        tikz_file = f.read()

    # fix legend size
    tikz_file = tikz_file.replace("legend style={", "legend style={font=\\small,")
    
    # show tick labels
    tikz_file = tikz_file.replace("xmajorticks=false", "xmajorticks=true")
    tikz_file = tikz_file.replace("ymajorticks=false", "ymajorticks=true")

    tickstyle_regex = "([xy])tick style={(.+)}"
    matches = re.findall(tickstyle_regex, tikz_file)

    # hide ticks
    for match in matches:
        tikz_file = tikz_file.replace(
            f"{match[0]}tick style={{{match[1]}}}",
            f"{match[0]}tick style={{{match[1]},draw=none}}"
        )

    # adjust vertical spacing between plots
    tikz_file = tikz_file.replace(
        "group style={",
        "group style={vertical sep=3.5cm, horizontal sep=2.5cm,"
    )

    options = [
        "clip=false", # set clip=false to show labels outside the plot
        "label style={font=\Huge}",
        "tick label style={font=\Huge}",
        "title style={font=\Huge}"
    ]

    options_str = ",\n".join(options)
    tikz_file = tikz_file.replace(
        "}\n]",
        "},\n" + options_str + "\n]"
    )

    # TODO fix "yticklabel style": "anchor=center,yshift=6pt"

    with open(file, "w") as f:
        f.write(tikz_file)

HB_PER_TV = 30

# sizes are in bytes
PS_SIZE = 64
TS_SIZE = 8
SIG_SIZE = 512

x = [30, 150, 300, 900]

# first plot: revocation time t_eff
y_teff = [a * 2 / 60 for a in x]

# second plot: frequency of HBs
y_hb_freq = [HB_PER_TV / a * 60 for a in x]

# third plot: size of PRL
y_prl = [16, 43, 71, 160]

# fourth plot: bandwidth (values in KBit/s)
hb_sizes = [(a * PS_SIZE + TS_SIZE + SIG_SIZE) * 1e-3 for a in y_prl] # KB
hb_frequencies = [HB_PER_TV / a for a in x] # 1/s
y_bandwidth = [a * b * 8 for a, b in zip(hb_sizes, hb_frequencies)] # KBit/s


print(f"X values: {x}")
print(f"T_eff: {y_teff}")
print(f"HB sizes: {hb_sizes}")
print(f"Frequency of HBs: {y_hb_freq}")
print(f"Bandwidth: {y_bandwidth}")

#plt.figure(figsize=(20,4))
fig, axs = plt.subplots(2,2, sharex=True, sharey=False)
#fig.suptitle('Impact of $T_v$ on different dimensions')

fst = axs[0,0]
snd = axs[0,1]
trd = axs[1,0]
fth = axs[1,1]

#fst = axs[0]
#snd = axs[1]
#trd = axs[2]
#fth = axs[3]

# seaborn `colorblind` palette: 
# ['#0173b2', '#de8f05', '#029e73', '#d55e00', '#cc78bc', '#ca9161', '#fbafe4', '#949494', '#ece133', '#56b4e9']

# first plot
fst.plot(x, y_teff, '#0173b2')
fst.set_title('$T_{eff}$ (min)')
fst.get_yaxis().set_label_coords(-0.1,0.5)

# second plot
snd.plot(x, y_hb_freq, '#de8f05')
snd.set_title('HB frequency (HB/min)')
snd.get_yaxis().set_label_coords(-0.1,0.5)

# third plot
trd.plot(x, hb_sizes, '#029e73')
trd.set_title('HB size (KB)')
trd.get_yaxis().set_label_coords(-0.1,0.5)

# fourth plot
fth.plot(x, y_bandwidth, '#d55e00')
fth.set_title('Required bandwidth (KBit/s)')
fth.get_yaxis().set_label_coords(-0.1,0.5)

for ax in axs.flat:
    #ax.set(xlabel='$T_v$ (s)')
    ax.xaxis.set_tick_params(labelbottom=True)


# set ticks and tick labels
plt.xticks(x)
#formatter = matplotlib.ticker.FuncFormatter(lambda s, x: f"{s/60:.1f}")
#ax.xaxis.set_major_formatter(formatter)

plt.subplots_adjust(left=0.12,
                    bottom=0.1,
                    right=0.95,
                    top=0.85,
                    wspace=0.4,
                    hspace=0.8)

#plt.savefig("plot.png", format="png")
save_tikz("tv-distribution.tex", height="6cm")