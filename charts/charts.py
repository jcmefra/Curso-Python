import matplotlib.pyplot as plt

def generate_bar_chart(labels, values):
    fig, ax = plt.subplots()
    ax.bar(labels, values)
    name = 'bar'
    plt.savefig('charts/{}'.format(name))
    plt.close()

def generate_pie_chart(labels, values):
    fig, ax = plt.subplots()
    ax.pie(values, labels = labels)
    ax.axis('equal')
    name = 'pie'
    plt.savefig('charts/{}}'.format(name))
    plt.close()

