import utils 

data = [
    {
    'country': 'Colombia',
    'population': 500
    },
    {
    'country': 'Peru',
    'population': 200
    }
]

def run():
    keys, values = utils.get_population()
    print(keys, values)


    country = input('Digite el país: ')
    result = utils.population_by_country(data, country)
    print(result)

    print(utils.A)

if __name__ == '__main__': #Entry Point para ejecutar main.py directamente desde la terminal
    run()