import matplotlib.pyplot as plt

def generate_bar_chart(labels, values):
  fig, ax = plt.subplots()
  ax.bar(labels, values)
  plt.savefig('./app/bar')

def generate_pie_chart(labels, values):
  fig, ax = plt.subplots()
  ax.pie(values)
  ax.axis('equal')
  ax.legend( labels=labels, loc='center left')
  plt.savefig('./app/pie')

if __name__ == '__main__':
  labels = ['a', 'b', 'c']
  values = [10, 40, 800]
  # generate_bar_chart(labels, values)
  generate_pie_chart(labels, values)