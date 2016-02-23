def _hist_key_in_ax(ax, key, label, data):
    bins = 50
    ax.hist([x[key] for x in data], bins)

def plot_keys(axs, keys, labels, data):
    for (ax, key, label) in zip(axs, keys, labels):
        _hist_key_in_ax(ax, key, label, data)
