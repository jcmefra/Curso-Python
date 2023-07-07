import charts

def run():
    charts.generate_pie_chart()
    charts.generate_bar_chart()

if __name__ == '__main__':
    labels = ['a', 'b', 'c']
    values = [42, 36, 88]

    charts.generate_bar_chart(labels, values)
    charts.generate_pie_chart(labels, values)